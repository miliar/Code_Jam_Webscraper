#include <cstdio>
#include <cmath>

double x, y, z;
double vx, vy, vz;
double xx0, yy0, zz0;
double vx0, vy0, vz0;

int t, n;
double t0, d0;

double Sqr(double x)
{
	return x*x;
}

int main()
{
	freopen("firefly.in", "r", stdin);
	freopen("firefly.out", "w", stdout);

	scanf("%d", &t);
	for (int tnum = 1; tnum <= t; tnum++)
	{
		xx0 = 0;
		yy0 = 0;
		zz0 = 0;
		vx0 = 0;
		vy0 = 0;
		vz0 = 0;

		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%lf%lf%lf%lf%lf%lf", &x, &y, &z, &vx, &vy, &vz);
			xx0 += x;
			yy0 += y;
			zz0 += z;
			vx0 += vx;
			vy0 += vy;
			vz0 += vz;
		}

		if (fabs(Sqr(vx0) + Sqr(vy0) + Sqr(vz0)) < 1e-2)
			t0 = 0;
		else
			t0 = -(xx0*vx0 + yy0*vy0 + zz0*vz0)/(Sqr(vx0) + Sqr(vy0) + Sqr(vz0));
		if (t0 < 0)
			t0 = 0;

		d0 = sqrt(Sqr(xx0 + t0*vx0) + Sqr(yy0 + t0*vy0) + Sqr(zz0 + t0*vz0))/n;

		printf("Case #%d: %.10lf %.10lf\n", tnum, d0, t0);
	}

	return 0;
}