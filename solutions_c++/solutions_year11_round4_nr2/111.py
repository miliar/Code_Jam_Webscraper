#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <bitset>
#include <queue>

using namespace std;

int n, m, d;
char s[600][600];

long long x[600][600], y[600][600];
long long dx[600][600], dy[600][600];

long long f[600][600], g[600][600];

long long sumx(int i, int j)
{
	if (i < 0 || j < 0) return 0;
	return x[i][j];
}

long long sumy(int i, int j)
{
	if (i < 0 || j < 0) return 0;
	return y[i][j];
}

long long sumf(int i, int j)
{
	if (i < 0 || j < 0) return 0;
	return f[i][j];
}


void solve(int test)
{
	scanf("%d%d%d\n", &n, &m, &d);
	for (int i = 0; i < n; i ++)
		gets(s[i]);

	for (int i = 0; i < n; i ++)
		for (int j = 0; j < m; j ++)
			dx[i][j] = (long long)(i) * (long long)(s[i][j] - '0' + d),
			dy[i][j] = (long long)(j) * (long long)(s[i][j] - '0' + d),
			g[i][j] = (long long)(s[i][j] - '0' + d);

	f[0][0] = g[0][0];
	for (int i = 1; i < m; i ++) y[0][i] = y[0][i - 1] + dy[0][i], f[0][i] = f[0][i - 1] + g[0][i];
	for (int i = 1; i < n; i ++) x[i][0] = x[i - 1][0] + dx[i][0], f[i][0] = f[i - 1][0] + g[i][0];


	for (int i = 1; i < n; i ++)
		for (int j = 1; j < m; j ++)
		{
			x[i][j] = x[i - 1][j] + x[i][j - 1] - x[i - 1][j - 1];
			y[i][j] = y[i - 1][j] + y[i][j - 1] - y[i - 1][j - 1];
			x[i][j] += dx[i][j];
			y[i][j] += dy[i][j];

			f[i][j] = f[i - 1][j] + f[i][j - 1] - f[i - 1][j - 1];
			f[i][j] += g[i][j];
		}

	for (int k = max(n, m); k >= 3; k --)
		for (int i = k - 1; i < n; i ++)
			for (int j = k - 1; j < m; j ++)
			{
				long long x1 = i, y1 = j, x2 = i - k + 1, y2 = j - k + 1;
				long long s1 = sumx(x1, y1) - sumx(x2 - 1, y1) - sumx(x1, y2 - 1) + sumx(x2 - 1, y2 - 1);
				long long s2 = sumy(x1, y1) - sumy(x2 - 1, y1) - sumy(x1, y2 - 1) + sumy(x2 - 1, y2 - 1);
				long long ms = sumf(x1, y1) - sumf(x2 - 1, y1) - sumf(x1, y2 - 1) + sumf(x2 - 1, y2 - 1);
				s1 -= dx[x1][y1] + dx[x1][y2] + dx[x2][y1] + dx[x2][y2];
				s2 -= dy[x1][y1] + dy[x1][y2] + dy[x2][y1] + dy[x2][y2];
				ms -= g[x1][y1] + g[x1][y2] + g[x2][y1] + g[x2][y2];

				long long A = (x1 + x2) * ms - s1 * 2LL;
				long long B = (y1 + y2) * ms - s2 * 2LL;
				if (A == 0LL && B == 0LL) 
				{
					printf("Case #%d: %d\n", test, k);
					return ;
				}
			}

	printf("Case #%d: IMPOSSIBLE\n", test);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	scanf("%d\n", &test);
	for (int i = 1; i <= test; i ++)
	{
		cerr << i << endl;
		solve(i);
	}
	return 0;
}