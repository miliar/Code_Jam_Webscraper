#include <cstdio>
#include <cstring>

int dx[] = {-1, 0, 0, 1}, dy[] = {0, -1, 1, 0};

int h, w;
char map[120][120];
int edge[120][120], ha[120][120];
void dfs(int a, int b, char ch)
{
	if (map[a][b])
		return;
	map[a][b] = ch;
	if (edge[a][b] != -1)
	{
		int e = edge[a][b];
		dfs(a + dx[e], b + dy[e], ch);
	}

	for (int d = 0; d < 4; ++d)
	{
		int nx = a + dx[d], ny = b + dy[d];
		if (nx < 0 || ny < 0 || nx >= h || ny >= w)
			continue;
		if (edge[nx][ny] + d == 3)
		{
			dfs(nx, ny, ch);
		}
	}
}

void work()
{
	scanf("%d%d", &h, &w);
	for (int i = 0; i < h; ++i)
		for (int j = 0; j < w; ++j)
			scanf("%d", &ha[i][j]);
	memset(edge, -1, sizeof(edge));
	memset(map, 0, sizeof(map));
	for (int i = 0; i < h; ++i)
		for (int j = 0; j < w; ++j)
		{
			int cd = ha[i][j];
			for (int d = 0; d < 4; ++d)
			{
				int nx = i + dx[d], ny = j + dy[d];
				if (nx < 0 || ny < 0 || nx >= h || ny >= w)
					continue;
				if (ha[nx][ny] < cd)
				{
					cd = ha[nx][ny];
					edge[i][j] = d;
				}
			}
		}
	char letter = 'a';
	for (int i = 0; i < h; ++i)
		for (int j = 0; j < w; ++j)
		{
			if (!map[i][j])
			{
				dfs(i, j, letter++);
			}
		}
	for (int i = 0; i < h; ++i)
		for (int j = 0; j < w; ++j)
		{
			putchar(map[i][j]);
			if (j != w - 1)
				putchar(' ');
			else
				puts("");
		}
}

int main()
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		printf("Case #%d:\n", i + 1);
		work();
	}
}
