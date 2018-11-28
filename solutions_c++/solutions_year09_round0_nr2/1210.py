#include <stdio.h>
#include <string.h>

int H, W;
char M;
int tab[128][128];
char ret[128][128];

const int move[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

char mark(int i, int j)
{
	if (ret[i][j] != '\0') return ret[i][j];
	int dir = -1;
	int low = tab[i][j];
	for (int k = 0; k < 4; k++)
	{
		int ni = i + move[k][0];
		int nj = j + move[k][1];
		if (ni >= 0 && ni < H && nj >= 0 && nj < W && tab[ni][nj] < low)
		{
			low = tab[ni][nj];
			dir = k;
		}
	}
	if (dir == -1)
	{
		return ret[i][j] = M++;
	}
	else
	{
		return ret[i][j] = mark(i+move[dir][0], j+move[dir][1]);
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int n = 1; n <= T; n++)
	{
		scanf("%d%d", &H, &W);
		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W; j++)
			{
				scanf("%d", &tab[i][j]);
			}
		}
		memset(ret, 0, sizeof(ret));
		M = 'a';
		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W; j++)
			{
				mark(i, j);
			}
		}
		printf("Case #%d:\n", n);
		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W-1; j++)
			{
				putchar(ret[i][j]);
				putchar(' ');
			}
			putchar(ret[i][W-1]);
			putchar('\n');
		}
	}
	return 0;
}