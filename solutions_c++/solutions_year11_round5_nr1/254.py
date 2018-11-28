#include <algorithm>
#include <iostream>
#include <sstream>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstring>

#define sz(a) (int)a.size()
#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()
#define llong long long
#define zero(a) fabs(a) < 1e-9
#define resz(a, n) a.clear(), a.resize(n)
#define same(a, n) memset(a, n, sizeof(a))
#define make(a, b) make_pair(a, b)
#define x first
#define y second

const double eps = 1e-11;
const double inf = 10000000;

using namespace std;

int w, loc, hic, m;
vector< pair< double, double > > lop, hip;

double mem[10000];

void clear(){
	lop.clear();
	hip.clear();
	for (int i = 0; i < 10000; ++i)
		mem[i] = -1;
}

double cut(vector< pair< double, double > > &p, double x) {
	if (x < 0 || x > w)
		return -1;
	int k = lower_bound(all(p), make(x + eps, -inf)) - p.begin();
	k = k - 1;
	double A = p[k + 1].y - p[k].y;
	double B = p[k].x - p[k + 1].x;
	double C = A * p[k].x + B * p[k].y;
	double y = (C - A * x) / B;
	return y;
}

double dst(pair< double, double > a, pair< double, double > b ){
	return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

double tri(pair< double, double > p1, pair< double, double > p2, pair< double, double > p3 ){
	double a = dst(p1, p2);
	double b = dst(p2, p3);
	double c = dst(p3, p1);
	double s = (a + b + c) / 2.0;
	double sol = sqrt(s * (s - a) * (s - b) * (s - c));
	return sol;
}

int main(){
	int tests;
	scanf("%d", &tests);
	for (int t = 1; t <= tests; t++) {
		clear();
		vector< int > pos;
		scanf("%d %d %d %d", &w, &loc, &hic, &m);
		for (int i = 0; i < loc; ++i) {
			int a, b;
			scanf("%d %d",&a,&b);
			lop.push_back(make(a, b));
			pos.push_back(a);
		}
		for (int i = 0; i < hic; ++i) {
			int a, b;
			scanf("%d %d", &a, &b);
			hip.push_back(make(a, b));
			pos.push_back(a);
		}
		sort(all(pos));
		pos.erase(unique(all(pos)), pos.end());
		double ta = 0;
		for (int i = 0; i < sz(pos) - 1; ++i) {
			double cx = pos[i];
			double _y0 = cut(lop, pos[i + 1]);
			double _y1 = cut(hip, pos[i + 1]);
			double y0 = cut(lop, cx);
			double y1 = cut(hip, cx);
			ta += tri(pair< double, double >(cx, y0), pair< double, double >(cx, y1), pair< double, double >(pos[i + 1], _y0));
			ta += tri(pair< double, double >(cx, y1), pair< double, double >(pos[i + 1], _y0), pair< double, double >(pos[i + 1], _y1));
		}
		double AM = ta / m;
		printf("Case #%d:\n", t);
		double A = 0;
		double cx = 0;
		int cnt = 0;
		for (int i = 1; i < sz(pos); ++i) {
			double _y0 = cut(lop, pos[i]);
			double _y1 = cut(hip, pos[i]);
			double y0 = cut(lop, cx);
			double y1 = cut(hip, cx);
			double a = tri(pair< double, double >(cx, y0), pair< double, double >(cx, y1), pair< double, double >(pos[i], _y1));
			a += tri(pair< double, double >(cx, y1), pair< double, double >(pos[i], _y0), pair< double, double >(pos[i], _y1));
			A += a;
			if (A + eps >= AM) {
				A -= a;
				double lo = cx, hi = pos[i];
				double nx = cx;
				for (int k = 0; k < 100; ++k) {
					double mx = (hi + lo) / 2;
					double _y0 = cut(lop, mx);
					double _y1 = cut(hip, mx);
					a = tri(pair< double, double >(cx, y0), pair< double, double >(cx, y1), pair< double, double >(mx, _y0));
					a += tri(pair< double, double >(cx, y1), pair< double, double >(mx, _y0), pair< double, double >(mx, _y1));
					if (A + a <= AM - eps)
						lo = mx + eps, nx = mx;
					else
						hi = mx - eps;
				}
				if (cnt != m - 1)
					printf("%.10lf\n",nx);
				cnt++;
				A = 0, cx = nx;
				i--;
			}
			else cx = pos[i];
		}
	}
	return 0;
}
