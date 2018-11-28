#include <iostream>
#include <queue>
#include <cmath>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;
#define INF 1000000
#define MAXN 10000
#define AND 1
#define OR 0
int n, V, gate[MAXN+1], changeable[MAXN+1], val[MAXN+1], dp[MAXN+1][2];
inline int eval(int t, int x, int y) {
  if (t == AND)
    return x&&y;
  else
    return x||y;
}
int go(int x, int v) {
  if (2*x > n)
    return (val[x] == v) ? 0 : INF;
  int &ret = dp[x][v];
  if (ret != -1)
    return ret;
  ret = INF;
  for (int t = 0; t <= 1; ++t) {
    if ((t!=gate[x]) && !changeable[x])
      continue;
    for (int c1 = 0; c1 <= 1; ++c1)
      for (int c2 = 0; c2 <= 1; ++c2)
	if (eval(t, c1, c2) == v)
	  ret <?= go(2*x, c1) + go(2*x+1, c2) + (t!=gate[x]);
  }
  return ret;
}
int main() {
  int no_cases;
  cin >> no_cases;
  for (int rr = 1; rr <= no_cases; ++rr) {    
    cin >> n >> V;
    memset(changeable, 0, sizeof(changeable));
    memset(dp, -1, sizeof(dp));
    for (int i = 1; i <= n; ++i) {
      if (i <= (n-1) / 2) {
	cin >> gate[i] >> changeable[i];
      } else
	cin >> val[i];
    }
    int ans = go(1, V);
    if (ans >= INF)
      printf("Case #%d: IMPOSSIBLE\n", rr);
    else
      printf("Case #%d: %d\n", rr, ans);
  }
  return 0;
}
