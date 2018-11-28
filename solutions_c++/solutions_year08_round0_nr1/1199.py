
	#include <cstdio>
	#include <stdlib.h>
	#include <algorithm>
	using namespace std;

	int tests;
	int n, m, leng[105], len, list[1005], ans[1005][105], ggg;
	char st[105][105];

	void work()
	{
		scanf("%d", &n);
		getchar();
		for (int i = 1; i <= n; i ++)
		{
			leng[i] = 0;
			char c = getchar();
			while (c != '\n')
			{
				leng[i] ++;
				st[i][leng[i]] = c;
				c = getchar();
			}
		}
		/*for (int i = 1; i <= n; i ++)
		{
			for (int j = 1; j <= leng[i]; j ++)
				putchar(st[i][j]);
			putchar('\n');
		}*/
		scanf("%d", &m);
		char c = getchar();
		for (int i = 1; i <= m; i ++)
		{
			len = 0;
			char c = getchar();
			while (c != '\n')
			{
				len ++;
				st[0][len] = c;
				c = getchar();
			}
			int j;
			for (j = 1; j <= n; j ++)
			{
				if (len != leng[j])	continue;
				int k = 1;
				while (k <= len && st[j][k] == st[0][k])	k ++;
				if (k == len + 1)
					break;
			}
			list[i] = j;
			//printf("%d ", j);
		}
		//printf("\n");
		memset(ans, 0, sizeof(ans));
		ggg = 5000;
		for (int i = 1; i <= m; i ++)
			for (int j = 1; j <= n; j ++)
			{
				ans[i][j] = 5000;
				if (j != list[i])
					for (int k = 1; k <= n; k ++)
						if (k == j)
							ans[i][j] <?= ans[i - 1][k];
						else
							ans[i][j] <?= ans[i - 1][k] + 1;
				if (i == m)
					ggg <?= ans[i][j];
			}
		if (m == 0)
			ggg = 0;
	}

	int main()
	{
		freopen("A-large.in", "r", stdin);
		freopen("s.out", "w", stdout);
		scanf("%d", &tests);
		//printf("%d\n", tests);
		for (int i = 1; i <= tests; i ++)
		{
			printf("Case #%d: ", i);
			work();
			printf("%d\n", ggg);
		}
		return 0;
	}
