#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const int NMAX = 45;

struct Circle
{
	double x, y, r;
};

Circle a[NMAX];
int n;

double Sqr(double x)
{
	return x*x;
}

double Dist(const Circle &c1, const Circle &c2)
{
	return sqrt(Sqr(c2.x - c1.x) + Sqr(c2.y - c1.y));
}

double Count(const Circle &c1, const Circle &c2)
{
	return (Dist(c1, c2) + c1.r + c2.r) / 2;
}

double Solve()
{
	double res;

	if (n == 3)
	{
		res = max(a[0].r, Count(a[1], a[2]));
		res = min(res, max(a[1].r, Count(a[0], a[2])));
		res = min(res, max(a[2].r, Count(a[0], a[1])));
	}
	else if (n == 2)
		res = max(a[0].r, a[1].r);
	else
		res = a[0].r;

	return res;
}

int main()
{
	freopen("sprinkler.in", "r", stdin);
	freopen("sprinkler.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int tnum = 1; tnum <= t; tnum++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%lf%lf%lf", &a[i].x, &a[i].y, &a[i].r);

		printf("Case #%d: %.10lf\n", tnum, Solve());
	}

	return 0;
}
