#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

pair<int, int> p[100500];
int n, d;


bool doubleEqual(double a, double b)
{
	double eps = 1e-9;
	return fabs(a - b) < eps;
}


bool doubleGreater(double a, double b)
{
	return a > b && !doubleEqual(a, b);
}


bool good(double t)
{
	double last = 1e9;
	last = - last * last;
	for(int i = 0; i < n; i++)
	{
		double left = p[i].first - t;
		left = max(left, last + d);
		double right = left + d * (p[i].second - 1);
		if(doubleGreater(right, p[i].first + t))
		{
			return false;
		}
		last = right;
	}
	return true;
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testCount;
	scanf("%d", &testCount);
	for(int testNumber = 1; testNumber <= testCount; testNumber++)
	{
		printf("Case #%d: ", testNumber);
		scanf("%d%d", &n, &d);
		for(int i = 0; i < n; i++)
		{
			scanf("%d%d", &p[i].first, &p[i].second);
		}
		sort(p, p + n);
		double l = 0;
		double r = 1e9;
		r = r * r;
		good(1);
		while(fabs(r - l) > 1e-9)
		{
			double m = (l + r) / 2;
			if(good(m) )
			{
				r = m;
			}
			else
			{ 
				l = m;
			}
		}
		printf("%.10lf\n", r);
	}
	return 0;
}