#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

int T, H, W;

const int maxn = 110;
const int dir[4][2] = { {-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int alt[maxn][maxn];
int label[maxn][maxn];

bool cango(int, int, int);

int main() 
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	scanf("%d", &T);

	for (int id = 1; id <= T; id++)
	{
		scanf("%d %d", &H, &W);

		for (int i = 0; i < H; i++)
		{
			for (int k = 0; k < W; k++)
			{
				scanf("%d", &alt[i][k]);
			}
		}

		memset(label, 255, sizeof label);
		
		int sign = 0;

		for (int sx = 0; sx < H; sx++)
		{
			for (int sy = 0; sy < W; sy++)
			{
				if (label[sx][sy] != -1) continue;

				queue< pair<int, int> > qu;				
				qu.push( make_pair(sx, sy));
				label[sx][sy] = sign++;

				while (!qu.empty())
				{
					int x = qu.front().first;
					int y = qu.front().second;
					qu.pop();

					for (int dr = 0; dr < 4; dr++)
					{
						int nx = x + dir[dr][0];
						int ny = y + dir[dr][1];

						if (nx < 0 || nx >= H || ny < 0 || ny >= W) continue;
						if (label[nx][ny] != -1) continue;

						if (!cango(x, y, dr)) continue;

						qu.push( make_pair(nx, ny));
						label[nx][ny] = label[sx][sy];
					}
				}
			}
		}

		printf("Case #%d:\n", id);

		for (int i = 0; i < H; i++)
		{
			for (int k = 0; k < W; k++)
			{
				if (k > 0) printf(" ");
				
				printf("%c", 'a' + label[i][k]);
				
				if (k + 1 == W) printf("\n");
			}
		}
	}

	return 0;
}

bool cango(int x, int y, int nowd)
{
	int dr = -1;
	int min = 100000000;

	for (int d = 0; d < 4; d++)
	{
		int nx = x + dir[d][0];
		int ny = y + dir[d][1];

		if (nx < 0 || nx >= H || ny < 0 || ny >= W) continue;

		if (dr == -1 || alt[nx][ny] < min)
		{
			dr = d;
			min = alt[nx][ny];
		}
	}

	if (min < alt[x][y] && nowd == dr) return true;

	
	int xx = x + dir[nowd][0];
	int yy = y + dir[nowd][1];

	dr = -1;
	min = 100000000;

	for (int d = 0; d < 4; d++)
	{
		int nx = xx + dir[d][0];
		int ny = yy + dir[d][1];

		if (nx < 0 || nx >= H || ny < 0 || ny >= W) continue;

		if (dr == -1 || alt[nx][ny] < min)
		{
			dr = d;
			min = alt[nx][ny];
		}
	}

	if (xx + dir[dr][0] != x || yy + dir[dr][1] != y) return false;
	if (min < alt[xx][yy]) return true;

	return false;
}
