#include <iostream>
#include <cstdio>
#include <stack>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
using namespace std;
#define For(i,a,b) for (i = a; i != b; ++i)
#define Rep(i,n) For(i,0,n)
#define GI ({int t;scanf("%d",&t);t;})
#define set(a,c) memset(a,c,sizeof(a))
#define pb push_back
#define INF (int)1e8
int dp[100010][2];
int tree[10010];
int C[10010];
int m,N;
int main() {
  int t = GI, test, i, j;
  Rep(test, t) {
    N = GI;int des = GI;
    m = (N-1)/2;
    Rep(i,N) {
      dp[i][0] = dp[i][1] = INF;
    }
    Rep(i,m) {
      tree[i] = GI, C[i] = GI;
    }
    For(i, m, N) {
      tree[i] = GI;
      dp[i][tree[i]] = 0;
      dp[i][1-tree[i]] = INF;
    }
    //int x = memo(0,s);
    for (i = m-1; i>=0 ;i-- ) {
      if (tree[i] == 1) {
	dp[i][0] = min(dp[i*2+1][0],dp[i*2+2][0]);
	dp[i][1] = dp[i*2+1][1] + dp[i*2+2][1];
	if (C[i] == 1) {
	  dp[i][1] <?= min(dp[i*2+1][1],dp[i*2+2][1]) + 1;
	  dp[i][0] <?= dp[i*2+1][0] + dp[i*2+2][0] + 1;
	}
	continue;
      }
      dp[i][1] = min(dp[i*2+1][1],dp[i*2+2][1]);
      dp[i][0] = dp[i*2+1][0] + dp[i*2+2][0];
      if (C[i] == 1) {
	dp[i][0] <?= min(dp[i*2+1][0],dp[i*2+2][0]) + 1;
	dp[i][1] <?= dp[i*2+1][1] + dp[i*2+2][1] + 1;
      }
    }
    cout << "Case #" << test + 1 << ": ";
    if (dp[0][des] >= INF) {
      cout << "IMPOSSIBLE\n";
      continue;
    }
    cout << dp[0][des] << endl;
  }
}
