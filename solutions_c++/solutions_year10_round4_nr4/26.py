#include <cstdio>
#include <cmath>
#include <cstring>

struct point
{
	int x, y;
};

const int maxn = 2;
const long double pi = atan(1) * 4;

int n, m;
point a[maxn];
point q;

int cm(point a, point b, point c)
{
	return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

int dm(point a, point b, point c)
{
	return (b.x - a.x) * (c.x - a.x) + (b.y - a.y) * (c.y - a.y);
}

long double calc(point a, point b, point c)
{
	long double at = fabsl((long double) cm(a, b, c) / 2);
	long double angle1 = acosl(dm(a, b, c) / sqrtl(dm(a, b, b)) / sqrtl(dm(a, c, c)));
	long double angle2 = acosl(dm(b, a, c) / sqrtl(dm(b, a, a)) / sqrtl(dm(b, c, c)));
	return angle1 * dm(a, c, c) / 2 + angle2 * dm(b, c, c) / 2 - at;
}

int main()
{
	int testnumber;
	
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("d.out", "w", stdout);
	
	scanf("%d", &testnumber);
	for (int testcount = 0; testcount < testnumber; testcount++)
	{
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
			scanf("%d%d", &a[i].x, &a[i].y);
		
		printf("Case #%d:", testcount + 1);
		for (int j = 0; j < m; j++)
		{
			scanf("%d%d", &q.x, &q.y);
			double d = calc(a[0], a[1], q) * 2;
			printf(" %.7lf", d);
		}
		printf("\n");
	}
	
	return 0;
}
