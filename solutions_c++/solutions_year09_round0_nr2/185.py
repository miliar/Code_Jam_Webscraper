#include <stdio.h>
#include <string.h>
#define INF 1 << 29
int gra[110][110][4];
char label[110][110];
int H, W;
int dir[4][2] = {-1, 0, 0, -1, 0, 1, 1, 0};
int ind[4] = {3, 2, 1, 0};
void dfs(int x, int y, char lcnt)
{
	if (label[x][y] != -1)
		return;
	label[x][y] = lcnt;
	for (int i = 0; i < 4; i++)
	{
		int nx = x + dir[i][0], ny = y + dir[i][1];
		if (gra[x][y][i])
			dfs(nx, ny, lcnt);
	}
}
int att[110][110];
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("ans.txt", "w", stdout);
	int N, i, j, k, d;
	scanf("%d", &N);
	for (i = 0; i < N; i++)
	{
		scanf("%d%d", &H, &W);
		for (j = 0; j < H; j++)
			for (k = 0; k < W; k++)
				for (d = 0; d < 4; d++)
					gra[j][k][d] = 0;
		for (j = 0; j < H; j++)
			for (k = 0; k < W; k++)
				scanf("%d", &att[j][k]);
		for (j = 0; j < H; j++)
			for (k = 0; k < W; k++)
			{
				int sx = -1, sy, sd, minA = INF;
				for (d = 0; d < 4; d++)
				{
					int nx = j + dir[d][0], ny = k + dir[d][1];
					if (nx >= 0 && nx < H && ny >= 0 && ny < W && minA > att[nx][ny] && att[nx][ny] < att[j][k])
					{
						minA = att[nx][ny];
						sd = d;
						sx = nx;
						sy = ny;
					}
				}
				if (sx != -1)
				{
					gra[j][k][sd] = 1;
					gra[sx][sy][3 - sd] = 1;
				}
			}
		memset(label, 0xff, sizeof(label));
		char lcnt = 'a';
		for (j = 0; j < H; j++)
			for (k = 0; k < W; k++)
				if (label[j][k] == -1)
				{
					dfs(j, k, lcnt);
					lcnt++;
				}
		printf("Case #%d:\n", i + 1);
		for (j = 0; j < H; j++)
			for (k = 0; k < W; k++)
				printf("%c%c", label[j][k], k == W - 1 ? '\n' : ' ');
	}
	return 0;
}
