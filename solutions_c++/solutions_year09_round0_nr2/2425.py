#include <iostream>
using namespace std;

const int MAXN = 100;

//N W E S
const int dx[4] = {-1,0,0,1};
const int dy[4] = {0,-1,1,0};
const int INF = 1000000;

int h, w;
int height[MAXN+2][MAXN+2];

bool linked[MAXN+2][MAXN+2][MAXN+2][MAXN+2];
char grid[MAXN+2][MAXN+2];

void dfs(int x, int y, char letter)
{
	if (x <= 0 || x > h) return;
	if (y <= 0 || y > w) return;

	if (grid[x][y] != '.')
		return;

	grid[x][y] = letter;
	for (int a=0; a<4; a++)
		if (linked[x][y][x+dx[a]][y+dy[a]])
			dfs(x+dx[a], y+dy[a], letter);
}

void work()
{
	memset(linked, false, sizeof linked);
	for (int x=1; x<=h; x++)
		for (int y=1; y<=w; y++)
		{
			//find where water flows
			int least = height[x][y], where = -1;
			for (int a=0; a<4; a++)
				if (height[x+dx[a]][y+dy[a]] < least)
					least = height[x+dx[a]][y+dy[a]], where = a;

			if (where != -1)
			{
				linked[x][y][x+dx[where]][y+dy[where]] = true;
				linked[x+dx[where]][y+dy[where]][x][y] = true;
			}
		}
/*
	for (int a=1; a<=h; a++)
		for (int b=1; b<=w; b++)
		{
			for (int c=1; c<=h; c++)
				for (int d=1; d<=w; d++)
					if (linked[a][b][c][d])
						printf("%d %d and %d %d are linked\n", a, b, c, d);
			puts("");
		}
*/

	memset(grid, '.', sizeof grid);
	char letter = 'a';
	for (int a=1; a<=h; a++)
		for (int b=1; b<=w; b++)
			if (grid[a][b] == '.')
			{
				dfs(a, b, letter);
				letter++;
			}

	for (int a=1; a<=h; a++)
	{
		cout << grid[a][1];
		for (int b=2; b<=w; b++)
			cout << " " << grid[a][b];
		puts("");
	}

}

int main()
{
	freopen("lol.in", "r", stdin);
	freopen("watershed.out", "w", stdout);

	int t; cin >> t;
	for (int T=0; T<t; T++)
	{
		memset(height, 0x3f, sizeof height);
		scanf("%d %d", &h, &w);

		for (int x=1; x<=h; x++)
			for (int y=1; y<=w; y++)
				scanf("%d", &height[x][y]);

		printf("Case #%d:\n", T+1);
		work();
	}

}
