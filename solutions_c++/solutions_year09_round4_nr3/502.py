#include <stdio.h>

int t, n, kk;
int prices[100][25];
int g[100][100];

int best;
int num[100];
//int x[maxn];   // 取决于是否需要最优解.若需要，还要增加一个path[maxn]数组

bool dfs(int *adj, int total, int cnt)
{
	int i, j, k;
	int t[100];

	if (total==0)
	{
		if (best < cnt)
		{
			//for (i=0; i<cnt; i++) path[i] = x[i]; //路径信息2
			best = cnt;
			return true;
		}
		return false;
	}


	for (i=0; i<total; i++)
	{
		if (cnt+(total-i) <= best) return false;
		if (cnt+num[adj[i]]<=best) return false;

		//x[cnt]=adj[i]; //路径信息3
		for (k=0,j=i+1; j<total; j++) if (g[adj[i]][adj[j]]) t[k++] = adj[j];

		if ( dfs(t, k, cnt+1) ) return true;
	}

	return false;
}

int MaximumClique()
{
	int i, j, k;
	int adj[100];

	if (n<=0) return 0;

	best = 0;
	for (i=n-1; i>=0; i--)
	{
		//x[0] = i; 路径信息1
		for (k=0,j=i+1; j<n; j++) if ( g[i][j] ) adj[k++] = j;
		dfs(adj, k, 1);
		num[i] = best;
	}

	return best;
}

bool cross(int i, int j)
{
	for (int m = 1; m < kk; m++)
	{
		if ((long long)(prices[i][m] - prices[j][m]) * (long long)(prices[i][m-1] - prices[j][m-1]) <= 0)
		{
			return true;
		}
	}
	return false;
}

int main()
{
	scanf("%d", &t);
	for (int t1 = 0; t1 < t; t1++)
	{
		scanf("%d %d", &n, &kk);
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < kk; j++)
			{
				scanf("%d", &prices[i][j]);
			}
		}
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < i; j++)
			{
				if (!cross(i, j))
				{
					g[i][j] = g[j][i] = 0;
				}
				else
				{
					g[i][j] = g[j][i] = 1;
				}
			}
		}
		printf("Case #%d: %d\n", t1+1, MaximumClique());
	}
}
