#include <cstdio>
#include <memory.h>

const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};

int H, W, Tests, Count;
int Map[110][110], Set[110][110], Sink[110][110], Label[10010];

void Flow(int x, int y)
{
	int min, mink, fx = x, fy = y;
	while (1)
	{
		min = Map[x][y], mink = -1;
		for (int k = 0; k < 4; ++ k)
			if (x + dx[k] > 0 && y + dy[k] > 0 && x + dx[k] <= H && y + dy[k] <= W && Map[x + dx[k]][y + dy[k]] < min)
				min = Map[x + dx[k]][y + dy[k]], mink = k;
		if (mink == -1) break;
		x += dx[mink], y += dy[mink];
	}
	if (!Set[x][y]) Set[x][y] = ++ Count;
	Sink[fx][fy] = Set[x][y];
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &Tests);
	for (int Cases = 1; Cases <= Tests; ++ Cases)
	{
		scanf("%d %d", &H, &W);
		for (int i = 1; i <= H; ++ i)
			for (int j = 1; j <= W; ++ j)
				scanf("%d", &Map[i][j]);
		memset(Set, 0, sizeof(Set));
		memset(Sink, 0, sizeof(Sink));
		memset(Label, 0, sizeof(Label));
		Count = 0;
		for (int i = 1; i <= H; ++ i)
			for (int j = 1; j <= W; ++ j)
				Flow(i, j);
		Count = 0;
		printf("Case #%d:\n", Cases);
		for (int i = 1; i <= H; ++ i)
		{
			for (int j = 1; j < W; ++ j)
			{
				if (!Label[Sink[i][j]]) Label[Sink[i][j]] = ++ Count;
				printf("%c ", Label[Sink[i][j]] + 'a' - 1);
			}
			if (!Label[Sink[i][W]]) Label[Sink[i][W]] = ++ Count;
				printf("%c\n", Label[Sink[i][W]] + 'a' - 1);
		}
	}
}
