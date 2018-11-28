#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cmath>
#include <iterator>
#include <complex>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <list>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

const int MAX = 510;

int n, r, c, d;
char a[MAX][MAX];

int sx[2][MAX][MAX], sy[MAX][MAX][MAX];
int s0x[2][MAX][MAX], s0y[MAX][MAX][MAX];

inline bool get(int x0, int y0, int x1, int y1, int x2, int y2)
{
	if (x1 <= 0 || y1 <= 0 || x2 > r || y2 > c) return false;
	return (s0x[0][x2][y2] + s0x[0][x1 - 1][y1 - 1] - s0x[0][x2][y1 - 1]
		- s0x[0][x1 - 1][y2] - sx[0][x1][y1] - sx[0][x1][y2]
		- sx[0][x2][y1] - sx[0][x2][y2] == 0 &&
		
		s0y[y0][x2][y2] + s0y[y0][x1 - 1][y1 - 1] - s0y[y0][x2][y1 - 1]
		- s0y[y0][x1 - 1][y2] - sy[y0][x1][y1] - sy[y0][x1][y2]
		- sy[y0][x2][y1] - sy[y0][x2][y2] == 0);
}

int main()
{
#ifdef DEBUG
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif

	int t;
	cin >> t;
	for (int test = 1; test <= t; ++test)
	{
		int ans = 0;

		cin >> r >> c >> d;
		for (int i = 1; i <= r; ++i)
		{
			cin >> a[i];
			for (int j = c; j; --j)
				a[i][j] = a[i][j - 1];
		}

		for (int y = 1; y <= c; ++y)
		{
			for (int i = 1; i <= r; ++i)
				for (int j = 1; j <= c; ++j)
					sy[y][i][j] = (a[i][j] - '0' + d) * (j - y);
			for (int i = 1; i <= r; ++i)
				for (int j = 1; j <= c; ++j)
					s0y[y][i][j] = s0y[y][i - 1][j] + s0y[y][i][j - 1] - s0y[y][i - 1][j - 1] + sy[y][i][j];
		}

		bool good = false;
		for (int x = 1; x <= r; ++x)
		{
			for (int i = 1; i <= r; ++i)
				for (int j = 1; j <= c; ++j)
					sx[0][i][j] = (a[i][j] - '0' + d) * (i - x);
			for (int i = 1; i <= r; ++i)
				for (int j = 1; j <= c; ++j)
					s0x[0][i][j] = s0x[0][i - 1][j] + s0x[0][i][j - 1] - s0x[0][i - 1][j - 1] + sx[0][i][j];

			int i = x;
			good = false;
			for (int a = min(r, c); a && !good; --a)
				for (int j = 1; j <= c; ++j)
				{
					if (get(i, j, i - a, j - a, i + a, j + a))
					{
						good = true;
						ans = max(ans, 2 * a + 1);
						break;
					}
				}
		}


		for (int y = 0; y <= c; ++y)
		{
			for (int i = 1; i <= r; ++i)
				for (int j = 1; j <= c; ++j)
					sy[y][i][j] = (a[i][j] - '0' + d) * (2 * j - 2 * y - 1);
			for (int i = 1; i <= r; ++i)
				for (int j = 1; j <= c; ++j)
					s0y[y][i][j] = s0y[y][i - 1][j] + s0y[y][i][j - 1] - s0y[y][i - 1][j - 1] + sy[y][i][j];
		}

		good = false;
		for (int x = 0; x <= r; ++x)
		{
			for (int i = 1; i <= r; ++i)
				for (int j = 1; j <= c; ++j)
					sx[0][i][j] = (a[i][j] - '0' + d) * (2 * i - 2 * x - 1);
			for (int i = 1; i <= r; ++i)
				for (int j = 1; j <= c; ++j)
					s0x[0][i][j] = s0x[0][i - 1][j] + s0x[0][i][j - 1] - s0x[0][i - 1][j - 1] + sx[0][i][j];
		
			int i = x;
			good = false;
			for (int a = min(r, c); a > 1 && !good; --a)
				for (int j = 1; j <= c; ++j)
					if (get(i, j, i - a + 1, j - a + 1, i + a, j + a))
					{
						good = true;
						ans = max(ans, 2 * a);
						break;
					}
		}						

		if (ans)
        	cout << "Case #" << test << ": " << ans << '\n';
        else
        	cout << "Case #" << test << ": " << "IMPOSSIBLE\n";
        cerr << test << endl;
	}

	return 0;
}
