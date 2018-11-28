using namespace std;
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <set>
#include <algorithm>
#include <utility>
#include <functional>
#include <numeric>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef istringstream ISS;

#define PB push_back
#define ALL(x) ((x).begin()),((x).end())
#define FOR(i,c) for(typeof(c.begin()) i=c.begin(); i!=c.end(); ++i)
#define REP(i,n) for(int i=0; i<(n); ++i)
#define REPD(i,n) for(int i=(n)-1; i>=0; --i)

#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) printf(__VA_ARGS__)
#else
#define debug(...)
#endif

const int infty = 999999999;

const int dx[8] = { 0, 1, 0,-1, 1, 1,-1,-1};
const int dy[8] = {-1, 0, 1, 0,-1, 1, 1,-1};

typedef double coord;

const double EPS = 1E-8;

const int HIT_INTERSECTS = 1;

const int LINE    = 0;
const int SEGMENT = 1;

class point {
public:
	coord x, y;
  
	point() { x = y = 0; }
	point(coord x1, coord y1) { x = x1; y = y1; }

// BEGIN CUT HERE
	friend ostream &operator <<(ostream &os, point p);

	string str()
	{
		ostringstream res;
		res << *this;
		return res.str();
	}
// END CUT HERE

	point operator +=(point a) { x += a.x; y += a.y; return *this; }
	point operator -=(point a) { x -= a.x; y -= a.y; return *this; }
	point operator *=(coord a) { x *= a;   y *= a;   return *this; }
	point operator /=(coord a) { x /= a;   y /= a;   return *this; }
	int   operator ==(point a) { return x==a.x && y==a.y; }
	int   operator !=(point a) { return x!=a.x || y!=a.y; }
};

point operator *(coord x, point a) { return a *= x; }
point operator *(point a, coord x) { return a *= x; }
point operator /(point a, coord x) { return a /= x; }
point operator +(point a, point b) { return a += b; }
point operator -(point a, point b) { return a -= b; }
coord operator *(point a, point b) { return a.x*b.x + a.y*b.y; }

coord cross(point a, point b) { return a.x*b.y - a.y*b.x; }
double length(point a) { return sqrt((double)(a*a)); }
point perp(point a) { return point(-a.y,a.x); }

class line {
public:
	point p1, p2;

	line() { p1 = p2 = point(); }
	line(point q1, point q2) { p1 = q1; p2 = q2; }

// BEGIN CUT HERE
	friend ostream &operator <<(ostream &os, line l);

	string str()
	{
		ostringstream res;
		res << *this;
		return res.str();
	}
// END CUT HERE

	line operator +=(point a) { p1 += a; p2 += a; return *this; }
	line operator -=(point a) { p1 -= a; p2 -= a; return *this; }
	int  operator ==(line a) { return (p1==a.p1 && p2==a.p2) || (p1==a.p2 && p2==a.p1); }
};

line operator +(line a, point b) { return a += b; }
line operator -(line a, point b) { return a -= b; }

// BEGIN CUT HERE
ostream &operator <<(ostream &os, point p)  { return os << '(' << p.x << ',' << p.y << ')'; }
ostream &operator <<(ostream &os, line l)   { return os << l.p1 << '-' << l.p2; }
// END CUT HERE

point dist(point a, line b, int segment = 0)
{
	point db = b.p2 - b.p1;
	
	if ( segment && ((b.p1-a)*db)*((b.p2-a)*db)>0 ) {
		return length(b.p1-a)<length(b.p2-a) ? b.p1 - a : b.p2 - a;
	}
	
	a -= db*((a-b.p1)*db)/(db*db);
	return b.p1 - a;
}

int equal(line a, line b)
{
	return length(dist(a.p1,b))<EPS && length(dist(a.p1,b))<EPS;
}

int intersect(line a, line b, point *sectpoint, int segment = 0)
{
	// directions of lines
	point da = a.p2 - a.p1;
	point db = b.p2 - b.p1;
	double eps;
	
	if ( length(da)<EPS || length(db)<EPS ) return 0;
	
	// false if lines are parallel
	if ( fabs(cross(da,db)/(length(da)*length(db)))<EPS ) return 0;

	// calc intersection point (need coord to be floating point!)
	*sectpoint = b.p1 + (cross(da,a.p1-b.p1)/cross(da,db))*db;

	// return false if line segments not really cross
	if ( segment ) {
		eps = HIT_INTERSECTS ? +EPS : -EPS;
		if ( cross(da,b.p1-a.p1)*cross(da,b.p2-a.p1)/(da*da)>eps ) return 0;
		if ( cross(db,a.p1-b.p1)*cross(db,a.p2-b.p1)/(db*db)>eps ) return 0;
	}
	
	return 1;
}

double sqr(double x) { return x*x; }

int main()
{
	int run, nruns;
	
	scanf("%d\n",&nruns);
	
	for(run=0; run<nruns; run++) {

		point tr1[3], tr2[3];

		REP(i,3) scanf("%lf %lf",&tr1[i].x,&tr1[i].y);
		REP(i,3) scanf("%lf %lf",&tr2[i].x,&tr2[i].y);

		point curr = (tr1[0] + tr1[1] + tr1[2])/3;
		point orig;

		point u[2], v[2];
		point tmp;

		u[0] = tr1[1]-tr1[0];
		v[0] = tr1[2]-tr1[0];
		tmp = ((v[0]*u[0])/(u[0]*u[0]))*u[0];
		v[0] -= tmp;
		
		u[1] = tr2[1]-tr2[0];
		v[1] = tr2[2]-tr2[0];
		tmp = ((v[1]*u[1])/(u[1]*u[1]))*u[1];
		v[1] -= tmp;
		
		do {
			orig = curr;

			double s = (curr-tr1[0])*u[0]/(u[0]*u[0]);
			double t = (curr-tr1[0])*v[0]/(v[0]*v[0]);

			point test = tr1[0] + s*u[0] + t*v[0];

			curr = tr2[0] + s*u[1] + t*v[1];

//			cout << orig << " -> " << curr << " " << s << "," << t << " " << test << endl;
			
		} while ( length(curr-orig)>1E-8 );

		printf("Case #%d: %.7lf %.7lf\n",run+1,curr.x,curr.y);
	}

	return 0;
}
