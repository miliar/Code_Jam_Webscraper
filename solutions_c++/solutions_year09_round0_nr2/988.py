#include <cstdio>
#include <cstring>

int t, tcs, h, w, map[105][105];
const int step[] = {-1, 0, 0, -1, 0, 1, 1, 0};
char color[105][105], ch;

void dfs(int x, int y)
{
	int k, nx, ny, mink = -1;
	
	for (k = 0; k < 8; k += 2)
	{
		if (map[x + step[k]][y + step[k + 1]] < map[x][y] &&
			(mink == -1 || map[x + step[k]][y + step[k + 1]] < map[x + step[mink]][y + step[mink + 1]]))
			mink = k;
	}
			
	if (mink == -1) {
		if (color[x][y] == '#')
			color[x][y] = ch++;
	} else {
		if (color[x + step[mink]][y + step[mink + 1]] == '#')
			dfs(x + step[mink], y + step[mink + 1]);
		color[x][y] = color[x + step[mink]][y + step[mink + 1]];
	}
}

int main()
{

	
	int i, j, k;
	
	scanf("%d", &t);
	for (tcs = 1; tcs <= t; ++tcs)
	{
		scanf("%d%d", &h, &w);
		for (i = 1; i <= h; ++i)
			for (j = 1; j <= w; ++j)
				scanf("%d", &map[i][j]);
		for (i = 1; i <= h; ++i)
			map[i][0] = map[i][w + 1] = 10005;
		for (j = 1; j <= w; ++j)
			map[0][j] = map[h + 1][j] = 10005;
		memset(color, '#', sizeof(color));
		ch = 'a';
		for (i = 1; i <= h; ++i)
			for (j = 1; j <= w; ++j)
				if (color[i][j] == '#')
					dfs(i, j);
		printf("Case #%d:\n", tcs);
		for (i = 1; i <= h; ++i)
		{
			printf("%c", color[i][1]);
			for (j = 2; j <= w; ++j)
				printf(" %c", color[i][j]);
			printf("\n");
		}
	}
	
	return 0;
}
