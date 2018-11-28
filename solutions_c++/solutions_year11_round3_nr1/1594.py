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

int R, C;
char fld[55][55];

int main() {
  int i, j, k, tcc;
  int tc = in();
  for (tcc = 1; tc--; tcc++) {
    bool is = 0;
    R = in(), C = in();
    rep(i, R) rep(j, C) {
      cin >> fld[i][j];
      if (fld[i][j] == '#') is = 1;
    }
    bool ok = 1;
    if (is == 0) goto done;
    rep(i, R) rep(j, C) if (fld[i][j] == '#') {
      fld[i][j] = '/';
      if (j + 1 < C and fld[i][j+1] == '#') fld[i][j + 1] = '\\'; else { ok = 0; break; }
      if (i + 1 < R and fld[i+1][j] == '#') fld[i + 1][j] = '\\'; else { ok = 0; break; }
      if (fld[i+1][j+1] == '#') fld[i + 1][j + 1] = '/'; else { ok = 0; break; }
      if (ok == 0) break;
    }
    done:
    printf("Case #%d:\n", tcc);
    if (ok or is == 0) {
      rep(i, R) { rep(j, C) cout << fld[i][j]; cout << endl; }
      continue;
    }
    if (ok == 0) { puts("Impossible"); continue; }
  }
  return 0;
}













