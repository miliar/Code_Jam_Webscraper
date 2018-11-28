#include <algorithm>
#include <cctype>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <bitset>
#include <cmath>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>

#define REP(i,a,b) for((i)=(a);(i)<(int)(b);(i)++)
#define rep(i,b)   REP(i,0,b)
#define FOR(i,c)   for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c)     (c).begin(), (c).end()

using namespace std;
typedef long long ll;
const double eps = 1e-10;
const int inf = 1<<25;

int in() { int x; scanf("%d", &x); return x; }

double rpi(double wp, double owp, double oowp) {
  return 0.25 * wp + 0.5 * owp + 0.25 * oowp;
}

char table[111][111];
double wp[111], owp[111], oowp[111];
int tot[111], won[111];

int main() {
  int i, j, k, tcc;
  int tc = in();
  for (tcc = 1; tc--; tcc++) {
    int n = in();
    rep(i, n) rep(j, n) cin >> table[i][j];
    rep(i, n) {
      tot[i] = 0, won[i] = 0;
      rep(j, n) if (i != j) {
        if (table[i][j] == '.') continue;
        if (table[i][j] == '1') tot[i]++, won[i]++;
        if (table[i][j] == '0') tot[i]++;
      }
      wp[i] = won[i] / (double)tot[i];
    }
    rep(i, n) {
      owp[i] = 0;
      int cnt = 0;
      rep(j, n) if (i != j) {
        if (table[j][i] == '0' and tot[j] > 1) {
          owp[i] += won[j] / (double)(tot[j] - 1);
          cnt++;
        }
        if (table[j][i] == '1' and tot[j] > 1) {
          owp[i] += (won[j] - 1) / (double)(tot[j] - 1);
          cnt++;
        }
      }
      if (cnt) owp[i] = owp[i] / (double)cnt;
    }
    rep(i, n) {
      oowp[i] = 0;
      int cnt = 0;
      rep(j, n) if (i != j) {
        if (table[i][j] == '.') continue;
        oowp[i] += owp[j];
        cnt++;
      }
      if (cnt) oowp[i] = oowp[i] / (double)cnt;
    }
    printf("Case #%d:\n", tcc);
    rep(i, n) {
      printf("%.10lf\n", rpi(wp[i], owp[i], oowp[i]));
    }
  }
  return 0;
}













