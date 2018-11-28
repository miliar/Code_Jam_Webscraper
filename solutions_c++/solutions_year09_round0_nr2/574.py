#include <cstdio>
#include <cstring>

const int NMAX = 105;
const int dx[] = {0, -1, 0, 0, 1};
const int dy[] = {0, 0, -1, 1, 0};

int a[NMAX][NMAX];
char u[NMAX][NMAX];
int h, w, t;
char col;

char Dfs(int x, int y)
{
	if (u[x][y] == 0)
	{
		int md = 0;
		for (int dir = 1; dir <= 4; dir++)
			if (a[x + dx[dir]][y + dy[dir]] < a[x + dx[md]][y + dy[md]])
				md = dir;

		if (md == 0)
		{
			u[x][y] = col;
			col++;
		}
		else
			u[x][y] = Dfs(x + dx[md], y + dy[md]);
	}

	return u[x][y];
}

void Solve()
{
	scanf("%d%d", &h, &w);
	for (int i = 0; i <= h + 1; i++)
		for (int j = 0; j <= w + 1; j++)
			a[i][j] = 20000;

	for (int i = 1; i <= h; i++)
		for (int j = 1; j <= w; j++)
			scanf("%d", &a[i][j]);

	memset(u, 0, sizeof(u));

	col = 'a';
	for (int i = 1; i <= h; i++)
		for (int j = 1; j <= w; j++)
			Dfs(i, j);

	for (int i = 1; i <= h; i++)
	{
		for (int j = 1; j <= w; j++)
			printf("%c ", u[i][j]);
		printf("\n");
	}
}

int main()
{
	freopen("watersheds.in", "r", stdin);
	freopen("watersheds.out", "w", stdout);

	scanf("%d", &t);
	for (int tnum = 1; tnum <= t; tnum++)
	{
		printf("Case #%d:\n", tnum);
		Solve();
	}

	return 0;
}
