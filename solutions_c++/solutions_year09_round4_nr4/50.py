#include <iomanip>
#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
#include <cassert>
#include <bitset>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cout << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<tint> vt;
typedef vector<vt> vvt;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

const double EPS = 1e-9;

struct point {
	double x,y;
};

point operator-(const point& p1, const point& p2) {
	return (point){p1.x-p2.x,p1.y-p2.y};
}

point operator+(const point& p1, const point& p2) {
	return (point){p1.x+p2.x,p1.y+p2.y};
}

double operator*(const point& p1, const point& p2) {
	return p1.x*p2.x + p1.y*p2.y;
}

ostream& operator<< (ostream& out, const point& p) {
	out << '(' << p.x << ',' << p.y << ')';
	return out;
}

point mulcomp(const point& p1, const point& p2) {
	return (point){p1.x*p2.x - p1.y*p2.y, p1.x*p2.y + p1.y*p2.x};
}

bool posible(double a, double b, double c) { return a+b >= c + EPS && fabs(a-b) <= c - EPS; }

point atdist(double a, double b) {
	double x = (a*a - b*b + 1) / 2.0;
	double y = sqrt(a*a - x*x);
	return (point){x,y};
}

pair<point,point> atdist(const point& p1, const point& p2, double a, double b) {
	point v = p2-p1;
	double d = sqrt(v*v);
	point rot = atdist(a/d,b/d);
	pair<point,point> res;
	res.first = p1 + mulcomp(v,rot);
	rot.y = -rot.y;
	res.second = p1 + mulcomp(v,rot);
	return res;
}

double dist(const point& p1, const point& p2) {
	point v = p1-p2;
	return sqrt(v*v);
}

#define MAXN 50
int n,x[MAXN],y[MAXN], r[MAXN];
tint ALL;


bool pos(double R) {
	vector<point> center;

	forn(j,n) {
		point b = (point){x[j],y[j]};
		center.pb(b);
		forn(i,j) {
			point a = (point){x[i],y[i]};
			if (!posible(R-r[i],R-r[j],dist(a,b))) continue;
			pair<point,point> c = atdist(a,b,R-r[i],R-r[j]);
			center.pb(c.first); center.pb(c.second);
		}
	}


	vector<tint> mask;
	forall(it,center) {
		point c = *it;
		mask.pb(0);
		forn(i,n) {
			point p = (point){x[i],y[i]};
			if (dist(c,p) + r[i] < R + EPS) mask.back() |= 1LL << i;
		}
	}

	int m = si(mask);
	forn(j,m) forn(i,j+1) if ((mask[i] | mask[j]) == ALL) return true;
	return false;
}



int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	cout << fixed << setprecision(8);
	int ncas; cin >> ncas;
	forsn(cas,1,ncas+1) {
		cin >> n;
		ALL = (1LL << n) - 1;
		forn(i,n) cin >> x[i] >> y[i] >> r[i];


		double lo = 0, hi = 1e6;
		while (fabs(lo-hi) > EPS) {
			double mi = (lo + hi) / 2;
			if (pos(mi)) hi = mi;
			else lo = mi;
		}

		cout << "Case #" << cas << ": " << lo << endl;
	}
}
