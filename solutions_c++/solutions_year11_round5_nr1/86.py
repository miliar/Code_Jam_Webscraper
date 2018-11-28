#pragma comment(linker, "/STACK:32000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <stdarg.h>
#include <memory.h>
#include <string.h>

using namespace std;

const double pi = 3.1415926535897932384626433832795;
#define ALL(x) x.begin(), x.end()
#define LL long long
#define MP make_pair
#define PB push_back
#define CLR(a,b) memset(a, b, sizeof(a))
template<class T> inline T Sqr(const T &x) { return x*x; }
template<class T> inline T Abs(const T &x) { return x >= 0 ? x : -x; }
#define fo(i, n) for (int i = 0; i < (n); i++)
#define foz(i, a) for (int i = 0; i < (a).size(); i++)

typedef double gbase;
const gbase geps = 1e-9;

struct Point
{
	gbase x, y;
	Point(gbase x = 0, gbase y = 0) : x(x), y(y) {}
	Point to(const Point &p) const { return Point(p.x - x, p.y - y); }
	gbase dot(const Point &p) const { return p.x * x + p.y * y; }
	gbase cross(const Point &p) const { return x * p.y - y * p.x; }
	gbase len2() const { return x*x + y*y; }
	double len() const { return sqrt(len2()); }
	Point normalized() const { double t = len(); return Point(x/t, y/t); }
	friend Point operator + (const Point &a, const Point &b) { return Point(a.x + b.x, a.y + b.y); }
	friend Point operator - (const Point &a, const Point &b) { return Point(a.x - b.x, a.y - b.y); }
	friend Point operator * (gbase k, const Point &p) { return Point(p.x * k, p.y * k); }
	friend Point operator * (const Point &p, gbase k) { return Point(p.x * k, p.y * k); }
	friend bool operator < (const Point &u, const Point &v) { return false; }
};

struct Line
{
	gbase a, b, c;
	Line(gbase a, gbase b, gbase c) : a(a), b(b), c(c) {}
	static Line PP(const Point &u, const Point &v) { double a = u.y - v.y, b = v.x - u.x; return Line(a, b, -(a * u.x + b * u.y)); }
	static Line PN(const Point &p, const Point &n) { return Line(n.x, n.y, -(n.x * p.x + n.y * p.y)); }
	gbase at(const Point &p) const { return a * p.x + b * p.y + c; }
	gbase sigdist(const Point &p) const { return at(p) / sqrt(a*a+b*b); }
	Point isect(const Line &other) { double d = a*other.b - b*other.a; return Point((b*other.c - c*other.b) / d, (c*other.a - a*other.c) / d); }
};

void init()
{

}

#define maxn 105

int w, l, u, g;
Point a[maxn], b[maxn];

Point readpoint()
{
	int x, y;
	scanf("%d%d", &x, &y);
	return Point(x, y);
}

double calc(Point a, Point b)
{
	return (a.y + b.y) * 0.5 * (b.x - a.x);
}

double calcarea(double x)
{
	// upper part
	int i = 0;
	int n_segs = u - 1;
	double s = 0;
	while (i + 1 < n_segs && b[i+1].x < x) {
		s += calc(b[i], b[i+1]);
		i++;
	}
	Line q = Line::PP(b[i], b[i+1]);
	Line z = Line::PP(Point(x, 0), Point(x, 1));
	Point p = q.isect(z);
	s += calc(b[i], p);
	// lower part
	i = 0;
	n_segs = l - 1;
	while (i + 1 < n_segs && a[i+1].x < x)
	{
		s -= calc(a[i], a[i+1]);
		i++;
	}
	q = Line::PP(a[i], a[i+1]);
	p = q.isect(z);
	s -= calc(a[i], p);
	return s;
}

double getx(double s)
{
	double l = 0, r = w;
	fo(it, 100)
	{
		double m = (l + r) / 2;
		if (calcarea(m) > s)
			r = m;
		else
			l = m;
	}
	return l;
}

void solvecase()
{
	scanf("%d%d", &w, &l);
	scanf("%d%d", &u, &g);
	fo(i, l) a[i] = readpoint();
	fo(i, u) b[i] = readpoint();
	double tot = calcarea(w);
	for (int i = 1; i < g; i++)
	{
		double need = tot / g * i;
		double x = getx(need);
		printf("\n%.8le", x);
	}
}

void solve() {
	init();
	int n_tests;
	scanf("%d", &n_tests);
	for (int i = 1; i <= n_tests; i++)
	{
		printf("Case #%d: ", i);
		solvecase();
		printf("\n");
	}
}

#define problem_letter "A"
//#define fname "test"
//#define fname problem_letter "-small-attempt0"
//#define fname problem_letter "-small-attempt1"
//#define fname problem_letter "-small-attempt2"
#define fname problem_letter "-large"

int main()
{
	freopen(fname ".in", "r", stdin);
	freopen(fname ".out", "w", stdout);
	solve();
	return 0;
}