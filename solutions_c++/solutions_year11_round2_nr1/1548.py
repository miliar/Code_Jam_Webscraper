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
  int N;
  char SCH[110][110];

  void Input() {
    scanf("%d", &N);
    rep(i, N) {
      scanf("%s", SCH[i]);
    }
  }

  void Solve() {
    int WINS[110], COUNTS[110];
    double WP[110], OWP[110], OOWP[110];
    memset(WINS, 0, sizeof(WINS));
    memset(COUNTS, 0, sizeof(COUNTS));
    rep(i, N) {
      rep(j, N) {
        if (SCH[i][j] == '1') {
          COUNTS[i]++;
          WINS[i]++;
        } else if (SCH[i][j] == '0') {
          COUNTS[i]++;
        }
      }
      WP[i] = (double)WINS[i] / (double)COUNTS[i];
    }
    rep(i, N) {
      double total = 0.0;
      int ops = 0;
      rep(j, N) {
        if (SCH[i][j] != '.') {
          int count = 0;
          int win = 0;
          rep (k, N) {
            if (k == i) continue;
            if (SCH[j][k] == '1') {
              count++;
              win++;
            } else if (SCH[j][k] == '0') {
              count++;
            }
          }
          total += (double)win / (double)count;
          ops++;
        }
      }
      OWP[i] = total / ops;
    }
    rep(i, N) {
      double total = 0;
      int ops = 0;
      rep(j, N) {
        if (SCH[i][j] != '.') {
          total += OWP[j];
          ops++;
        }
      }
      OOWP[i] = total / ops;
    }
    rep(i, N) {
      double ans = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
      printf("%lf10\n", ans);
    }
  }
};

int main() {
  int T;
  scanf("%d", &T);
  for (int testCase = 1; testCase <= T; ++testCase) {
    printf("Case #%d:\n", testCase);
    Problem p;
    p.Input();
    p.Solve();
  }

  return 0;
}
