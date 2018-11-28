#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

const int move[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int H, W;
int emap[101][101];
char mapmove[101][101];
char basins[101][101];
char label[30];

vector< pair<int, int> > sink;

void fill(int a, int b, int c)
{
	basins[a][b] = c;

	queue< pair<int, int> > que;
	que.push(pair<int, int>(a, b));

	while (!que.empty())
	{
		int x = que.front().first;
		int y = que.front().second;
		que.pop();

		for (int i = 0 ; i < 4 ; ++i)
		{
			int x2 = x + move[i][0];
			int y2 = y + move[i][1];

			if (x2 >= 0 && x2 < H && y2 >= 0 && y2 < W)
			{
				if (basins[x2][y2] == -1 && mapmove[x2][y2] != -1)
				{
					if (x2 + move[mapmove[x2][y2]][0] == x && y2 + move[mapmove[x2][y2]][1] == y)
					{
						basins[x2][y2] = c;
						que.push(pair<int, int>(x2, y2));
					}
				}
			}
		}
	}
}

void solve(void)
{
	sink.clear();

	for (int i = 0 ; i < H ; ++i)
	{
		for (int j = 0 ; j < W ; ++j)
		{
			mapmove[i][j] = -1;
			basins[i][j] = -1;
		}
	}

	for (int i = 0 ; i < H ; ++i)
	{
		for (int j = 0 ; j < W ; ++j)
		{
			int emin = 999999;
			for (int k = 0 ; k < 4 ; ++k)
			{
				int i2 = i + move[k][0];
				int j2 = j + move[k][1];

				if (i2 >= 0 && i2 < H && j2 >= 0 && j2 < W)
				{
					if (emap[i2][j2] < emap[i][j] && emap[i2][j2] < emin)
					{
						emin = emap[i2][j2];
						mapmove[i][j] = k;
					}
				}
			}
			if (mapmove[i][j] == -1)
			{
				sink.push_back(pair<int, int>(i, j));
			}
		}
	}

	if (sink.size() > 26) printf("!!!!!!!!!!\n");

	memset(label, 0xFF, 26);

	for (int i = 0 ; i < sink.size() ; ++i)
	{
		fill(sink[i].first, sink[i].second, i);
	}

	char now = 'a';
	for (int i = 0 ; i < H ; ++i)
	{
		for (int j = 0 ; j < W ; ++j)
		{
			if (label[basins[i][j]] == -1)
			{
				label[basins[i][j]] = now++;
			}
		}
	}
}

int main(void)
{
	int T;
	scanf("%d ", &T);

	for (int t = 1 ; t <= T ; ++t)
	{
		scanf("%d %d ", &H, &W);

		for (int i = 0 ; i < H ; ++i)
		{
			for (int j = 0 ; j < W ; ++j)
			{
				scanf("%d ", &emap[i][j]);
			}
		}

		solve();

		printf("Case #%d:\n", t);
		for (int i = 0 ; i < H ; ++i)
		{
			for (int j = 0 ; j < W ; ++j)
			{
				if (j) printf(" ");
				printf("%c", label[basins[i][j]]);
			}
			printf("\n");
		}
	}
}
