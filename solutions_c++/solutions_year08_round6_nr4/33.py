
	#include <cstdio>
	#include <cstdlib>
	#include <algorithm>

	int n, m, list[15][3], e[15][15], pos[15], used[15];

	int dfs(int steps)
	{
		if (steps == m + 1)
		{
			for (int i = 1; i < m; i ++)
				if (e[pos[list[i][1]]][pos[list[i][0]]] == 0)
					return 0;
			return 1;
		}
		for (int i = 1; i <= n; i ++)
			if (!used[i])
			{
				pos[steps] = i;
				used[i] = 1;
				if (dfs(steps + 1))	return 1;
				used[i] = 0;
			}
		return 0;
	}

	void work()
	{
		scanf("%d", &n);
		memset(e, 0, sizeof(e));
		for (int i = 1; i < n; i ++)
		{
			int p, q;
			scanf("%d %d", &p, &q);
			e[p][q] = 1;
			e[q][p] = 1;
		}
		scanf("%d", &m);
		for (int i = 1; i < m; i ++)
			scanf("%d%d", &list[i][0], &list[i][1]);
		memset(used, 0, sizeof(used));
		if (dfs(1))
			printf("YES\n");
		else
			printf("NO\n");
	}

	int main(int argc, char *argv[])
	{
		freopen("d.in", "r", stdin);
		freopen("d.out", "w", stdout);
		int c;
		scanf("%d", &c);
		for (int testnum = 1; testnum <= c; testnum ++)
		{
			printf("Case #%d: ", testnum);
			work();
		}
		return 0;
	}
