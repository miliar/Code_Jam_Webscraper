#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <cmath>
using namespace std;

int x[30], y[30], r[30];

double solve(int i, int j)
{
	double le=sqrt((double) (x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]));
	return (le+r[i]+r[j])/2.0;
}

double maxx(double a, double b)
{
	return a>b?a:b;
}

double minn(double a, double b)
{
	return a>b?b:a; 
}

void runtest()
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d %d %d", &x[i], &y[i], &r[i]);
	}

	if (n == 1)
	{
		printf(" %d\n", r[0]);
	}
	else if (n == 2)
	{
		printf(" %d\n", r[0]>r[1]?r[0]:r[1]);
	}
	else
	{
		double d1=solve(0,1);
		double d2=solve(0,2);
		double d3=solve(1,2);
		double x1=maxx(d1,r[2]);
		double x2=maxx(d2,r[1]);
		double x3=maxx(d3,r[0]);

		printf(" %.9lf\n", minn(minn(x1,x2),x3));
	}
}



int main()
{
	freopen("C:\\b1.txt", "r", stdin);
	freopen("C:\\b1out.txt", "w", stdout);

	int tests;
	scanf("%d\n", &tests);

	for (int te = 1; te <= tests; te++)
	{
		printf("Case #%d:", te);
		runtest();
	}

	return 0;
}
