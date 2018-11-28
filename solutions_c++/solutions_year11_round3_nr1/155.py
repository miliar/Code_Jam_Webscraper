#include <stdio.h>

static const int N = 60;
static const int M = 60;

char g[N][M];

int n, m;

bool Replace(int x, int y)
{
	if (x + 1 >= n)
		return false;
	if (y + 1 >= m)
		return false;

	if (g[x][y] != '#')
		return false;
	if (g[x + 1][y] != '#')
		return false;
	if (g[x][y + 1] != '#')
		return false;
	if (g[x + 1][y + 1] != '#')
		return false;

	g[x][y] = '/';
	g[x][y + 1] = '\\';
	g[x + 1][y] = '\\';
	g[x + 1][y + 1] = '/';
	return true;
}

int main()
{
	int total;
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);

	scanf("%d", &total);
	for (int test = 1; test <= total; ++test)
	{
		
		bool flag = true;
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			scanf("%s", g[i]);

		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
			{
				if (g[i][j] == '#')
				{
					if (!Replace(i, j))
					{
						flag = false;
						goto end;
					}
				}
			}

end:;
			printf("Case #%d:\n", test);
			
			if (flag)
			{
				for (int i = 0; i < n; ++i)
					printf("%s\n", g[i]);
			}
			else
			{
				printf("Impossible\n");
			}
	}
	return 0;
}