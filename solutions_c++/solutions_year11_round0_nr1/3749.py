#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main(){
  int T;
  cin >> T;
  for(int i = 0; i < T; ++i){
    int ret = 0;
    vector<int> O, B;
    int n;
    cin >> n;
    int o, b, to, tb;
    o = b = 1;
    to = tb = 0;
    for(int j = 0; j < n; ++j){
      char c;
      int h, tmp = 0;
      cin >> c >> h;
      if(c == 'O'){
        tmp = to + 1 + abs(h - o);
        o = h;
        to = ret = max(ret + 1, tmp);
      } else {
        tmp = tb + 1 + abs(h - b);
        b = h;
        tb = ret = max(ret + 1, tmp);
      }
    }
    cout << "Case #" << i + 1 << ": " << ret << endl;
  }
}
