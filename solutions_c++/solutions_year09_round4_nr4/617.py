#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iomanip>
#include <memory>
#include <cstring>
#include <climits>
#include <cassert>
#include <list>
using namespace std;

#define ALL(a) (a).begin(), (a).end()
#define PB push_back
#define MP make_pair
#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); (i)++)
#define FORD(i, a, b) for(int (i) = (a); (i) >= (b); (i)--)
#define REP(i, n) for (int (i) = 0; (i) < n; (i)++)
#define SIZE(a) (int)(a).size()
#define DBGN(x) cout << #x << " = " << x << endl;
#define DBG(x) cout << #x << " = " << x << ", ";
#define DBGARR(x, n) REP(i, n) cout << #x << '[' << i << "] = " << x[i] << endl;
#define DBGTBL(x, a, b) REP(i, a) REP(j, b) cout << #x << '[' << i << "][" << j << "] = " << x[i][j] << endl;

#define FIN "test.in"
#define FOUT "test.out"

int x[3], y[3], r[3];

double rr(int i, int j) {
  return 0.5 * sqrt((double)(x[i] - x[j]) * (x[i] - x[j]) + (double)(y[i] - y[j]) * (y[i] - y[j])) + 0.5 * (r[i] + r[j]);
}

int main()
{
  freopen(FIN, "r", stdin);
  freopen(FOUT, "w", stdout);

  int T;
  cin >> T;
  REP(zzz, T) {
    int N;
    cin >> N;
    REP(i, N) cin >> x[i] >> y[i] >> r[i];
    double res;
    if (N == 1) {
      res = r[0];
    } else if (N == 2) {
      res = max(r[0], r[1]);
    } else {
      double r0 = rr(0, 1);
      r0 = max(r0, (double)r[2]);
      double r1 = rr(0, 2);
      r1 = max(r1, (double)r[1]);
      double r2 = rr(1, 2);
      r2 = max(r2, (double)r[0]);
      res = min(r0, min(r1, r2));
    }
    printf("Case #%d: %.8f\n", zzz + 1, res);
  }


  fclose(stdin);
  fflush(stdout);
  fclose(stdout);
  return 0;
}
