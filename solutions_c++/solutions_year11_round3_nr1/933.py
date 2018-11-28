#include <string>
#include <vector>
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

#define rep(i,n) for (int (i) = 0; (i) < (int)(n); (i)++)
#define REP(i,a,n) for (int(i) = a; (i) < (int)(n); (i)++)
#define iter_type(c) __typeof((c).begin())
#define repi(c, i) for (iter_type(c) i = (c).begin(); i != (c).end(); ++i)
#define pb push_back
#define mp make_pair

#define OSS ostringstream
#define ISS istringstream
#define CAST(x,type)  *({OSS oss; oss << (x); ISS iss(oss.str()); static type _r; iss >> _r; &_r; })
#define ALL(a) (a).begin(), (a).end()

struct Problem {
  int R, C;
  char TI[60][60];

  void Input() {
    scanf("%d %d", &R, &C);
    rep(i, R) {
      cin >> TI[i];
    }
  }

  void Solve() {
    rep(i, R) {
      rep(j, C) {
        char c = TI[i][j];
        if (c == '#') {
          if (i == R - 1 || j == C - 1) goto bad;
          if (TI[i + 1][j] != '#' ||
              TI[i][j + 1] != '#' ||
              TI[i + 1][j + 1] != '#'
              ) goto bad;
          TI[i][j] = '/';
          TI[i + 1][j] = '\\';
          TI[i][j + 1] = '\\';
          TI[i + 1][j + 1] = '/';
        }
      }
    }
    rep(i, R) {
      printf("%s\n", TI[i]);
    }

    return;
 bad:
    printf("Impossible\n");
  }
};

int main() {
  int T;
  scanf("%d", &T);
  for (int testCase = 1; testCase <= T; ++testCase) {
    printf("Case #%d: ", testCase);
    Problem p;
    p.Input();
    printf("\n");
    p.Solve();
  }

  return 0;
}
