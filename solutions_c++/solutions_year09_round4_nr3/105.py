
	#include <cstdlib>
	#include <cstdio>
	#include <algorithm>

	using namespace std;

	int n, k;
	int v[200][200], visit[200], match[200], graph[200][200];

	int can(int a, int b)
	{
		for (int i = 0; i < k; i ++)
			if (v[a][i] >= v[b][i])
				return 0;
		return 1;
	}

	int dfs(int p)
	{
		for (int i = 0; i < n; i ++)
		{
			if(graph[i][p] == 1 && visit[i] == -1)
			{
				visit[i] = 1;
				if (match[i] == -1 || dfs(match[i]))
				{
					match[i] = p;
					return 1;
				}
			}
		}
		return 0;
	}

	int work()
	{
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; i ++)
			for (int j = 0; j < k; j ++)
				scanf("%d", &v[i][j]);
		for (int i = 0; i < n; i ++)
			for (int j = 0; j < n; j ++)
				graph[i][j] = can(i, j);
		int ans = 0;
		memset(match, -1, sizeof(match));
		for (int i = 0; i < n; i ++)
		{
			memset(visit, -1, sizeof(visit));
			if (dfs(i)) 
				ans++;
		}
		return n - ans;
	}

	int main()
	{
		freopen("c.in", "r", stdin);
		freopen("c.out", "w", stdout);
		int t;
		scanf("%d", &t);
		for (int i = 1; i <= t; i ++)
			printf("Case #%d: %d\n", i, work());
		return 0;
	}
