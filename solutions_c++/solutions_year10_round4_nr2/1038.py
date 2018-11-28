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

// #define INF 1000000000
#define INF 10000

int m[1030];
int dp[1030][1030][11];
int p[1030];

int pw;

int doit(int node, int t, int missed);
int P;

int f(int node, int t, int missed) {
  if (node >= pw) {
    node -= pw;
    //    DBG(node); DBG(t); DBGN(m[node]);
    if (missed > m[node])
      return INF;
    return 0;
  }
  if (dp[node][t][missed] == -1) {
    int res = doit(node, t, missed);
    dp[node][t][missed] = res;
    //    DBG(node); DBG(t); DBGN(res);
  }
  return dp[node][t][missed];
}

int doit(int node, int t, int missed) {
  int l = node * 2;
  int r = l + 1;
  int nobuy = max(f(l, t, missed + 1) + f(r, 0, missed + 1),
                  f(l, 0, missed + 1) + f(r, t, missed + 1));
  int buy = max(f(l, t + 1, missed) + f(r, 1, missed),
                f(l, 1, missed) + f(r, t + 1, missed));
  return min(nobuy, p[node] + buy);
}

int main()
{
  freopen(FIN, "r", stdin);
  freopen(FOUT, "w", stdout);

  int tests;
  cin >> tests;
  REP(z, tests) {
    cin >> P;
    pw = 1 << P;
    REP(i, pw) cin >> m[i];
    int cnt = pw / 2;
    while (cnt >= 1) {
      FOR(i, cnt, 2 * cnt - 1) {
        cin >> p[i];
      }
      cnt /= 2;
    }
    memset(dp, -1, sizeof(dp));
    cout << "Case #" << z + 1 << ": " << f(1, 0, 0) << endl;
  }

  fclose(stdin);
  fflush(stdout);
  fclose(stdout);
  return 0;
}
