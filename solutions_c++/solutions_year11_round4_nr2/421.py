#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cctype>

using namespace std;
template <class T> T sqr(T a) { return a * a; }
#define maxn 510

struct point
{
	long long y, x, w;

	point() { }
	point(long long yy, long long xx, long long ww): y(yy), x(xx), w(ww) { }

	point operator+ (point p)
	{
		return point(y + p.y, x + p.x, w + p.w);
	}

	point operator- (point p)
	{
		return point(y - p.y, x - p.x, w - p.w);
	}

	point operator* (long long d)
	{
		return point(y * d, x * d, w);
	}
};

point vp[maxn][maxn];
point curp[maxn];
char s[maxn][maxn];
int r, c, d;

long long getw(int i, int j)
{
	return d + s[i][j] - '0';
}

point getp(int i, int j)
{
	return point(i, j, getw(i, j)) * getw(i, j);
}

int main()
{
#ifdef impetus
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int testnum;
	scanf("%d", &testnum);
	for (int tc = 0; tc < testnum; tc++)
	{
		scanf("%d%d%d", &r, &c, &d);
		for (int i = 0; i < r; i++)
			scanf("%s", s[i]);
		int result = 1;
		for (int i = 0; i < c; i++)
		{
			vp[i][0] = point(0, 0, 0);
			for (int j = 0; j < r; j++)
				vp[i][j + 1] = vp[i][j] + getp(j, i);
		}
		for (int k = min(r, c); k >= 3 && result == 1; k--)
			for (int i = 0; i < r - k + 1 && result == 1; i++)
			{
				curp[0] = point(0, 0, 0);
				for (int j = 0; j < k; j++)
					curp[0] = curp[0] + vp[j][i + k] - vp[j][i];
				for (int j = 1; j < c - k + 1; j++)
					curp[j] = curp[j - 1] - (vp[j - 1][i + k] - vp[j - 1][i]) + (vp[j + k - 1][i + k] - vp[j + k - 1][i]);
				for (int j = 0; j < c - k + 1 && result == 1; j++)
				{
					curp[j] = curp[j] - (getp(i, j) + getp(i + k - 1, j) + getp(i, j + k - 1) + getp(i + k - 1, j + k - 1));
					if (fabs(1.0 * curp[j].y / curp[j].w - (i + k / 2.0 - 0.5)) < 1e-8 &&
						fabs(1.0 * curp[j].x / curp[j].w - (j + k / 2.0 - 0.5)) < 1e-8)
						result = k;
				}
			}
		if (result == 1)
			printf("Case #%d: IMPOSSIBLE\n", tc + 1);
		else	
			printf("Case #%d: %d\n", tc + 1, result);
	}
	return 0;
}