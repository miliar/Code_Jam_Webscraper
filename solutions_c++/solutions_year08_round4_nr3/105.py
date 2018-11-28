#include <iostream>
#include <cmath>

using	namespace	std;

const	int	maxn = 1000;

int	n, cases;
int	x[maxn + 1], y[maxn + 1], z[maxn + 1];
int	p[maxn + 1];

inline	int	cmp(const double &x, const double &y)
{
	if (fabs(x - y) < 1e-8)
		return	0;
	else
		return	x < y ? -1 : 1;
}

inline	double	calc(const double xx, const double yy, const double zz)
{
	double	rtn = 0;
	for (int i = 0; i < n; ++i)
		rtn = max(rtn, static_cast<double>(abs(xx - x[i]) + abs(yy - y[i]) + abs(zz - z[i])) / p[i]);
	return	rtn;
}

void	solve()
{
	scanf("%d", &n);
	int	maxx = 0, minx = INT_MAX, maxy = 0, miny = INT_MAX, maxz = 0, minz = INT_MAX;
	for (int i = 0; i < n; ++i)
	{
		scanf("%d%d%d%d", &x[i], &y[i], &z[i], &p[i]);
		maxx = max(maxx, x[i]);	minx = min(minx, x[i]);
		maxy = max(maxy, y[i]);	miny = min(miny, y[i]);
		maxz = max(maxz, z[i]);	minz = min(minz, z[i]);
	}
	double	xx = (minx + maxx) * 0.5;
	double	yy = (miny + maxy) * 0.5;
	double	zz = (minz + maxz) * 0.5;
	double	delta = max(maxx - minx, max(maxy - miny, maxz - minz));
	double	ans = calc(xx, yy, zz);

	while (delta > 1e-8)
	{
		while (true)
		{
			double	t = calc(xx + delta, yy, zz);
			if (cmp(t, ans) < 0)
			{
				ans = t;
				xx += delta;
			}
			else
				break;
		}
		while (true)
		{
			double	t = calc(xx - delta, yy, zz);
			if (cmp(t, ans) < 0)
			{
				ans = t;
				xx -= delta;
			}
			else
				break;
		}
		while (true)
		{
			double	t = calc(xx, yy + delta, zz);
			if (cmp(t, ans) < 0)
			{
				ans = t;
				yy += delta;
			}
			else
				break;
		}
		while (true)
		{
			double	t = calc(xx, yy - delta, zz);
			if (cmp(t, ans) < 0)
			{
				ans = t;
				yy -= delta;
			}
			else
				break;
		}
		while (true)
		{
			double	t = calc(xx, yy, zz + delta);
			if (cmp(t, ans) < 0)
			{
				ans = t;
				zz += delta;
			}
			else
				break;
		}
		while (true)
		{
			double	t = calc(xx, yy, zz - delta);
			if (cmp(t, ans) < 0)
			{
				ans = t;
				zz -= delta;
			}
			else
				break;
		}
		delta *= 0.5;
	}
	printf("Case #%d: %.6lf\n", ++cases, ans);
}

int	main()
{
	int	t;
	scanf("%d", &t);
	while (t--)	solve();
	return	0;
}

