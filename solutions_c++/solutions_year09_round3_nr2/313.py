#include <cstdio>
#include <string>
#include <math.h>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define eps 1e-6

// comment __________________ [placed here for copying in code _ character absent in non-standart keyboard]

int testnum;


struct point
{
	double x, y, z;

	point()
	{
		x = y = z = 0;
	}
};


double sqr(double d)
{
	return d * d;
}

double dist(point p1, point p2)
{
	return sqrt(sqr(p1.x - p2.x) + sqr(p1.y - p2.y) + sqr(p1.z - p2.z));
}

point sc, fc;
double time;

point aa[900];
point vv[900];
int n;

double resdist, restime;

point getcenter(double t)
{
	point a;
	for (int i = 0; i < n; i++)
	{
		a.x += aa[i].x + vv[i].x * t;
		a.y += aa[i].y + vv[i].y * t;
		a.z += aa[i].z + vv[i].z * t;
	}
	a.x /= n;
	a.y /= n;
	a.z /= n;
	return a;
}

double scalar(point o, point a, point b)
{
	return (a.x - o.x) * (b.x - o.x) + (a.y - o.y) * (b.y - o.y) + (a.z - o.z) * (b.z - o.z);
}

void solve()
{
	point orig;
	time = 10000000;
	sc = getcenter(0);
	fc = getcenter(time);
	if (dist(sc, fc) < eps)
	{
		resdist = dist(orig, sc);
		restime = 0;
	}
	else
	{
		double l = 0, r = time;
		point pp;
		while (r - l > 1e-9)
		{
			double c = (l + r) / 2;
			pp.x = sc.x + c / time * (fc.x - sc.x);
			pp.y = sc.y + c / time * (fc.y - sc.y);
			pp.z = sc.z + c / time * (fc.z - sc.z);
			if (scalar(pp, orig, sc) < 0)
				l = c;
			else
				r = c;
		}
		resdist = dist(orig, pp);
		restime = l;
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testnum);
	char s[100];
	for (int testcount = 0; testcount < testnum; testcount++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%lf%lf%lf%lf%lf%lf", &aa[i].x, &aa[i].y, &aa[i].z, &vv[i].x, &vv[i].y, &vv[i].z);
		solve();
		printf("Case #%d: %lf %lf\n", testcount + 1, resdist, restime);
	}
	return 0;
}