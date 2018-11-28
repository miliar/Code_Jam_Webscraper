#include<stdio.h>
#include<string.h>

const int maxn = 405;

int n, m, x, y;
int g[maxn][maxn];
int d0[maxn], d1[maxn], Q[maxn];

void bfs(int st, int d[maxn])
{
	memset(d, -1, sizeof(int) * maxn);
	int begin = 0 ,end = 0; d[st] = 0;
	Q[end++] = st;
	while(begin < end)
	{
		int x = Q[begin++];
		for(int i=0; i<n; i++)
			if(g[x][i] && d[i]==-1)
			{
				d[i] = d[x] + 1;
				Q[end++] = i;
			}
	}
}

int dp[maxn][maxn];

int dfs(int x, int y, int u)
{
	if(d1[y] == 1) return u;
//	if(dp[x][y] != -1) return dp[x][y];

	int & ans = dp[x][y];

	for(int i=0; i<n; i++)
		if(g[y][i] && d1[i] == d1[y] - 1)
		{
			int newu = u - 1;

			for(int j=0; j<n; j++)
				if(g[j][i] && !g[y][j] && !g[x][j])
					newu++;

			int p = dfs(y, i, newu);
			
			if(p > ans) ans = p;
		}

	return ans;
}

int main()
{
	freopen("D-small-attempt1.in","r",stdin);
	freopen("D-small-attempt1.out","w",stdout);
	int ntest;
	scanf("%d",&ntest);
	for(int test = 1; test <= ntest; test++)
	{
		memset(g, 0, sizeof(g));
		scanf("%d%d", &n, &m);
		for(int i=0; i<m; i++)
		{
			scanf("%d,%d", &x, &y);
			g[x][y] = g[y][x] = 1;
		}

		for(int i=0; i<n; i++) g[i][i] = 1;
		
		bfs(0, d0);
		bfs(1, d1);
		
		int u = 0;
		for(int i=0; i<n; i++)
			if(g[0][i]) u++;

		memset(dp, -1, sizeof(dp));
		int ans = dfs(0, 0, u-1);

		printf("Case #%d: %d %d\n", test, d1[0]-1, ans);
	}

	return 0;
}
