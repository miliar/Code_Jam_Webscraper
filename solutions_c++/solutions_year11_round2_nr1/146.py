#include <iostream>
#include <cstdio>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <numeric>
#include <functional>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <string>
#include <sstream>
#include <fstream>
#include <complex>
#include <iterator>
#include <memory>
#include <utility>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define rep(i,s,n) for(int i=s;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
#define MP(a, b) make_pair((a), (b))
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long double ld;
typedef long long ll;
static const double PI = atan(1.0) * 4.0;

const int M = 100;
int N;
char m[M][M + 1];
double WP[M], OWP[M], OOWP[M];

int main() {
  int T;
  cin >> T;
  REP(turn, T) {
    cin >> N;
    REP(i, N) cin >> m[i];
    // WP
    REP(i, N) {
      int w = 0, g = 0;
      REP(j, N) {
        if (m[i][j] != '.') ++g;
        if (m[i][j] == '1') ++w;
      }
      assert(g != 0);
      WP[i] = (double) w / g;
      //      cout << i << ' ' << WP[i] << endl;
    }
    // OWP
    REP(i, N) {
      int c = 0;
      double s = 0;
      REP(j, N) {
        if (m[i][j] != '.') {
          ++c;
          int w = 0, g = 0;
          REP(k, N) if (k != i) {
            if (m[j][k] != '.') ++g;
            if (m[j][k] == '1') ++w;
          }
          s += (double) w / g;
        }
      }
      assert(c != 0);
      OWP[i] = s / c;
    }
    // OOWP
    REP(i, N) {
      int c = 0;
      double s = 0;
      REP(j, N) {
        if (m[i][j] != '.') {
          ++c;
          s += OWP[j];
        }
      }
      assert(c != 0);
      OOWP[i] = s / c;
    }
    printf("Case #%d:\n", turn + 1);
    REP(i, N) printf("%.12f\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
  }
  return 0;
}
