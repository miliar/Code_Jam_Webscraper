/*
 * C.cpp
 *
 *  Created on: 2010-6-5
 *      Author: stm
 */

#include <cstdio>
#include <cstring>
#include <memory>
using namespace std;

const int MAXN = 1010, MAXH = 4999999;
int n, h[MAXH][2], a[MAXN][MAXN], b[MAXN][MAXN];
bool used[MAXH];

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int C;
	scanf("%d", &C);
	for (int cases = 1; cases <= C; ++cases)
	{
		scanf("%d", &n);
		memset(a, 0, sizeof(a));
		int x1, x2, y1, y2;
		for (int i = 0; i < n; ++i)
		{
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int x = x1; x <= x2; ++x)
				for (int y = y1; y <= y2; ++y)
					a[y][x] = 1;
		}
		int ans = 0;
		while (n)
		{
			/*printf("%d\n", n);
			for (int j = 1; j <= 5 ; ++j)
			{
				for (int i = 1; i < 6; ++i)
					printf("%d ", a[j][i]);
				puts("");
			}*/
			for (int i = 0; i < 110; ++i)
				for (int j = 0; j < 110; ++j)
				{
					b[i][j] = 0;
					if (a[i][j])
					{
						if (i == 0 || j == 0)
						{ continue; }
						if (a[i - 1][j] || a[i][j - 1])
							b[i][j] = 1;
					}
					else
					{
						if (i == 0 || j == 0)
						{ continue; }
						if (a[i - 1][j] && a[i][j - 1])
						{
							b[i][j] = 1;
						}
					}
				}
			n = 0;
			for (int i = 0; i < 110; ++i)
				for (int j = 0; j < 110; ++j)
				{
					a[i][j] = b[i][j];
					if (a[i][j]) ++n;
				}
			++ans;
		}
		printf("Case #%d: %d\n", cases, ans);
	}
}
