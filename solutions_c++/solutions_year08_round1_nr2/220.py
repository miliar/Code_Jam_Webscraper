
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
/*

*/
int res, b[20], best[20], cur;
int e[200][20][2], n, m;

int ok()
{
for (int i = 1; i <= m; i ++)
{
	int p = 0;
	for (int j = 1; j <= n; j ++)
		for (int k = 0; k <= 1; k ++)
			if (b[j] == k && e[i][j][k])
				p = 1;
	if (p == 0)	return 0;
}
cur = 0;
for (int i = 1; i <= n; i ++)
	cur = cur + b[i];
return 1;
}

void work()
{
scanf("%d%d", &n, &m);
memset(b, 0, sizeof(b));
memset(e, 0, sizeof(e));
res = -1;
for (int i = 1; i <= m; i ++)
{
	int k;
	scanf("%d", &k);
	for (int j = 1; j <= k; j ++)
	{
		int x, y;
		scanf("%d%d", &x, &y);
		e[i][x][y] = 1;
	}
}
for (; b[n + 1] != 1;)
{
	if (ok())
		if (res == -1 || cur < res)
		{
			for (int i = 1; i <= n; i ++)
				best[i] = b[i];
			res = cur;
		}
	int i = 1;
	for (; b[i] == 1; i ++)
		b[i] = 0;
	b[i] = 1;
}
if (res == -1)
	printf(" IMPOSSIBLE\n");
else
{
	for (int i = 1; i <= n; i ++)
		printf(" %d", best[i]);
	printf("\n");
}
}

int main()
{
freopen("B-small-attempt0.in", "r", stdin);
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
