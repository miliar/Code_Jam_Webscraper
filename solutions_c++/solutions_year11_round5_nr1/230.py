#pragma comment(linker, "/STACK:512000000")

#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cassert>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define forv(i, v) forn(i, (v).size())
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define all(v) (v).begin(), (v).end()
#define mp make_pair

typedef long long ll;
typedef long double ld;

typedef vector<int> VI;
typedef vector<bool> VB;
typedef pair<int, int> Edge;
typedef vector<vector<Edge> > Graph;

void init()
{
	freopen("input.txt", "rt", stdin);
}

struct Point
{
	int x, y;
};

double hei(const Point& a, const Point& b, double x)
{
	double t = (x - a.x) / (b.x - a.x);
	//a.x + (b.x - a.x) * t == x
	return a.y + (b.y - a.y) * t;
}



double square(const vector<Point>& a, double w)
{
	double result = 0.0;
	forv(i, a) {
		if (i) {
			if (a[i].x <= w) {
				result += (a[i].x - a[i - 1].x) * (a[i].y + a[i - 1].y) * 0.5;
			}
			else {
				double h = hei(a[i - 1], a[i], w);
				result += (w - a[i - 1].x) * (h + a[i - 1].y) * 0.5;
				break;
			}
		}
	}
	return result;
}

double square(const vector<Point>& a, const vector<Point>& b, double w)
{
	return square(b, w) - square(a, w);
}


double shift(const vector<Point>& a, const vector<Point>& b, double s, double w)
{
	double l = 0, r = w;
	forn(it, 50) {
		double m = (l + r) / 2;
		if (square(a, b, m) > s) r = m;
		else l = m;
	}
	return l;
}

int main()
{
	//init();

	int tc; cin >> tc;
	cout.precision(9);
	cout << fixed;
	forn(it, tc) {
		double w, n, m, g;
		cin >> w >> n >> m >> g;
		vector<Point> pa(n), pb(m);
		forn(i, n) cin >> pa[i].x >> pa[i].y;
		forn(i, m) cin >> pb[i].x >> pb[i].y;
		double all = square(pa, pb, w);
		double part = all / g;
		cout << "Case #" << it + 1 << ":" << endl;
		double s = 0;
		forn(i, g - 1) {
			s += part;
			cout << shift(pa, pb, s, w) << endl;
		}
	}

	return 0;
}
