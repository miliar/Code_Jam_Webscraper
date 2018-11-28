#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <utility>
#include <numeric>
#include <fstream>

using namespace std;

#define		ALL(c)	(c).begin(),(c).end()
#define		SZ(c)	int((c).size())
#define		LEN(s)	int((s).length())
#define		FOR(i,n)	for(int i=0;i<(n);++i)
#define		FORD(i,a,b)	for(int i=(a);i<=(b);++i)
#define		FORR(i,a,b)	for(int i=(b);i>=(a);--i)

typedef istringstream iss;
typedef ostringstream oss;
typedef long double ld;
typedef long long i64;
typedef pair<int,int> pii;

typedef vector<i64> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;

typedef vector<ld> vd;
typedef vector<vd> vvd;

typedef vector<string> vs;

const i64 d18 = 1000000000000000000LL;
template<class T> T sqr(T a) { return a * a; }
i64 abs(i64 a) { return (a >= 0) ? a : -a; }

ofstream LOG("log.txt");

ifstream fin;
ofstream fout;

const ld pi = atan2(0.0, -1.0);
const ld inv_pi = 1.0 / pi;
const ld inv_180 = 1.0 / 180.0;
const ld eps = 1e-9;

struct Point
{
	ld x, y;
	Point(): x(0), y(0) {}
	Point(ld _x, ld _y): x(_x), y(_y) {}
	Point(const Point& _p): x(_p.x), y(_p.y) {}
	bool operator==(const Point& r) const { return fabs(x-r.x)<eps && fabs(y-r.y)<eps; }
	bool operator<(const Point& r) const { return x<r.x-eps || fabs(x-r.x)<eps && y<r.y-eps; }
};

Point operator+(const Point& p1, const Point& p2)
{
	return Point(p1.x + p2.x, p1.y + p2.y);
}

Point operator-(const Point& p1, const Point& p2)
{
	return Point(p1.x - p2.x, p1.y - p2.y);
}

Point operator-(const Point& p1)
{
	return Point(-p1.x, -p1.y);
}

Point operator*(const Point& p1, ld a)
{
	return Point(p1.x * a, p1.y * a);
}

Point operator/(const Point& p1, ld a)
{
	if (fabs(a) < eps) return p1;
	return p1 * (1.0 / a);
}

ld dot(const Point& p1, const Point& p2)
{
	return p1.x * p2.x + p1.y * p2.y;
}

ld cross(const Point& p1, const Point& p2)
{
	return p1.x * p2.y - p1.y * p2.x;
}

Point ort_l(const Point& p1)
{
	return Point(-p1.y, p1.x);
}

Point ort_r(const Point& p1)
{
	return -ort_l(p1);
}

Point rotate(const Point& p, const Point& rot)
{
	return Point(p.x * rot.x - p.y * rot.y, p.x * rot.y + p.y * rot.x);
}

// from –pi to pi, if p==0 return 0
ld atan3(const Point& p)
{
	return atan2(p.y, p.x);
}

ld sqrlen(const Point& p)
{
	return p.x * p.x + p.y * p.y;
}

ld len(const Point& p)
{
	return sqrt(sqrlen(p));
}

ld dist(const Point& p1, const Point& p2)
{
	return len(p2 - p1);
}

ld sqrdist(const Point& p1, const Point& p2)
{
	return sqrlen(p2 - p1);
}

Point norm(const Point& p)
{
	if (sqrlen(p) < eps) return p;
	return p / len(p);
}

Point stretch(const Point& p, ld a)
{
	return norm(p) * a;
}

Point rot(ld angle)
{
	return Point(cos(angle), sin(angle));
}

Point rot2(const Point& p1, const Point& p2)
{
	return rot(atan3(p2) - atan3(p1));
}

vector<Point> P, Q;

ld solve(Point q)
{
	ld R0 = dist(q, P[0]);
	ld R1 = dist(q, P[1]);

	ld res = 0;

	Point d0vec = P[1] - P[0];
	Point q0vec = q - P[0];
	ld alpha0 = fabs(atan3(q0vec) - atan3(d0vec));
	if (alpha0 > pi) alpha0 = 2 * pi - alpha0;
	res += R0 * R0 * alpha0;

	Point d1vec = P[0] - P[1];
	Point q1vec = q - P[1];
	ld alpha1 = fabs(atan3(q1vec) - atan3(d1vec));
	if (alpha1 > pi) alpha1 = 2 * pi - alpha1;
	res += R1 * R1 * alpha1;

	res -= fabs(cross(d0vec, q0vec));

	return res;
}

void solve_case(int TN)
{
	int n, m;
	fin >> n >> m;
	P.resize(n);
	FOR(i, n) fin >> P[i].x >> P[i].y;
	Q.resize(m);
	FOR(i, m) fin >> Q[i].x >> Q[i].y;
	
	vd R(m);
	FOR(i, m) R[i] = solve(Q[i]);

	fout << "Case #" << TN << ":";
	cout << "Case #" << TN << ":";
	FOR(i, m)
	{
		fout << fixed << setprecision(8) << " " << R[i];
		cout << fixed << setprecision(8) << " " << R[i];
	}
	fout << endl;
	cout << endl;
}

int main()
{
	fin.open("D.in"); 
	fout.open("D.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}
