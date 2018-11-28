# include <stdio.h>
# include <string.h>
# define INF 500000
# define min(x, y) (((x) < (y))? (x) : (y))

int a[1005][105];

char engine[105][105], query[1005][105];

int main()
{
	int cases, s, q, i, j, t;
	t = 0;
//	freopen("D:\\A-large.in", "r", stdin);
//	freopen("D:\\A-large.out", "w", stdout);
	scanf("%d", &cases);
	while (cases--)
	{
		scanf("%d", &s);
		gets(engine[0]);
		for (i = 0; i < s; i++) gets(engine[i]);
		scanf("%d", &q);
		gets(query[0]);
		for (i = 0; i < q; i++) gets(query[i]);
		if (!q)
		{
			printf("Case #%d: 0\n", ++t);
			continue;
		}
		for (i = 0; i < q; i++)
			for (j = 0; j < s; j++)
				a[i][j] = INF;
		for (i = 0; i < s; i++)
			if (strcmp(engine[i], query[0]))
				a[0][i] = 0;
		int min1, min2, temp, t1, t2;
		min1 = 0;
		if (s == 2) min2 = INF;
		else min2 = 0;
		for (i = 1; i < q; i++)
		{
			t1 = t2 = INF;
			for (j = 0; j < s; j++)
				if (strcmp(engine[j], query[i]))
				{
					if (a[i-1][j] == min1) temp = min2;
					else temp = min1;
					a[i][j] = min(a[i-1][j], temp + 1);
					if (a[i][j] < t1)
					{
						t2 = t1;
						t1 = a[i][j];
					}
					else if (a[i][j] < t2) t2 = a[i][j];
				}
				else a[i][j] = INF;
			min1 = t1; min2 = t2;
		}
		int ans = INF;
		for (i = 0; i < s; i++)
			if (ans > a[q-1][i])
				ans = a[q-1][i];
		printf("Case #%d: %d\n", ++t, ans);
	}
}