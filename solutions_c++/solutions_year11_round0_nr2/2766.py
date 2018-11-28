#include <iostream>
#include <string>
#include <map>
#include <utility>
#include <vector>
using namespace std;
int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    int C;
    cin >> C;
    map<pair<char, char>, char> base;
    for (int j = 0; j < C; ++j) {
      string s;
      cin >> s;
      base[make_pair(s[0], s[1])] = s[2];
      base[make_pair(s[1], s[0])] = s[2];
    }
    int D;
    cin >> D;
    map<char, char> opp;
    for (int j = 0; j < D; ++j) {
      string s;
      cin >> s;
      opp[s[0]] = s[1];
      opp[s[1]] = s[0];
    }
    int N;
    cin >> N;
    string str;
    cin >> str;
    vector<char> res(N);
    int ri = 0;
    for (int j = 0; j < N; ++j) {
      res[ri] = str[j];
      if (ri > 0) {
        map<pair<char, char>, char>::iterator it =
          base.find(make_pair(res[ri], res[ri - 1]));
        if (it != base.end()) {
          res[ri - 1] = it->second;
          --ri;
        } else {
          map<char, char>::iterator it = opp.find(res[ri]);
          if (it != opp.end()) {
            for (int k = 0; k < ri; ++k) {
              if (res[k] == it->second) {
                ri = -1;
                break;
              }
            }
          }
        }
      }
      ++ri;
    }
    bool first = true;
    cout << "Case #" << (i + 1) << ": [";
    for (int j = 0; j < ri; ++j) {
      if (first) {
        first = false;
      } else {
        cout << ", ";
      }
      cout << res[j];
    }
    cout << "]" << endl;
  }
  return 0;
}
