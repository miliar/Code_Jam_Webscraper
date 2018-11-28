
	#include <stdio.h>
	#include <stdlib.h>
	#include <memory.h>
	/*

	*/
	int e[2010][2010];
	int tot[2010], num[2010];
	int res[2010], n, m, list[2010];

	int can(int x)
	{
		for (int i = 1; i <= tot[x]; i ++)
			if (res[e[x][i]] == 0)
				return 1;
		return 0;
	}

	int find()
	{
		for (int i = 1; i <= m; i ++)
			if (res[list[i]] == 0 && !can(i))
				return i;
		return 0;
	}

	void work()
	{
		scanf("%d%d", &n, &m);
		memset(e, 0, sizeof(e));
		memset(list, 0, sizeof(list));
		for (int i = 1; i <= m; i ++)
		{
			scanf("%d", &num[i]);
			tot[i] = 0;
			for (int j = 1; j <= num[i]; j ++)
			{
				int x, y;
				scanf("%d%d", &x, &y);
				if (y == 1)
					list[i] = x;
				else
				{
					tot[i] ++;
					e[i][tot[i]] = x;
				}
			}
		}
		memset(res, 0, sizeof(res));
		for (;;)
		{
			int i = find();
			if (i == 0)
				break;
			if (list[i] == 0)
			{
				printf(" IMPOSSIBLE\n");
				return;
			}
			else
				res[list[i]] = 1;
		}
		for (int i = 1; i <= n; i ++)
			printf(" %d", res[i]);
		printf("\n");
	}

	int main()
	{
		freopen("b-large.in", "r", stdin);
		freopen("b.out", "w", stdout);
		int test;
		scanf("%d", &test);
		for (int i = 1; i <= test; i ++)
		{
			printf("Case #%d:", i);
			work();
		}
		return 0;
	}
