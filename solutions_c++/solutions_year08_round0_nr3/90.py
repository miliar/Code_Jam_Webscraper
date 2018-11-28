//Maked by diver_ru, maked with love^^
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>

#ifdef ONLINE_JUDGE
//#include <iostream>
FILE *fi = stdin, *fo = stdout;
#else
#include <fstream>

//std::ifstream cin("input.txt");
//std::ofstream cout("output.txt");
FILE *fi = fopen("input.txt", "r"), *fo = fopen("output.txt", "w");
#endif
using namespace std;

const double eps = 1e-8;

struct Point{
	double x, y;
	Point(double _x = 0, double _y = 0)
	{
		x = _x, y = _y;
	}
	
	friend Point operator - (const Point &a, const Point &b)
	{
		return (Point(a.x - b.x, a.y - b.y));
	}
};

double answer;
double pi;

double flyRad, outerRad, thickness, stringRad, gapWidth;

double innerRad;

template<typename T> T sqr(T a)
{
	return (a * a);
}

double length(const Point &p)
{
	if (fabs(p.x) < eps)
		return (p.y);
	if (fabs(p.y) < eps)
		return (p.x);
	return (sqrt(sqr(p.x) + sqr(p.y)));
}

void readData()
{
	pi = 4 * atan(1.0);
	fscanf(fi, "%lf%lf%lf%lf%lf", &flyRad, &outerRad, &thickness, &stringRad, &gapWidth);
}

bool pointInsideCircle(Point p)
{
	return (sqr(p.x) + sqr(p.y) <= sqr(innerRad) + eps);
}

bool flyInsideCircle(Point c)
{
	return (sqrt(sqr(c.x) + sqr(c.y)) + flyRad < innerRad + eps);
}

bool findPointInsideHor(const Point &p1, const Point &p2, Point &res)
{
	if (!flyInsideCircle(p1))
		return (false);
	double l = p1.x, r = p2.x;
	while (r - l > eps){
		double k = (r + l) / 2.0;
		if (flyInsideCircle(Point(k, p1.y)))
			l = k;
		else
			r = k;
	}
	res = Point(l, p1.y);
	return (true);
}

bool findPointInsideVert(const Point &p1, const Point &p2, Point &res)
{
	if (!flyInsideCircle(p1))
		return (false);
	double l = p1.y, r = p2.y;
	while (r - l > eps){
		double k = (r + l) / 2.0;
		if (flyInsideCircle(Point(p1.x, k)))
			l = k;
		else
			r = k;
	}
	res = Point(p1.x, l);
	return (true);
}

double processGap(Point p1)
{
	p1 = Point(p1.x + flyRad, p1.y + flyRad);
	if (!flyInsideCircle(p1))
		return (0);
	Point a = p1,
		b = Point(a.x, a.y + gapWidth - flyRad * 2),
		c = Point(a.x + gapWidth - flyRad * 2, a.y + gapWidth - flyRad * 2),
		d = Point(a.x + gapWidth - flyRad * 2, a.y);
	if (flyInsideCircle(c))
		return (sqr(gapWidth - flyRad * 2));
	Point p2, p3, p4, p5;
	findPointInsideVert(a, b, p2);
	findPointInsideHor(a, d, p5);
	if (!findPointInsideHor(b, c, p3))
		p3 = p2;
	if (!findPointInsideVert(d, c, p4))
		p4 = p5;
	double res = (p2.y - p1.y) * (p3.x - p2.x); //rect
	res += (p3.y - p5.y + p4.y - p5.y) * (p4.x - p3.x) / 2.0; //trapec
	double r = innerRad - flyRad, l = length(p4 - p3);
	double height = sqrt(sqr(r) - sqr(l / 2.0));
	res += atan(l / (height * 2.0)) * sqr(r); //sector
	res -= height * l / 2.0; // triangle
	return (res);
}

void solve()
{
	answer = 0;
	if (flyRad * 2 >= gapWidth){
		answer = 1;
		return;
	}
	double fullSquare = sqr(outerRad) * pi / 4.0;
	innerRad = outerRad - thickness;
	int count = (int)floor((innerRad - stringRad) / (gapWidth + 2 * stringRad)) + 2;

	double missSquare = 0;
	for (int i = 0; i < count; ++i)
		for (int j = 0; j < count; ++j)
			missSquare += processGap(Point(stringRad + (stringRad * 2 + gapWidth) * i,
			                         stringRad + (stringRad * 2 + gapWidth) * j));
	answer = 1 - missSquare / fullSquare;
}

void writeResult()
{
	fprintf(fo, "%.6f\n", answer);
}

int main()
{
	int n;
	fscanf(fi, "%d", &n);
	for (int i = 1; i <= n; ++i){
		readData();
		solve();
		fprintf(fo, "Case #%d: ", i);
		writeResult();
	}
	return 0;
}