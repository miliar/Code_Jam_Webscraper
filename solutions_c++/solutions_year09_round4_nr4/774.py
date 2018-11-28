#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;

double dist(double x1, double y1, double x2, double y2)
{
	double t1 = (x2-x1)*(x2-x1);
	double t2 = (y2-y1)*(y2-y1);
	return sqrt(t1+t2);
}

int main()
{
	freopen("D-small-attempt3.in", "r", stdin);
	freopen("small.out", "w", stdout);

	int T;
	scanf("%d", &T);
	double x[64], y[64], r[64];
	for ( int t=1 ; T-- ; ++t )
	{
		int n;
		scanf("%d", &n);

		double res = 1e10;
		for ( int i=0 ; i<n ; ++i )
		{
			scanf("%lf %lf %lf", &x[i], &y[i], &r[i]);
		}

		if ( n == 1 ) 
		{
			res = r[0];
		}
		if ( n == 2 )
		{
			res = max(r[0], r[1]);
		}
		if ( n == 3 )
		{
			double r1 = max(dist(x[0], y[0], x[1], y[1])+r[0]+r[1], r[2]) * 0.5;
			double r2 = max(dist(x[0], y[0], x[2], y[2])+r[0]+r[2], r[1]) * 0.5;
			double r3 = max(dist(x[2], y[2], x[1], y[1])+r[2]+r[1], r[0]) * 0.5;
			if ( dist(x[0], y[0], x[1], y[1])+min(r[0], r[1]) <= max(r[0], r[1]) )
			{
				res = min(res, max(max(r[0], r[1]), r[2]));
			}
			if ( dist(x[0], y[0], x[2], y[2])+min(r[0], r[2]) <= max(r[0], r[2]) )
			{
				res = min(res, max(max(r[0], r[1]), r[2]));
			}
			if ( dist(x[2], y[2], x[1], y[1])+min(r[2], r[1]) <= max(r[2], r[1]) )
			{
				res = min(res, max(max(r[0], r[1]), r[2]));
			}
			res = min(res, r1);
			res = min(res, r2);
			res = min(res, r3);
		}
		printf("Case #%d: %.8lf\n", t, res);
	}

	return 0;
}
