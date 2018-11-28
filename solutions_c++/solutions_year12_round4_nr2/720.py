#include <iostream>
#include <fstream>
#include <cassert>
#include <cstdlib>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>
#include <cstring>

#define all(x) (x).begin(),(x).end()

using namespace std;

struct point
{
	double x,y;
	point(double x = 0, double y = 0) : x(x), y(y) {};
};

point operator - (const point& a, const point& b)
{
	return point(a.x - b.x, a.y - b.y);
}

point operator + (const point& a, const point& b)
{
	return point(a.x + b.x, a.y + b.y);
}

point operator * (const point& a, double b)
{
	return point(a.x * b, a.y * b);
}

point operator * (double b, const point& a)
{
	return a * b;
}

struct circle
{
	point c;
	double r;
	circle(point c, double r): c(c), r(r) {};
	circle(double x = 0, double y = 0, double r = 0): c(x,y), r(r) {};
};

double minX = 0;
double maxX;
double minY = 0;
double maxY;

const double eps = 1e-9;

bool _eq(double a, double b)
{
	return abs(a - b) < eps;
}

bool _gt(double a, double b)
{
	return a > b && !_eq(a,b);
}

bool _ls(double a, double b)
{
	return a < b && !_eq(a,b);
}

double sqr(double x)
{
	return x * x;
}

int n;
const int nmax = 1e5;
circle c[nmax];
point v[nmax];

double dist(const point& a, const point& b)
{
	return sqrt(sqr(a.x - b.x) + sqr(a.y - b.y));
}

bool inter(const circle& a, const circle& b)
{	
	double d = dist(a.c, b.c);
	return _gt(a.r + b.r, d);
}

point norm(const point& a)
{
	double q = sqrt(max(double(0), sqr(a.x) + sqr(a.y)));
	if (_eq(q, 0)) q = 1;
	return point(a.x / q, a.y / q);
}

bool push(int a, int b, double coef)
{
	if (!inter(c[a], c[b])) return false;
	double delta = c[a].r + c[b].r - dist(c[a].c, c[b].c);
	delta *= coef;
	point va = norm(c[b].c - c[a].c);
	v[a] = v[a] + va * delta;
	v[b] = v[b] - va * delta;
	return 1;
};

void solve(int tc)
{
	printf("Case #%d: ", tc);
	cin >> n >> maxX >> maxY;
	for (int i = 0; i < n; i++)
		cin >> c[i].r;
	for (int i = 0; i < n; i ++)
	{
		c[i].c.x = drand48() * maxX;
		c[i].c.y = drand48() * maxY;
	}
	bool ok = 0;
	while (!ok)
	{
		for (double C = 2.0; C > 0.495; C -= 0.1)
		{
			ok = 1;
			for (int i = 0; i < n; i ++)
				v[i] = point();
			for (int i = 0; i < n; i ++)
				for (int j = i + 1; j < n; j++)
					ok = ok && !push(i, j, C);
			if (ok) break;
			for (int i = 0; i < n; i ++)
			{
				c[i].c = c[i].c + v[i];
				c[i].c.x = max(c[i].c.x, minX);
				c[i].c.x = min(c[i].c.x, maxX);
				c[i].c.y = max(c[i].c.y, minY);
				c[i].c.y = min(c[i].c.y, maxY);
			}
		}
	}
	cerr << "Test " << tc << " OK" << endl;
	for (int i = 0; i < n; i ++)
		for (int j = i + 1; j < n; j ++)	
			assert(!inter(c[i], c[j]));
	for (int i = 0; i < n; i ++)
		printf("%.10lf %.10lf ", c[i].c.x, c[i].c.y);
	printf("\n");
}

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i ++)
		solve(i + 1);
	return 0;
};
