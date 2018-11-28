#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <ctype.h>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

#define For(i, n) for (int i = 0; i < n; i ++)
#define foreach(x, i) for (__typeof(x.begin()) i = x.begin(); i != x.end(); i ++)
#define pb push_back
#define mp make_pair


using namespace std;

const int N = 1000;
char a[N][N];
int n, m, d;
int s[N][N];
int b[N][N];
int S(int x, int y)
{
	if (x < 0 || y < 0)
		return 0;
	return s[x][y];
}

int Sum(int x, int y, int nx, int ny)
{
	int ret = S(nx, ny) - S(x - 1, ny) - S(nx, y - 1) + S(x - 1, y - 1);
	int t = 0;
	for (int i = x; i <= nx; i ++)
		for (int j = y; j <= ny; j ++)
			t += b[i][j];
	assert(t == ret);
	return ret;
}

int SumCol(int x, int y, int len)
{
	return Sum(x, y, x + len - 1, y);
}
int SumRow(int x, int y, int len)
{
	return Sum(x, y, x, y + len - 1);
}


void solve()
{
	scanf("%d%d%d", &n, &m, &d);
	For (i, n) scanf("%s", a[i]);
	For (i, n) For (j, m)
	{
		s[i][j] = S(i - 1, j) + S(i, j - 1) - S(i - 1, j - 1)
		   	+ (b[i][j] = a[i][j] - '0');
	}

	int ans = 0;
	For (sx, n) For (sy, m)
	{
		int suml = 0, sumr = 0, sumu = 0, sumd = 0;
		if (sx == 2 && sy == 2)
			int asdf = 0;
		for (int len = 1;  ;len ++)
		{
			if (!(sx - len >= 0 && sx + len < n && sy - len >= 0 && sy + len < m))
				break;

			suml += SumCol(sx - len + 1, sy - len, len * 2 - 1) * len
				+ SumCol(sx - len, sy - len + 1, 2) * (len - 1)
				+ SumCol(sx + len - 1, sy - len + 1, 2) * (len - 1);

			sumr += SumCol(sx - len + 1, sy + len, len * 2 - 1) * len
				+ SumCol(sx - len, sy + len - 1, 2) * (len - 1)
				+ SumCol(sx + len - 1, sy + len - 1, 2) * (len - 1);

			sumu += SumRow(sx - len, sy - len + 1, len * 2 - 1) * len
				+ SumRow(sx - len + 1, sy - len, 2) * (len - 1)
				+ SumRow(sx - len + 1, sy + len - 1, 2) * (len - 1);

			sumd += SumRow(sx + len, sy - len + 1, len * 2 - 1) * len
				+ SumRow(sx + len - 1, sy - len, 2) * (len - 1)
				+ SumRow(sx + len - 1, sy + len - 1, 2) * (len - 1);

			if (suml == sumr && sumu == sumd)
				ans = max(ans, len * 2 + 1);

		}
	}
	if (ans == 0)
		puts("IMPOSSIBLE");
	else printf("%d\n", ans);
}

int main()
{
	int t; scanf("%d", &t);
	For (i, t)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}

