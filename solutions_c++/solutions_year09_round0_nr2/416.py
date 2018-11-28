#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define MAXN 105
#define INF 1000000000
int test, n, m, a[MAXN][MAXN], c[MAXN][MAXN], ch, mark;
void dfs(int i, int j)
{
	int ok = 0;
	int t = min(a[i][j] - 1, min(a[i - 1][j], min(a[i + 1][j], min(a[i][j - 1], a[i][j + 1]))));
	if (!ok && a[i - 1][j] == t)
	{
		ok = 1;
		if (!c[i - 1][j]) dfs(i - 1, j);
		else mark = c[i - 1][j];
	}
	if (!ok && a[i][j - 1] == t)
	{
		ok = 1;
		if (!c[i][j - 1]) dfs(i, j - 1);
		else mark = c[i][j - 1];
	}
	if (!ok && a[i][j + 1] == t)
	{
		ok = 1;
		if (!c[i][j + 1]) dfs(i, j + 1);
		else mark = c[i][j + 1];
	}
	if (!ok && a[i + 1][j] == t)
	{
		ok = 1;
		if (!c[i + 1][j]) dfs(i + 1, j);
		else mark = c[i + 1][j];
	}
	if (!ok) mark = ch++;
	c[i][j] = mark;
}
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++)
	{
		scanf("%d%d", &n, &m);
		for (int i = 0; i <= n + 1; i++) a[i][0] = a[i][m + 1] = INF;
		for (int i = 0; i <= m + 1; i++) a[0][i] = a[n + 1][i] = INF;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				scanf("%d", &a[i][j]);
		memset(c, 0, sizeof(c)); ch = 'a';
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				if (!c[i][j]) dfs(i, j);
		printf("Case #%d:\n", tt);
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j < m; j++) putchar(c[i][j]), putchar(' ');
			printf("%c\n", c[i][m]);
		}
	}
	fclose(stdin); fclose(stdout);
	return 0;
}