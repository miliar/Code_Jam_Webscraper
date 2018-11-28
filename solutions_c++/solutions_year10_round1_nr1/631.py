/*
 * A.cpp
 *
 *  Created on: 2010-5-22
 *      Author: stm
 */

#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 52,
		  dx[2] = {1, 1},
		  dy[4] = {1, -1};
char g[MAXN][MAXN], gg[MAXN][MAXN];
int n, k;
bool R, B;

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for (int T = 1; T <= cases; ++T)
	{
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; ++i)
			scanf("%s", g[i]);

		//int tot;

		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				gg[i][j] = g[i][j];

		for (int i = 0; i < n; ++i)
		{
			for (int j = n - 2; j >= 0; --j)
			{
				if (gg[i][j] == '.') continue;
				int p = j;
				while (p + 1 < n && gg[i][p + 1] == '.')
				{
					gg[i][p + 1] = gg[i][p]; gg[i][p] = '.';
					p = p + 1;
				}
			}
		}

	/*	for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
				printf("%c", gg[i][j]);
			puts("");
		}
*/
		R = B = false;
		for (int i = 0; i < n; ++i)
		{
			int c = 0;
			if (gg[i][0] != '.') ++c;
			if (c >= k)
			{
				if (gg[i][0] == 'R') R = true;
				else B = true;
			}
			for (int j = 1; j < n; ++j)
			{
				if (gg[i][j] == '.')
				{
					c = 0;
				}
				else
				{
					if (gg[i][j] == gg[i][j - 1])
					{
						++c;
						if (c >= k)
						{
							if (gg[i][j] == 'R') R = true; else B = true;
						}
					}
					else
					{
						c = 1;
					}
				}
			}
		}
		for (int j = 0; j < n; ++j)
		{
			int c = 0;
			if (gg[0][j] != '.') ++c;
			if (c >= k)
			{
				if (gg[0][j] == 'R') R = true; else B = true;
			}
			for (int i = 1; i < n; ++i)
			{
				if (gg[i][j] == '.')
				{
					c = 0;
				}
				else
				{
					if (gg[i][j] == gg[i - 1][j])
					{
						++c;
						if (c >= k)
						{
							if (gg[i][j] == 'R') R = true; else B = true;
						}
					}
					else
					{
						c = 1;
					}
				}
			}
		}

		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
				if (gg[i][j] != '.')
				{
					int c = 1;
					int x = i, y = j;
					char ch = gg[i][j];
					while (c < k)
					{
						x += dx[0], y += dy[0];
						if (x < 0 || y < 0 || x >= n || y >= n) break;
						if (gg[x][y] != ch) break;
						c++;
					}
					if (c >= k)
					{
						if (gg[i][j] == 'R') R = true; else B = true;
					}
					c = 1;
					x = i, y = j;
					ch = gg[i][j];
					while (c < k)
					{
						x += dx[1], y += dy[1];
						if (x < 0 || y < 0 || x >= n || y >= n) break;
						if (gg[x][y] != ch) break;
						c++;
					}
					if (c >= k)
					{
						if (gg[i][j] == 'R') R = true; else B = true;
					}
				}
		}

		printf("Case #%d: ", T);
		int c = 0;
		if (R) ++c;
		if (B) ++c;
		if (c == 0) puts("Neither");
		else
		if (c == 2) puts("Both");
		else
		{
			if (R) puts("Red");
			else puts("Blue");
		}
	}
	return 0;
}
