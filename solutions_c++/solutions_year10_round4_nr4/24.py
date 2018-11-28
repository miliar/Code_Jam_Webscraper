#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
#include <bitset>
#include <sstream>
#include <set>
#include <map>

using namespace std;
template <class T> T sqr(T a) { return a * a; }

struct point
{
	double x, y;
};

int eq(double a, double b)
{
	return fabs(a - b) < 1e-6;
}

int leq(double a, double b)
{
	return eq(a, b) || a < b;
}

int lneq(double a, double b)
{
	return !eq(a, b) && a < b;
}

double solve(double ra, double rb, double d)
{
	double angle = acos((sqr(ra) + sqr(d) - sqr(rb)) / 2 / ra / d);
	return angle * sqr(ra) - sqr(ra) * cos(angle) * sin(angle); 
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		int n, m;
		point a, b;
		scanf("%d%d%lf%lf%lf%lf", &n, &m, &a.x, &a.y, &b.x, &b.y);
		printf("Case #%d: ", testCount + 1);
		double d = sqrt(sqr(a.x - b.x) + sqr(a.y - b.y));
		for (int i = 0; i < m; i++)
		{
			point c;
			scanf("%lf%lf", &c.x, &c.y);
			double ra = sqrt(sqr(a.x - c.x) + sqr(a.y - c.y));
			double rb = sqrt(sqr(b.x - c.x) + sqr(b.y - c.y));
			double res;
			if (leq(ra + rb, d))
				res = 0;
			else if (leq(rb + d ,ra))
				res = 2 * acos(-1.0) * sqr(rb);
			else if (leq(ra + d ,rb))
				res = 2 * acos(-1.0) * sqr(ra);
			else
				res = solve(ra, rb, d) + solve(rb, ra, d);
			printf("%lf ", res);
		}
		printf("\n");
	}
	return 0;
}