#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <string>
#include <set>
#include <queue>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)n; ++i)


const int INF = 1000000000;

int n, m;
int a[200][200];
int dirX[200][200];
int dirY[200][200];
int used[200][200];
bool us[30];
int ans[30];

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

void getDir(int x, int y)
{
	int ansX = -1, ansY = -1;
	int mi = a[x][y];
	forn(i, 4)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (nx < 0 || nx >= n || ny < 0 || ny >= m)
			continue;

		if (a[nx][ny] < mi)
		{
			mi = a[nx][ny];
			ansX = nx, ansY = ny;
		}
	}
	dirX[x][y] = ansX;
	dirY[x][y] = ansY;
}

void dfs(int x, int y, int color)
{
	used[x][y] = color;
	forn(i, 4)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (nx < 0 || nx >= n || ny < 0 || ny >= m || used[nx][ny])
			continue;

		if (dirX[nx][ny] == x && dirY[nx][ny] == y)
			dfs(nx, ny, color);

	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	forn(test, tests)
	{
		memset(used, 0, sizeof(used));
		scanf("%d%d", &n, &m);
		forn(i, n)
			forn(j, m)
				scanf("%d", &a[i][j]);

		int color = 0;
		forn(i, n)
			forn(j, m)
				getDir(i, j);

		forn(i, n)
			forn(j, m)
				if (dirX[i][j] == -1)
					dfs(i, j, ++color);

		memset(us, 0, sizeof us);
		color = 0;
		forn(i, n)
			forn(j, m)
			{
				if (us[used[i][j]])
					continue;
				ans[used[i][j]] = color++;
				us[used[i][j]] = true;
			}
				

		printf("Case #%d:\n", test + 1);
		forn(i, n)
		{
			forn(j, m)
				printf("%c ", ans[used[i][j]] + 'a');
			printf("\n");
		}




	}
	

	return 0;
}

