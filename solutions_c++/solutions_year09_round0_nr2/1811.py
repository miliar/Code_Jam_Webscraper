#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

#pragma comment(linker,"/STACK:10000000")

const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};

const int N = 200;
const int M = 200;

int n, m;
int a[N][M];

bool isMap(int x, int y)
{
	return 0 <= x && x < n && 0 <= y && y < m;
}

int color[N][M];

int dfs(int x, int y, int c)
{
	color[x][y] = c;
	int best = -1, bestH = a[x][y];
	for (int i = 0; i < 4; ++i)
		if (isMap(x + dx[i], y + dy[i]) && 
				a[x + dx[i]][y + dy[i]] < bestH)
		{
			best = i;
			bestH = a[x + dx[i]][y + dy[i]];
		}

	if (best == -1)
		return c;

	if (color[x + dx[best]][y + dy[best]] > c)
		return dfs(x + dx[best], y + dy[best], c);
	else
		return color[x + dx[best]][y + dy[best]];
}

int main()
{
	int tt;
	scanf("%d", &tt);
	for (int ii = 1; ii <= tt; ++ii)
	{
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
			{
				scanf("%d", &a[i][j]);
				color[i][j] = 26;
			}

		int cnt = 0;

		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
			{
				if (color[i][j] != 26)
					continue;
				int p = dfs(i, j, cnt);
//				printf("%d\n", p);
				if (p != cnt)
					dfs(i, j, p);
				else
					++cnt;
			}

		printf("Case #%d:\n", ii);
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
				printf("%c ", color[i][j] + 'a');
			printf("\n");
		}
	}

	return 0;
}