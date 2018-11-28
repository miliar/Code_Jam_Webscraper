#include <cmath>
#include <cstdio>

int v1[1002], v2[1002], v3[1002], v4[1002], x[1002], y[1002], z[1002], p[1002], n;
bool check(double c)
{
	double left = -1e100, right = 1e100;
	for (int i = 0; i < n; ++i)
	{
		if (left < v1[i] - p[i] * c)
			left = v1[i] - p[i] * c;
		if (right > v1[i] + p[i] * c)
			right = v1[i] + p[i] * c;
		if (right < left)
			return 0;
	}
	left = -1e100, right = 1e100;
	for (int i = 0; i < n; ++i)
	{
		if (left < v2[i] - p[i] * c)
			left = v2[i] - p[i] * c;
		if (right > v2[i] + p[i] * c)
			right = v2[i] + p[i] * c;
		if (right < left)
			return 0;
	}
	left = -1e100, right = 1e100;
	for (int i = 0; i < n; ++i)
	{
		if (left < v3[i] - p[i] * c)
			left = v3[i] - p[i] * c;
		if (right > v3[i] + p[i] * c)
			right = v3[i] + p[i] * c;
		if (right < left)
			return 0;
	}
	left = -1e100, right = 1e100;
	for (int i = 0; i < n; ++i)
	{
		if (left < v4[i] - p[i] * c)
			left = v4[i] - p[i] * c;
		if (right > v4[i] + p[i] * c)
			right = v4[i] + p[i] * c;
		if (right < left)
			return 0;
	}
	return 1;
}

int test;
void work()
{
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		scanf("%d%d%d%d", &x[i], &y[i], &z[i], &p[i]);
		v1[i] = x[i] + y[i] + z[i];
		v2[i] = x[i] + y[i] - z[i];
		v3[i] = x[i] - y[i] + z[i];
		v4[i] = x[i] - y[i] - z[i];
	}
	double lo = 0, hi = 6000000;
	while (hi - lo > 1e-7)
	{
		double c = (lo + hi) / 2;
		if (check(c))
			hi = c;
		else
			lo = c;
	}
	printf("Case #%d: %.6lf\n", ++test, (lo + hi) /2 );
}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
		work();
}
