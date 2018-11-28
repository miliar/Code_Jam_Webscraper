#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN = 12000;

int mark[MAXN], vis[MAXN];
int num[MAXN],ans, num2[MAXN];
int dp[120][120];

int calc(int n){
	memset(dp, 0x3f, sizeof(dp));
	for(int i = 0; i <= n+1; ++i){
		dp[i][i] = dp[i][i+1] = 0;
	}
	for(int k = 2; k <= n; ++k){
		for(int i = 0; i +k <= n; ++i)
			for(int j = i+1; j < (i+k); ++j)
				dp[i][i+k] = min(dp[i][i+k], dp[i][j]+dp[j][i+k]+num[j]-num[i]+num[i+k]-num[j]-2);
	}
	return dp[0][n];
}
int main()
{
	int m, T, q, p, a;
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t){
		scanf("%d %d", &p, &q);
		num[0] = 0;
		for(int i = 1; i <= q; ++i){
			scanf("%d", &a);
			num[i] = a;
		}
		num[q+1] = p+1;
		ans = 0;
		if(q == 1){
			ans = p-1;
		}else {
			ans = calc(q+1);
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}


