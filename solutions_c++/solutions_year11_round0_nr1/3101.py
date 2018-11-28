#include <iostream>
#include <vector>
#include <queue>
#include <cstdlib>

using namespace std;

struct Button{
  int col;
  int n;
};

int solve(vector<Button> &vb){
  int pos[2] = {1,1};
  int res[2] = {0,0};

  for(int i = 0; i < vb.size(); i++){
    int col = vb[i].col;
    int dist = abs(pos[col] - vb[i].n) + 1;
    pos[col] = vb[i].n;
    res[col] += dist;
    if(res[col] <= res[1 - col]){
      res[col] = res[1-col] + 1;
    }
  }
  return res[0] > res[1] ? res[0] : res[1];
}

int main() {
  int t;
  cin >> t;
  for(int i = 0; i < t; i++) {
    int n;
    cin >> n;
    vector<Button> vb;
    for(int l = 0; l < n; l++) {
      Button b;
      char c;
      cin >> c;
      cin >> b.n;
      b.col = c == 'B' ? 0 : 1;
      vb.push_back(b);
    }
    cout << "Case #" << (i+1) << ": " << solve(vb) << endl;
  }
}
