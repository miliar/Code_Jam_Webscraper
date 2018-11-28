#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cmath>
#include <list>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b(b);i<_b;++i)
#define FORD(i,a,b) for(int i=(a),_b(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(),a.end()
#define SORT(a) sort(ALL(a))
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
#define SZ(a) ((int) a.size())
#define pb push_back

#define VAR(a,b) __typeof(b) a=(b)
#define FORE(it,a) for(VAR(it,(a).begin());it!=(a).end();it++)
#define X first
#define Y second
#define DEBUG(x) cout << #x << " = " << x << endl;

#define INF 1000000000

typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef pair <int, VI> PIVI;
typedef long long ll;

const double eps = 1e-8;
const double pi = acos (-1.0);

#define sqr(x) ((x)*(x))

inline int cmp(double q, double w = 0, double eps = ::eps) {
    return (q < w + eps) ? (q > w - eps) ? 0 : -1 : 1;
}

struct point {
    double x, y;
    point(double x = 0, double y = 0): x(x), y(y) {}

    point operator + (point q) { return point(x + q.x, y + q.y); }
    point operator - (point q) { return point(x - q.x, y - q.y); }
    point operator * (double t) { return point(x * t, y * t); }
    point operator / (double t) { return point(x / t, y / t); }

    double operator * (point q) { return q.x * x + q.y * y; }
    double operator % (point q) { return x * q.y - y * q.x; }
    
    int cmp(point q) const {
        if (int t = ::cmp(x, q.x)) return t;
        return ::cmp(y, q.y);
    }
    
    bool operator == (point q) { return cmp(q) == 0; }
    bool operator != (point q) { return cmp(q) != 0; }
    bool operator < (point q) { return cmp(q) < 0; }
};

inline double dist(point a, point b) { return hypot(b.x - a.x, b.y - a.y); }

double f, R, t, r, g;

bool inside (double x, double y) {
	return hypot (x, y) <= (R - t - f);
}

bool inside (point p) {
	return hypot (p.x, p.y) <= (R - t - f);
}

double add;

double katsumi (double x, double y) {
	return y < 0 ? -x : x;
}


ostream & operator << (ostream & str, point p) {
	return str << '(' << p.x << ", " << p.y << ')';
}


point a[100];
point b[100];
point hernya[100];

int sza, szb, szhernya;


void see (double xx1, double yy1, double xx2, double yy2) {

	double x1 = xx1 <? xx2;
	double x2 = xx1 >? xx2;
	double y1 = yy1 <? yy2;
	double y2 = yy1 >? yy2;
	
	x1 += f;
	x2 -= f;
	y1 += f;
	y2 -= f;

	sza = 0;
	a[sza++] = point (x1, y1);
	a[sza++] = point (x1, y2);
	a[sza++] = point (x2, y2);
	a[sza++] = point (x2, y1);
	
	int cnt = 0;
	REP (i, sza)
		cnt += inside (a[i]);
	
	if (!cnt)
		return;
		
	if (cnt == 4) {
		add += sqr(g - 2 * f);
		return;
	}
	
	szb = 0;	
	szhernya = 0;
	
	REP (i, sza) {
		if (inside (a[i]))
			b[szb++] = a[i];
		if (inside (a[i]) != inside (a[(i+1) % sza])) {
			if (i == 0) 
				b[szb++] = point (x1, katsumi (sqrt ((R - t - f) * (R - t - f) - x1 * x1), y1));				
			if (i == 2)
				b[szb++] = point (x2, katsumi (sqrt ((R - t - f) * (R - t - f) - x2 * x2), y2));				
				
			if (i == 1) 
				b[szb++] = point (katsumi (sqrt ((R - t - f) * (R - t - f) - y2 * y2), x2), y2);				
			if (i == 3)
				b[szb++] = point (katsumi (sqrt ((R - t - f) * (R - t - f) - y1 * y1), x1), y1);				
		
			hernya[szhernya++] = b[szb-1];		
		}
	}
	
	double sq = 0;

/*cout <<endl;
		cout << xx1 << ' ' << yy1 << ' ' << xx2 << ' ' << yy2 << endl;	
		REP (i, SZ (hernya))
			cout << hernya[i] << ' ';
		cout << endl;
		REP (i, SZ (b))
			cout << b[i] << ' ';
		cout << endl;*/

	REP (i, szb) {
		sq += b[i] % (b[(i+1)%szb]);
	}
	sq = fabs (sq);
	sq /= 2;

	double d = dist (hernya[0], hernya[1]);
	double alfa = acos ((2 * sqr (R - t - f) - d*d) / (2 * sqr (R - t - f)));
//cout << alfa << endl;
	double S = alfa * sqr (R - t - f) / 2 - fabs (hernya[0] % hernya[1]) / 2.0;
	
	sq += S;
	add += sq;
//	cout << sq << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test;
	cin >> test;	
	FOR (ntest, 1, test+1) {		
		cin >> f >> R >> t >> r >> g;
		
		add = 0.0;
		if (2 * f <= g) {
			for (double x = r; x < R; x += 2 * r + g)
				for (double y = r; y < R; y += 2 * r + g)
					for (int signx = -1; signx <= 1; signx += 2)
						for (int signy = -1; signy <= 1; signy += 2)
							see (x * signx, y * signy, (x + g) * signx, (y + g) * signy);
		}
//		cout << (pi * R * R ) << endl;
		printf ("Case #%d: %.8lf\n", ntest, (pi * R * R - add) / (pi * R * R));
	}
	return 0;
}
