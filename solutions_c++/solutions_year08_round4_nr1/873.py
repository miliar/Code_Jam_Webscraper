#include <stdio.h>

const int N = 10010;
const int MAXINT = 1000000000;

#define Min(a, b) ((a)<(b)?(a):(b))

#define AND 1
#define OR 0

int n, rr;
int v[N], c[N];
int dp[N][2][2];

void dfs(int x) {
	int i, j , k;
	if(c[x] == -1) {
		for(i = 0; i < 2; ++i) {
			dp[x][i][v[x]] = 0;
			dp[x][i][1-v[x]] = MAXINT;
		}
		return;
	}
	dfs(x*2);
	dfs(x*2+1);
	for(j = 0; j < 2; ++j) {
		for(k = 0; k < 2; ++k) {
			dp[x][AND][0] = Min(dp[x][AND][0], dp[2*x][j][0] + dp[2*x+1][k][1]);
			dp[x][AND][0] = Min(dp[x][AND][0], dp[2*x][j][1] + dp[2*x+1][k][0]);
			dp[x][AND][0] = Min(dp[x][AND][0], dp[2*x][j][0] + dp[2*x+1][k][0]);
			dp[x][AND][1] = Min(dp[x][AND][1], dp[2*x][j][1] + dp[2*x+1][k][1]);
			dp[x][OR][1] = Min(dp[x][OR][1], dp[2*x][j][1] + dp[2*x+1][k][1]);
			dp[x][OR][1] = Min(dp[x][OR][1], dp[2*x][j][0] + dp[2*x+1][k][1]);
			dp[x][OR][1] = Min(dp[x][OR][1], dp[2*x][j][1] + dp[2*x+1][k][0]);
			dp[x][OR][0] = Min(dp[x][OR][0], dp[2*x][j][0] + dp[2*x+1][k][0]);

		}
	}
	if(v[x] != AND) dp[x][AND][0]++, dp[x][AND][1]++;
	if(v[x] != OR) dp[x][OR][0]++, dp[x][OR][1]++;
	for(i = 0; i < 2; ++i) {
		for(j = 0; j < 2; ++j) {
			dp[x][i][j] = Min(dp[x][i][j], MAXINT);
		}
	}
	if(c[x] != 1) {
		for(j = 0; j < 2; ++j)
			dp[x][1-v[x]][j] = MAXINT;
	}
//	
//	for(i = 0; i < 2; ++i) {
//		for(j = 0; j < 2; ++j)
//			printf("dp[%d][%d][%d] = %d\n", x, i, j, dp[x][i][j]);
//	}
}

int main()
{
	freopen("A-large(2).in", "r", stdin);
	freopen("A-large.txt", "w", stdout);

	int ntc, i, j, tc = 0;
	scanf("%d", &ntc);
	while(ntc--) {
		printf("Case #%d: ", ++tc);
		scanf("%d%d", &n, &rr);
		for(i = 1; i <= (n-1)/2; ++i) {
			scanf("%d %d", v+i, c+i);
		}
		for(; i <= n; ++i) {
			scanf("%d", &v[i]);
			c[i] = -1;
		}
		for(i = 1; i <= n; ++i) 
			dp[i][0][0] = dp[i][0][1] = dp[i][1][0] = dp[i][1][1] = MAXINT;
		dfs(1);
		int ans = Min(dp[1][AND][rr], dp[1][OR][rr]);
		if(ans == MAXINT) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
	return 0;
}
