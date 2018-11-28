#include <cstdio>
#include <cmath>

#include <algorithm>
using namespace std;
#define M 10007
int test;
int c[200][200];

#define x first
#define y second
pair<int, int> p[30];

int C(int a, int b)
{
	return c[a][b];
	if (b / M - a / M - (b - a) / M > 0)
		return 0;
	if (a == 0 || a == b)
		return 1;
	int t = C(a, b - 1) + C(a - 1, b - 1);
	if (t >= M)
		t -= M;
	return t;
}

int path(int a, int b)
{
	if (a <= 0 || b <= 0)
		return 0;
	--a; --b;
	if ((a + b) % 3 != 0)
		return 0;
	int t1 = a - (a + b) / 3, t2 = b - (a + b) / 3;
	if (t1 < 0 || t2 < 0)
		return 0;
	return C(t1, t1 + t2);
}

void work()
{
	c[0][0] = 1;
	c[1][1] = c[0][1] = 1;
	for (int i = 2; i <= 100; ++i)
	{
		c[0][i] = 1;
		for (int j = 1; j <= i; ++j)
			c[j][i] = (c[j - 1][i - 1] + c[j][i - 1]) % M;
	}
	int h, w, r;
	scanf("%d%d%d", &h, &w, &r);
	for (int i = 0; i < r; ++i)
	{
		scanf("%d%d", &p[i].x, &p[i].y);
	}
	sort(p, p + r);
	int ans = 0;
	for (int s = 0; s < 1 << r; ++s)
	{
		int cnt = 0, x = 1, y = 1, way = 1;
		for (int i = 0; i < r; ++i)
		{
			if (s & 1 << i)
			{
				++cnt;
				way = way * path(p[i].x - x + 1, p[i].y - y + 1) % M;
				x = p[i].x; y = p[i].y;
			}
		}
		way = way * path(h - x + 1, w - y + 1) % M;
		if (cnt & 1)
			way = -way;
		ans += way;
		ans %= M;
	}
	ans %= M;
	if (ans < 0)
		ans += M;
	printf("Case #%d: %d\n", ++test, ans);
}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
		work();
}
