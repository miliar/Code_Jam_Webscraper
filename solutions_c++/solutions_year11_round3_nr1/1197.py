#include <stdio.h>
#include <string.h>

char map[55][55];
int r, c;

void cover(const int &i, const int &j)
{
	map[i][j] = '/';
	map[i][j + 1] = '\\';
	map[i + 1][j] = '\\';
	map[i + 1][j + 1] = '/';
}

void dfs(const int &a, const int &b)
{
	if (a < 0 || a >= r || b < 0 || b >= c)
		return;
	if (map[a][b + 1] == '#' && map[a + 1][b] == '#' && map[a + 1][b + 1] == '#')
		cover(a, b);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		scanf("%d %d", &r, &c);
		memset(map, 0, sizeof (map));
		for (int j = 0; j < r; ++j)
			scanf("%s", map[j]);
		for (int j = 0; j < r; ++j)
		{
			for (int k = 0; k < c; ++k)
			{
				if (map[j][k] == '#')
				{
					dfs(j, k);
				}
			}
		}
		bool impossible = false;
		for (int j = 0; j < r; ++j)
		{
			for (int k = 0; k < c; ++k)
			{
				if (map[j][k] == '#')
				{
					printf("Case #%d:\nImpossible\n", i);
					impossible = true;
					break;
				}
			}
			if (impossible == true)
				break;
		}
		if (impossible == false)
		{
			printf("Case #%d:\n", i);
			for (int j = 0; j < r; ++j)
				printf("%s\n", map[j]);
		}
	}
	return 0;
}