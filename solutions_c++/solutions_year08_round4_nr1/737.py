#include <iostream>
using namespace std;

const int MMAX = 11000;
const int INF = 20000;
int m,v,t;
int gates[MMAX], change[MMAX],dp[2][MMAX];

void dfs(int pos)
{
	int left,right;
	left = pos*2;
	right = pos*2 + 1;
	if (pos <= t)
	{
		dfs(left);
		dfs(right);
		if (gates[pos])
		{
			dp[1][pos] = dp[1][left] + dp[1][right];
			int tmp = min(dp[1][left]+dp[0][right], dp[0][left]+dp[1][right]);
			tmp = min(tmp, dp[0][left]+dp[0][right]);
			dp[0][pos] = tmp;

			if (change[pos] == 1)
			{
				tmp = min(dp[1][left]+dp[0][right], dp[0][left]+dp[1][right]);
				tmp = min(tmp, dp[1][left] + dp[1][right]);
				dp[1][pos] = min(dp[1][pos], tmp+1);
				dp[0][pos] = min(dp[0][pos], dp[0][left]+dp[0][right]+1);
			}
		}
		else
		{
			int tmp = min(dp[1][left]+dp[0][right], dp[0][left]+dp[1][right]);
			tmp = min(tmp, dp[1][left] + dp[1][right]);
			dp[1][pos] = tmp;
			dp[0][pos] = dp[0][left] + dp[0][right];

			if (change[pos] == 1)
			{
				dp[1][pos] = min(dp[1][pos], dp[1][left]+dp[1][right]+1);
				tmp = min(dp[1][left]+dp[0][right], dp[0][left]+dp[1][right]);
				tmp = min(tmp, dp[0][left]+dp[0][right]);
				dp[0][pos] = min(dp[0][pos], tmp+1);
			}
		}
	}
	else
	{
		dp[gates[pos]][pos] = 0;
		dp[1-gates[pos]][pos] = INF;
	}

	dp[0][pos] = min(dp[0][pos], INF);
	dp[1][pos] = min(dp[1][pos], INF);
}

int solve()
{
	int i, j;
	memset(dp, 0, sizeof(dp));
	dfs(1);
	if (dp[v][1] >= INF)	return -1;
	return dp[v][1];
}

int main()
{
	int nca,ca,i,j,ans;
	freopen("A-large.in", "r", stdin);
	freopen("12.out", "w", stdout);
	scanf("%d",&nca);
	for (ca=1; ca<=nca; ca++)
	{
		scanf("%d%d",&m,&v);
		t = m/2;
		for (i=1; i<=t; i++)
			scanf("%d%d",&gates[i],&change[i]);
		for (; i<=m; i++)
			scanf("%d",&gates[i]);
		ans = solve();
		printf("Case #%d: ",ca);
		if (ans == -1)	printf("IMPOSSIBLE\n");
		else	printf("%d\n",ans);
	}
}