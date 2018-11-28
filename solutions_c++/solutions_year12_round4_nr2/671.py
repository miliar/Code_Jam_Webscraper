/*
 * $File: b.cpp
 * $Date: Sat May 26 23:33:44 2012 +0800
 * $Author: Xinyu Zhou <zxytim@gmail.com>
 */

#include <cstdio>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <ctype.h>
#include <cstring>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

#define For(i, n) for (int i = 0; i < n; i ++)
#define Ford(i, n) for (int i = n - 1; i >= 0; i --)
#define pb push_back
#define mp make_pair

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

template<typename T> void checkmax(T &a, T b) { if (b > a) a = b; }
template<typename T> void checkmin(T &a, T b) { if (b < a) a = b; }

typedef pair<int, int> pii;
typedef vector<pii> vpii;

void solve(int case_id);

int main()
{
	srand(42);
	int ncase;
	scanf("%d", &ncase);
	for (int id = 1; id <= ncase; id ++)
	{
		printf("Case #%d: ", id);
		fprintf(stderr, "%d/%d\n", id, ncase);
		solve(id);
	}
	return 0;
}

template<typename T> 
struct PointTemplate
{
	T x, y;
	PointTemplate(){}
	PointTemplate(T _x, T _y) : x(_x), y(_y) {}
	PointTemplate operator + (const PointTemplate &p) const
	{ return PointTemplate(x + p.x, y + p.y); }
	PointTemplate operator - (const PointTemplate &p) const
	{ return PointTemplate(x - p.x, y - p.y); }
	PointTemplate operator * (T f) const
	{ return PointTemplate(x * f, y * f); }
	PointTemplate operator / (T f) const
	{ return PointTemplate(x / f, y / f); }
	T cross(const PointTemplate &p) const
	{ return x * p.y - y * p.x; }
	T mosqr() const { return x * x + y * y; }
	T mo() const { return sqrt(mosqr()); }
	PointTemplate unit() const
	{ return *this / mo(); }
	PointTemplate resize(T f) const
	{ return unit() * f; }

};

typedef PointTemplate<double> Point;

struct Circle
{
	Point center;
	double radius;
	int id;
};

bool cmp(const Circle &a, const Circle &b)
{
	return a.radius > b.radius;
}

bool cmpId(const Circle &a, const Circle &b)
{
	return a.id < b.id;
}

double sqr(double x) { return x * x; }

const int N = 10001;
Circle cir[N];
double W, L;
int n;
double areaCover()
{
	double ret = 0;
	for (int i = 0; i < n; i ++)
		for (int j = i + 1; j < n; j ++)
		{
			double r2 = sqr(cir[i].radius + cir[j].radius);
			double d = sqr(cir[i].center.x - cir[j].center.x) + sqr(cir[i].center.y - cir[j].center.y);
			double val = r2 - d;
			if (val >= 0)
				ret += val;
		}
	return ret;
}

bool in_range(const Point &p)
{
	return p.x >= 0 && p.x <= W && p.y >= 0 && p.y <= L;
}

void solve(int case_id)
{
	scanf("%d%lf%lf", &n, &W, &L);
	for (int i = 0; i < n; i ++)
	{
		scanf("%lf", &cir[i].radius);
		cir[i].id = i;
	}

	sort(cir, cir + n, cmp);

	static Point dir[8] = {
		{1, 0}, {0, 1}, {-1, 0}, {0, -1},
		{1, -1}, {-1, 1}, {1, 1}, {-1, -1}
	};
	for (int rd = 0; ; rd ++)
	{
		double ans = areaCover();
		double step = max(W, L) / 2;
		double factor = 0.9;
		double eps = 1e-6;
		for (int i = 0; i < n; i ++)
		{
			cir[i].center.x = rand() % (int)W;
			cir[i].center.y = rand() % (int)L;
		}
		fprintf(stderr, "round: %d\n", rd);

		while (step > eps)
		{
			ans = areaCover();
			bool found = false;
			for (int i = 0; i < n; i ++)
			{
				for (int j = 0; j < 8; j ++)
				{
					cir[i].center = cir[i].center + dir[j] * step;
					if (!in_range(cir[i].center))
					{
						cir[i].center = cir[i].center - dir[j] * step;
						continue;
					}
					double val = areaCover();
					if (val < ans)
						ans = val, found = true;
					else cir[i].center = cir[i].center - dir[j] * step;
				}
			}
			if (!found)
				step *= factor;
		}
		
		if (areaCover() < 0.000000001)
		{
			fprintf(stderr, "ans=%lf,areaCover()=%lf\n", ans, areaCover());
			break;
		}
	}

	sort(cir, cir + n, cmpId);
	for (int i = 0; i < n; i ++)
		printf("%lf %lf ", cir[i].center.x, cir[i].center.y);
	fprintf(stderr, "ans: %lf\n", areaCover());
	printf("\n");
}

