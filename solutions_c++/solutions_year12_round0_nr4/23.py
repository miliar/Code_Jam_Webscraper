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
const ld eps = 1e-9;
const ld pi = atan2(0.0, -1.0);
template<class T> T sqr(T a) { return a * a; }
i64 abs(i64 a) { return (a >= 0) ? a : -a; }

ofstream LOG("log.txt");

ifstream fin;
ofstream fout;

struct Point
{
	ld x, y;
	Point(): x(0), y(0) {}
	Point(ld _x, ld _y): x(_x), y(_y) {}
	Point(const Point& _p): x(_p.x), y(_p.y) {}
	bool operator==(const Point& r) const { return fabs(x-r.x)<eps && fabs(y-r.y)<eps; }
	bool operator<(const Point& r) const { return x<r.x-eps || fabs(x-r.x)<eps && y<r.y-eps; }
};

struct Lineabc
{
	ld a, b, c;
	Lineabc() {}
	Lineabc(ld _a, ld _b, ld _c): a(_a), b(_b), c(_c) {}
	Lineabc(const Point& p1, const Point& p2)
	{
		a = p1.y - p2.y;
		b = p2.x - p1.x;
		c = -(a * p1.x + b * p1.y);
	}
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


ld dot(const Point& p1, const Point& p2)
{
	return p1.x * p2.x + p1.y * p2.y;
}

ld cross(const Point& p1, const Point& p2)
{
	return p1.x * p2.y - p1.y * p2.x;
}

ld sqrlen(const Point& p)
{
	return dot(p, p);
}

ld len(const Point& p)
{
	return sqrt(dot(p, p));
}

ld sqrdist(const Point& p1, const Point& p2)
{
	return sqrlen(p1-p2);
}

ld dist(const Point& p1, const Point& p2)
{
	return len(p1-p2);
}

int fsgn(ld x)
{
	return x > eps ? 1 : x < -eps ? -1 : 0;
}

bool intersect(const Point& p1, const Point& p2, const Point& q1, const Point& q2)
{
	if (max(p1.x, p2.x) + eps < min(q1.x, q2.x) || min(p1.x, p2.x) > max(q1.x, q2.x) + eps) return false;
	if (max(p1.y, p2.y) + eps < min(q1.y, q2.y) || min(p1.y, p2.y) > max(q1.y, q2.y) + eps) return false;

	ld c1 = cross(p2 - p1, q1 - p1);
	ld c2 = cross(p2 - p1, q2 - p1);

	ld d1 = cross(q2 - q1, p1 - q1);
	ld d2 = cross(q2 - q1, p2 - q1);

	return (fsgn(c1) * fsgn(c2) <= 0 && fsgn(d1) * fsgn(d2) <= 0);
}

// true - intersect in single point
bool inters(const Lineabc& l1, const Lineabc& l2, Point& p)
{
	ld D = -l1.a * l2.b + l1.b * l2.a;
	if (fabs(D) < eps) return false;
	ld Dx = -l1.b * l2.c + l1.c * l2.b;
	ld Dy = l1.a * l2.c - l1.c * l2.a;
	p.x = Dx / D;
	p.y = Dy / D;
	return true;
}

int gcd(int a, int b)
{
	return a == 0 ? b : gcd(b%a, a);
}

void solve_case(int TN)
{
	int n, m, d;
	fin >> n >> m >> d;
	vs H(n);
	int mi = -1, mj = -1;
	FOR(i, n) 
	{
		fin >> H[i];
		FOR(j, m) if (H[i][j] == 'X')
		{
			mi = i, mj = j;
			H[i][j] = '.';
		}
	}
	int ans = 0;
	FORD(di, -d-2, d+2) FORD(dj, -d-2, d+2) if ((di != 0 || dj != 0) && gcd(abs(di),abs(dj)) == 1)
	{
		Point sp(mi + 0.5, mj + 0.5);
		Point sv(50.0 * di, 50.0 * dj);
		ld dst = 0.0;
		bool firstit = true;
		while (dst + eps < d)
		{
			int pi = (int)(sp.x + sv.x * eps);
			int pj = (int)(sp.y + sv.y * eps);

			if (!firstit && pi == mi && pj == mj && fabs(cross(sv, Point(mi+0.5,mj+0.5) - sp)) < eps)
			{
				dst += dist(sp, Point(mi+0.5,mj+0.5));
				if (dst < d + eps) ++ans;
				break;
			}

			firstit = false;

			Point p1, p2, p3;
			if (sv.x >= 0 && sv.y >= 0)
			{
				p1 = Point(pi+1, pj);
				p2 = Point(pi+1, pj+1);
				p3 = Point(pi, pj+1);
			}
			else if (sv.x >= 0 && sv.y <= 0)
			{
				p1 = Point(pi, pj);
				p2 = Point(pi+1, pj);
				p3 = Point(pi+1, pj+1);
			}
			else if (sv.x <= 0 && sv.y >= 0)
			{
				p1 = Point(pi, pj);
				p2 = Point(pi, pj+1);
				p3 = Point(pi+1, pj+1);
			}
			else //if (sv.x <= 0 && sv.y <= 0)
			{
				p1 = Point(pi+1, pj);
				p2 = Point(pi, pj);
				p3 = Point(pi, pj+1);
			}

			bool r1 = intersect(sp, sp+sv, p1, p2);
			bool r2 = intersect(sp, sp+sv, p2, p3);
			Point ip;
			if (r1 && r2)
			{
				inters(Lineabc(sp, sp+sv), Lineabc(p1, p2), ip);
				int si = (int)(ip.x + sv.x * eps);
				int sj = (int)(ip.y + sv.y * eps);
				if (H[si][pj] == '.' && H[pi][sj] == '.' && H[si][sj] == '#') break;
				if (H[si][pj] == '#' && H[pi][sj] == '#' || H[si][sj] == '.')
				{
					dst += dist(sp, ip);
					sp = ip;
					if (H[si][sj] == '#') sv = -sv;
					continue;
				}
			}

			if (r1)
				inters(Lineabc(sp, sp+sv), Lineabc(p1, p2), ip);
			else
				inters(Lineabc(sp, sp+sv), Lineabc(p2, p3), ip);
			dst += dist(sp, ip);
			sp = ip;
			int si = (int)(ip.x + sv.x * eps);
			int sj = (int)(ip.y + sv.y * eps);
			if (H[si][sj] == '.') continue;
			si = (int)(ip.x - sv.x * eps);
			sj = (int)(ip.y + sv.y * eps);
			if (H[si][sj] == '.')
				sv.x = -sv.x;
			else
				sv.y = -sv.y;
		}
	}

	cout << "Case #" << TN << ": " << ans << endl;
	fout << "Case #" << TN << ": " << ans << endl;
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
