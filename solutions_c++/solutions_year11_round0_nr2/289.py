#include <iostream>
using namespace std;

char inv[26][26];
bool opp[26][26];

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    memset(inv, 0, sizeof(inv));
    memset(opp, 0, sizeof(opp));
    int C; cin >> C;
    for (int i = 0; i < C; i++) {
      string s; cin >> s;
      int x = s[0]-'A', y = s[1]-'A';
      inv[x][y] = inv[y][x] = s[2];
    }
    int D; cin >> D;
    for (int i = 0; i < D; i++) {
      string s; cin >> s;
      int x = s[0]-'A', y = s[1]-'A';
      opp[x][y] = opp[y][x] = true;
    }
    int N; cin >> N;
    string s; cin >> s;
    string res = "";
    for (int i = 0; i < N; i++) {
      res += s[i];
      if (res.size() >= 2) {
        int x = res[res.size()-2]-'A', y = res[res.size()-1]-'A';
        if (inv[x][y] != 0)
          res = res.substr(0, res.size()-2) + inv[x][y];
      }
      for (int j = 0; j < res.size()-1; j++)
        if (opp[res[j]-'A'][res[res.size()-1]-'A']) {
          res = "";
          break;
        }
    }
    cout << "Case #" << c << ": [";
    for (int i = 0; i < res.size(); i++) {
      cout << res[i];
      if (i < res.size()-1) cout << ", ";
    }
    cout << "]" << endl;
  }
  return 0;
}
