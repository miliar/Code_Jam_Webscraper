#include <stdio.h>
#include <math.h>
#include <algorithm>

using namespace std;

double dist(double x1, double y1, double x2, double y2)
{
	return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

int main()
{
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);

	int t, test, i, n;
	double x[3], y[3], r[3];

	scanf("%d", &t);

	for(test = 1; test <= t; ++test)
	{
		scanf("%d", &n);
		for(i = 0; i < n; ++i)
		{
			scanf("%lf %lf %lf", &x[i], &y[i], &r[i]);
		}
		if(n == 1)
		{
			printf("Case #%d: %.8lf\n", test, r[0]);
		}
		else if(n == 2)
		{
			printf("Case #%d: %.8lf\n", test, max(r[0], r[1]));
		}
		else
		{
			double sol = 1000000;
			double temp;
			temp = max(r[0], (dist(x[1], y[1], x[2], y[2]) + r[1] + r[2]) / 2);
			if(sol > temp)
			{
				sol = temp;
			}
			temp = max(r[1], (dist(x[0], y[0], x[2], y[2]) + r[0] + r[2]) / 2);
			if(sol > temp)
			{
				sol = temp;
			}
			temp = max(r[2], (dist(x[0], y[0], x[1], y[1]) + r[0] + r[1]) / 2);
			if(sol > temp)
			{
				sol = temp;
			}
			printf("Case #%d: %.8lf\n", test, sol);
		}
	}
	
	return 0;
}
