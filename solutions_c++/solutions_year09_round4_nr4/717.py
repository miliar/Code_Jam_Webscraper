#include <cstdio>
#include <cmath>

int n, tests;
double x[3], y[3], r[3];

double max(double a, double b)
{
	if (a > b)
		return a;
	return b;
}

double min(double a, double b)
{
	if (a < b)
		return a;
	return b;
}

double dist(int a, int b)
{
	return sqrt(pow(x[a] - x[b], 2.0) + pow(y[a] - y[b], 2.0));
}

int main()
{
	scanf("%d", &tests);
	for (int t = 1; t <= tests; t++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%lf %lf %lf", &x[i], &y[i], &r[i]);
		
		printf("Case #%d: ", t);
		if (n == 1)
		{
			printf("%.7lf\n", r[0]);
		}
		else if (n == 2)
		{
			printf("%.7lf\n", max(r[0], r[1]));
		}
		else
		{
			double ans = 1e20, d;
			
			d = dist(0, 1) + r[0] + r[1];
			ans = min(ans, max(d / 2.0, r[2]));
			
			d = dist(0, 2) + r[0] + r[2];
			ans = min(ans, max(d / 2.0, r[1]));

			d = dist(1, 2) + r[1] + r[2];
			ans = min(ans, max(d / 2.0, r[0]));
			
			printf("%.7lf\n", ans);
		}
	}
	return 0;
}