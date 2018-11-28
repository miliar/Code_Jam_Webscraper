#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <numeric>

using namespace std;

#define INF (2000000000)

const int nmax = 100;

struct P
{
	double x, y;
	P(double xx = 0, double yy = 0)
	{
		x = xx;
		y = yy;
	}
	void scan()
	{
		scanf("%lf%lf", &x, &y);
	}
	double cs(const P& other) const
	{
		return x * other.y - other.x * y;
	}
	double dp(const P& other) const
	{
		return x * other.x + other.y * y;
	}
	double lg()
	{
		return sqrt(x * x + y * y);
	}
	P operator -(const P& other) const
	{
		return P(x - other.x, y - other.y);
	}
};

P p[nmax];
P q[nmax];

double sq(double r, double angle)
{
	return (angle * r * r - r * r * sin(angle)) / 2.0;
}

void solveTest()
{
	int n, m;
	int i;
	scanf("%d%d", &n, &m);
	for(i = 0; i < n; ++i)
	{
		p[i].scan();
	}
	for(i = 0; i < m; ++i)
	{
		q[i].scan();
	}

	double g = (p[0] - p[1]).lg();
	for(i = 0; i < m; ++i)
	{
		double lg1 = (p[0] - q[i]).lg();
		double lg2 = (p[1] - q[i]).lg();

		double d1 = (p[1] - p[0]).dp(q[i] - p[0]);
		double d2 = (p[0] - p[1]).dp(q[i] - p[1]);

		double a1 = 2 * acos(d1 / (g * lg1));
		double a2 = 2 * acos(d2 / (g * lg2));

		double anst = sq(lg1, a1) + sq(lg2, a2);
		printf("%.10lf ", anst);
	}
	printf("\n");
}

int main()
{
	int t;
	int i;
	freopen("D.txt", "r", stdin);
	freopen("D_out.txt", "w", stdout);
	scanf("%d", &t);
	for(i = 0; i < t; ++i)
	{
		printf("Case #%d: ", i + 1);
		cerr << i + 1 << " Done!\n";
		solveTest();
	}
	return 0;
}
