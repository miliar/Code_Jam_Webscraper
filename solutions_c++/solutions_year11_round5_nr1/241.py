#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <set>
#include <algorithm>
#include <queue>
#include <cassert>
#include <fstream>
#include <sstream>
#include <bitset>
#include <stack>
#include <list>
using namespace std;
#define debug1(x) cout << #x" = " << x << endl;
#define debug2(x, y) cout << #x" = " << x << " " << #y" = " << y << endl;
#define debug3(x, y, z) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << endl;
#define debug4(x, y, z, w) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << " " << #w" = " << w << endl;

template <class T>
ostream & operator << (ostream & out, const vector<T> & t)
{	out << t.size() << " {";	for (int i = 0; i < t.size(); ++i) 		out << t[i] << " ";	out << "}";	return out;}

template <class T>
ostream & operator << (ostream & out, const set<T> & t)
{	out << "{";	for (set<T>::iterator itr = t.begin(); itr != t.end(); ++itr)		out << *itr << " ";	out << "}";	return out;}

/////////////////////////
// template finished
/////////////////////////
int T, testid;

struct Point
{
	double x, y;
};

double W;
vector<Point> lower;
vector<Point> upper;
double G;
int L, U;
const double eps = 1e-8;

double getArea(double x, vector<Point> & ps)
{
	double lastx = ps[0].x;
	double lasty = ps[0].y;
	double ret = 0;
	for (int i = 1; i < ps.size(); ++i)
	{
		double nowx = ps[i].x;
		double nowy = ps[i].y;
		if (x <= nowx + eps)
		{
			double yy = lasty + (nowy - lasty) / (nowx - lastx) * (x - lastx);
			ret += (lasty + yy) * (x - lastx) / 2;
			break;
		}
		ret += (nowy + lasty) * (nowx - lastx) / 2;
		lastx = nowx;
		lasty = nowy;
	}

	return ret;
}

void init()
{
	cin >> W >> L >> U >> G;
	lower.resize(L);
	upper.resize(U);
	for (int i = 0; i < L; ++i)
		cin >> lower[i].x >> lower[i].y;
	for (int i = 0; i < U; ++i)
		cin >> upper[i].x >> upper[i].y;
}

void york()
{
	printf("\n");
	double areaupper = getArea(W, upper);
	double arealower = getArea(W, lower);
	double area = areaupper - arealower;
	double smallarea = area / G;
	//debug1(area);
//	debug1(getArea(5, upper) - getArea(5, lower));
	for (int i = 1; i < G; ++i)
	{
		double tararea = area / G * i;
	//	debug2(i, tararea);
		double l = 0;
		double r = W;
		while (l < r - eps)
		{
			double mid = (l + r) / 2;
			double nowarea = getArea(mid, upper) - getArea(mid, lower);
			if (nowarea > tararea) 
				r = mid;
			else 
				l = mid;
		}
		printf("%.10f\n", l);
	}
}

int main()
{
	cin >> T;
	for (testid = 1; testid <= T; ++testid)
	{
		printf("Case #%d: ", testid);
		init();
		york();
	}
	return 0;
}