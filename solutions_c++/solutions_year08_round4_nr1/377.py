#include <stdio.h>
#include <string.h>
#include <algorithm>

#define mmax 10005
#define inf 0x3f3f3f3f

using namespace std;

int m, v, T;
int a[mmax], c[mmax][2];
int d[mmax];

void dfs(int x)
{
	if(x * 2 > m) c[x][a[x]] = 0, c[x][!a[x]] = inf;
	else
	{
		dfs(x * 2);
		dfs(x * 2 + 1);
		c[x][0] = c[x][1] = 100000;
		int cor = 1, cand = 1;
		if(d[x] == 0) cor = cand = 1000000;
		if(a[x] == 1) cand = 0;
		else cor = 0;

		c[x][0] = min(c[x][0], c[x * 2][0] + c[x * 2 + 1][0] + cor);
		c[x][0] = min(c[x][0], c[x * 2][0] + c[x * 2 + 1][0] + cand);
		c[x][0] = min(c[x][0], c[x * 2][0] + c[x * 2 + 1][1] + cand);
		c[x][0] = min(c[x][0], c[x * 2][1] + c[x * 2 + 1][0] + cand);

		c[x][1] = min(c[x][1], c[x * 2][0] + c[x * 2 + 1][1] + cor);
		c[x][1] = min(c[x][1], c[x * 2][1] + c[x * 2 + 1][0] + cor);
		c[x][1] = min(c[x][1], c[x * 2][1] + c[x * 2 + 1][1] + cor);
		c[x][1] = min(c[x][1], c[x * 2][1] + c[x * 2 + 1][1] + cand);
	}
}

int main()
{
	freopen("a.in", "r", stdin);

	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		scanf("%d%d", &m, &v);
		for(int i = 1; i <= (m - 1) / 2; i++) scanf("%d%d", &a[i], &d[i]);
		for(int i = (m - 1) / 2 + 1; i <= m; i++) scanf("%d", &a[i]);

		for(int i = 1; i <= m; i++)
			c[i][0] = c[i][1] = 1000000;
		dfs(1);
		if(c[1][v] >= 100000) printf("IMPOSSIBLE\n");
		else printf("%d\n", c[1][v]);
	}

	return 0;
}
