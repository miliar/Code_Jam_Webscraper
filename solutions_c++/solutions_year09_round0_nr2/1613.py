#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int h, w, qc, m[102][102];
char c[102][102], cc[102][102];

void une(int x, int y, int px, int py)
{
	if (px > x)
	{
		c[x][y] = 'S';
		return;
	}
	if (px < x)
	{
		c[x][y] = 'N';
		return;
	}
	if (py < y)
	{
		c[x][y] = 'W';
		return;
	}
	c[x][y] = 'E';
}

void flow(int x, int y)
{
	int men = 20000, px, py;

	if (x < h - 1)
	{
		men = m[x + 1][y];
		px = x + 1;
		py = y;
	}
	if (y < w - 1)
	{
		if (m[x][y + 1] <= men)
		{
			men = m[x][y + 1];
			px = x;
			py = y + 1;
		}
	}
	if (y > 0)
	{
		if (m[x][y - 1] <= men)
		{
			men = m[x][y - 1];
			px = x;
			py = y - 1;
		}
	}
	if (x > 0)
	{
		if (m[x - 1][y] <= men)
		{
			men = m[x - 1][y];
			px = x - 1;
			py = y;
		}
	}

	if (men < m[x][y])
	{
		une(x, y, px, py);
	}
	else c[x][y] = 'F';
}

int fill(int x, int y)
{
	if (cc[x][y] != -1)
	{
		return cc[x][y] - 'a';
	}

	if (c[x][y] == 'F')
	{
		cc[x][y] = 'a' + qc++;
		return qc - 1;
	}

	if (c[x][y] == 'N')
	{
		cc[x][y] = 'a' + fill(x - 1, y);
	} else
	if (c[x][y] == 'S')
	{
		cc[x][y] = 'a' + fill(x + 1, y);
	} else
	if (c[x][y] == 'W')
	{
		cc[x][y] = 'a' + fill(x, y - 1);
	} else
	if (c[x][y] == 'E')
	{
		cc[x][y] = 'a' + fill(x, y + 1);
	}

	return cc[x][y] - 'a';
}

int main(void)
{
	int t, tc = 1;
	scanf("%d", &t);

	while (t--)
	{
		scanf("%d %d", &h, &w);
		
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				scanf("%d", &m[i][j]);
			}
		}

		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				flow(i, j);
			}
		}

		memset(cc, -1, sizeof(cc));
		qc = 0;

		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				if (cc[i][j] == -1)
				{
					fill(i, j);
				}
			}
		}

		printf("Case #%d:\n", tc++);
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				if (j == 0) printf("%c", cc[i][j]);
				else printf(" %c", cc[i][j]);
			} printf("\n");
		}
	}
	
	return 0;
}
