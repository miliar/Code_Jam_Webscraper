#include <iostream>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
using namespace std;

int main() {
  int L, D, N;
  string s;
  getline(cin, s);
  sscanf(s.c_str(), "%d %d %d", &L, &D, &N);
  vector<string> dict;
  for (int i = 0; i < D; i++) {
    string s;
    getline(cin, s);
    dict.push_back(s);
  }
  for (int i = 0; i < N; i++) {
    int ans = 0;
    string q;
    getline(cin, q);
    int qi;
    qi = 0;
    vector<string> toks;
    for (int p = 0; p < L; p++) {
      if (q[qi] == '(') {
        int close = q.find(')', qi+1);
        assert(close != -1);
        toks.push_back(q.substr(qi+1, close-(qi+1)));
        qi = close+1;
      } else {
        toks.push_back(string("") + q[qi]);
        ++qi;
      }
    }
    bool good;
    for (int w = 0; w < D; w++) {
      good = true;
      for (int c = 0; c < L; c++) {
        if (toks[c].find(dict[w][c]) == -1) {
          good = false;
          break;
        }
      }
      if (good) ++ans;
    }
    cout << "Case #" << (i+1) << ": " << ans << endl;
  }
  return 0;
}
