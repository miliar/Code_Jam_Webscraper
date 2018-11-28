#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <queue>
#include <set>
#include <sstream>
#include <cmath>

#define REP(i, N) for (int i = 0; i < (int)N; i++)
#define MP(a, b) make_pair(a, b)
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;
int nextInt() {
  char c;
  int res = 0;
  while (!isdigit(c = getchar())){};
  do {
    res = res * 10 + c - '0';
  } while (isdigit(c = getchar()));
  return res;
}

vector<string> rotate(vector<string> v) {
  int R = v.size(), C = v[0].size();
  vector<string> res;
  REP(i, R) res.push_back(string(C, '.'));
  REP(i, R) {
    REP(j, C) {
      res[j][R-i-1] = v[i][j];
    }
  }
  return res;
}

int main() {
  int T;
  cin >> T;
  REP(testcase, T) {
    vector<string> v;
    REP(i, 4) {
      string str;
      cin >> str;
      v.push_back(str);
    }
    bool winx = false, wino = false, nc = false;
    REP(k, 2) {
      REP(i, 5) {
        int x, o, t;
        x = o = t = 0;
        REP(j, 4) {
          switch(v[i == 4 ? j : i][j]) {
          case 'X': x++; break;
          case 'O': o++; break;
          case 'T': t++; break;
          default: nc = true; break;
          }
        }
        if (x == 4 || x == 3 && t == 1) {
          winx = true;
        }
        if (o == 4 || o == 3 && t == 1) {
          wino = true;
        }
      }
      v = rotate(v);
    }
    printf("Case #%d: ", testcase + 1);
    if (winx) {
      puts("X won");
    } else if (wino) {
      puts("O won");
    } else if (nc) {
      puts("Game has not completed");
    } else {
      puts("Draw");
    }
  }
}
