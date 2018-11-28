#include <iostream>
#include <vector>
#include <cstring>
#include <cstdio>

using namespace std;

char COMB[256][256];
bool BOMB[256][256];

int main() {
  int T; cin >> T;
  for(int tt = 1; tt <= T; tt++) {
    memset(COMB, 0, sizeof(COMB));
    memset(BOMB, 0, sizeof(BOMB));

    int C; cin >> C;
    for(int i = 0; i < C; i++) {
      string s; cin >> s;
      COMB[s[0]][s[1]] = s[2];
      COMB[s[1]][s[0]] = s[2];
    }

    int D; cin >> D;
    for(int i = 0; i < D; i++) {
      string s; cin >> s;
      BOMB[s[0]][s[1]] = BOMB[s[1]][s[0]] = true;
    }

    int N; cin >> N;
    string s; cin >> s;
    string t; t += s[0];
    for(int i = 1; i < N; i++) {
      int r = COMB[t[t.size() - 1]][s[i]];
      if(r && r != '?') {
        t[t.size() - 1] = r;
      } else {
        t += s[i];

        for(int j = 0; j < t.size(); j++) {
          if(BOMB[t[j]][s[i]]) {
            t = "";
            if(i + 1 < N) t += s[++i];
            break;
          }
        }
      }
    }

    cout << "Case #" << tt << ": [";
    for(int i = 0; i < t.size(); i++) {
      if(i) cout << ", ";
      cout << t[i];
    }
    cout << "]" << endl;
  }
}
