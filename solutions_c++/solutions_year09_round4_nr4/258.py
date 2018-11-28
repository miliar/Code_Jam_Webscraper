#include <cstdio>
#include <iostream>
#include <sstream>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <queue>

using namespace std;

#define ll long long
#define ld long double
#define mp make_pair
#define pb push_back
#define re return
#define fi first
#define se second
#define sqr(x) (x)*(x)
#define sz(x) (x).size ()
#define all(x) x.begin(), x.end ()
#define fill(x,y) std::memset(x,y,sizeof(x))

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pair<int, int> > vii;
typedef set<int> si;
typedef map<int, int> mii;

template <class T>T abs (T x) { if (x < 0) return -x; else return x; }

const double eps = 1e-9;

vector<pair<double, double> > p;
int x[100], y[100], r[100]; 
int n;

double dist (double x1, double y1, double x2, double y2) {
	return sqrt ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
}

int cross (double x1, double y1, double r1, double x2, double y2, double r2, double *cx1, double *cy1, double *cx2, double *cy2) {
	double d = dist (x1, y1, x2, y2);
	if (d * d > (r1 + r2) * (r1 + r2) + eps) return 0;
	if (d * d < (r1 - r2) * (r1 - r2) - eps) return 0;
	double a = 2 * (x2 - x1);
	double b = 2 * (y2 - y1);
	double c = (x1 * x1 - x2 * x2 + y1 * y1 - y2 * y2 + r2 * r2 - r1 * r1);
	double t = -(x1 * a + y1 * b + c + 0.0) / ((x2 - x1) * a + (y2 - y1) * b);
	double xc = x1 + (x2 - x1) * t;
	double yc = y1 + (y2 - y1) * t;
	double dd = (xc - x1) * (xc - x1) + (yc - y1) * (yc - y1);
	double hh = r1 * r1 - dd;
	if (fabs (hh) < eps) hh = 0;
	double h = sqrt (hh);
	double dx = y1 - y2;
	double dy = x2 - x1;
	double dab = sqrt (dx * dx + dy * dy);
	*cx1 = xc + dx / dab * h;
	*cy1 = yc + dy / dab * h;
	*cx2 = xc - dx / dab * h;
	*cy2 = yc - dy / dab * h;
        return 1;
}


int check (double mr) {
//	printf ("check %.10f\n", mr);
	p.clear ();
	double xc1, yc1, xc2, yc2;
	for (int i = 0; i < n; i++) {
		p.pb (mp (x[i], y[i]));
		for (int j = i + 1; j < n; j++)
			if (cross (x[i], y[i], mr - r[i], x[j], y[j], mr - r[j], &xc1, &yc1, &xc2, &yc2)) {
				p.pb (mp (xc1, yc1));
				p.pb (mp (xc2, yc2));
			}
	}
	for (int i = 0; i < p.size (); i++) 
		for (int j = i + 1; j < p.size (); j++) {
			int ok = 1;
//			printf ("look %.5f %.5f : %.5f %.5f\n", p[i].first, p[i].second, p[j].first, p[j].second);
			for (int k = 0; k < n; k++) {
				double d1 = dist (x[k], y[k], p[i].first, p[i].second);
				double d2 = dist (x[k], y[k], p[j].first, p[j].second);
				if (d1 > mr - r[k] + eps && d2 > mr - r[k] + eps) {
					ok = 0;
					break;
				}
			}
			if (ok) return 1;	
		}
	return 0;
}

int main () {
	int tt;
	scanf ("%d", &tt);
	for (int it = 0; it < tt; it++) {
		double ml = 0, mr = 1e15;
		scanf ("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf ("%d%d%d", &x[i], &y[i], &r[i]);
			if (r[i] > ml) ml = r[i];
		}
		if (n <= 2) {
			printf ("Case #%d: %.10f\n", it + 1, ml);
			continue;
		}
		while (mr - ml > eps) {
			cerr << ml << " " << mr << endl;
			double ms = (ml + mr) / 2;
			if (check (ms)) mr = ms; else ml = ms;
		}
		cerr << "case #" << it + 1 << endl;      
		printf ("Case #%d: %.10f\n", it + 1, (ml + mr) / 2);
	}
}                
