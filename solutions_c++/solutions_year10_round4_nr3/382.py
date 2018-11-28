#include <stdio.h>
#include <string>
#include <algorithm>
#define maxn 128
using namespace std;

int C, c = 1;
int r;
bool grid[maxn][maxn], tmpgrid[maxn][maxn];
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	for(scanf("%d", &C); C; --C)
	{
		int x1, y1, x2, y2;

		scanf("%d", &r);

		memset(grid, 0, sizeof(grid));
		for(int i = 0; i < r; ++i)
		{
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);

			for(int u = x1; u <= x2; ++u)
				for(int v = y1; v <= y2; ++v)
					grid[u][v] = 1;
		}

		int t = 1;

		while(1)
		{
			bool die = true;
			memset(tmpgrid, 0, sizeof(tmpgrid));

			for(int i = 100; i > 0; --i)
				for(int j = 100; j > 0; --j)
				{
					if(!grid[i][j])
					{
						if(grid[i - 1][j] && grid[i][j - 1])
						{
							tmpgrid[i][j] = 1;
							die = false;
						}
						else
							tmpgrid[i][j] = 0;
					}else
					{
						if(!grid[i - 1][j] && !grid[i][j - 1])
							tmpgrid[i][j] = 0;
						else
						{
							tmpgrid[i][j] = 1;
							die = false;
						}
					}
				}
			if(die)
				break;
			memcpy(grid, tmpgrid, sizeof(grid));
			++t;
		}
		printf("Case #%d: %d\n", c++, t);
	}
}