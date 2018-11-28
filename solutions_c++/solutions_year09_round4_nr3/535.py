#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <assert.h>
using namespace std;
#define MAXN 42
int n, k, p[100][25], dp[1<<16];
char conf[100][100], ok[1<<16];
int go(int mask) {
  if (!mask)
    return 0;
  int &ret = dp[mask];
  if (ret != -1)
    return ret;
  ret = 1000000;
  for (int m = mask; m > 0; m = (m-1) & mask)
    if (ok[m])
      ret = min(ret, 1 + go(mask^m));
  return ret;
}
int main() {
  int T;
  cin >> T;
  for (int rr = 1; rr <= T; ++rr) {
    memset(conf, 0, sizeof(conf));
    cin >> n >> k;
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < k; ++j)
	cin >> p[i][j];
    for (int i = 0; i < n; ++i)
      for (int j = i + 1; j < n; ++j)
	for (int r = 0; r < k; ++r) {
	  if (p[i][r] == p[j][r]) {
	    conf[i][j] = 1;
	    break;
	  }
	  if (r+1 == k)
	    continue;
	  int a1 = p[i][r], a2 = p[i][r+1];
	  int b1 = p[j][r], b2 = p[j][r+1];
	  if ((a1<=b1 && a2>=b2) || (a1>=b1 && a2<=b2)) {
	    conf[i][j] = 1;
	    break;
	  }
	}
    memset(ok, 1, sizeof(ok));
    for (int m = 1; m < (1<<n); ++m) {
      for (int i = 0; i < n; ++i) 
	if (m&(1<<i))
	  for (int j = i + 1; j < n; ++j)
	    if (m&(1<<j))
	      if (conf[i][j]) {
		ok[m] = 0;
		goto done;
	      }
    done:
      ;
    }
    memset(dp, -1, sizeof(dp));
    printf("Case #%d: %d\n", rr, go((1<<n)-1));
  }
  return 0;
}
