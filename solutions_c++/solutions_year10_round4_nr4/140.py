#include <iostream>
#include <fstream>
#include <stdio.h>
#include <iomanip>
#include <algorithm>
#include <string>
#include <cctype>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <functional>
#include <stdarg.h>
#include <stdlib.h>
#include <iterator>
#include <math.h>
#include <complex>
#include <numeric>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef complex<double> point;
typedef complex<double> Vector;
typedef pair<point, point> Segment;
typedef pair<int, int> PII;
typedef pair<int, double> PID;
typedef pair<int, string> PIS;
typedef pair<PII, PII> PPII;
typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<point> VP;
typedef vector<VI> VVI;
typedef vector<VD> VVD;
typedef vector<VVI> VVVI;
typedef vector<PII> VPII;
typedef vector<string> VS;

#define f(i, n)					for(int i = 0; i < n; i++)
#define fo(i, a, b)				for(int i = a; i <= b; i++)
#define fx(it, x)				for(typeof((x).begin()) it = (x).begin(); it != (x).end();++it)
#define popcount(n)				__builtin_popcount(n)
#define clz(n)					__builtin_clz(n)
#define ctz(n)					__builtin_ctz(n)
#define gcd(a, b)				__gcd(a, b)
#define lcm(a, b)				((a) / gcd(a, b) * b)
#define nom						first
#define den						second
#define sz(a)					(int(a.size()))
#define pb						push_back
#define all(v)					v.begin(), v.end()
#define EQ(a, b)				(abs((a) - (b)) < EPS)
#define LESS(a, b)				(a + EPS < b)
#define sqr(a)					((a) * (a))
#define cl(x, el)				memset(x, el, sizeof(x))
#define wait					system("pause")
#define Get_Time(time)			(double)((double)(clock() - time) / (double)CLOCKS_PER_SEC)

#define X						real()
#define Y						imag()
#define to_degree(r)			(((r) * 180.0) / (Pi))
#define to_radians(g)			(((g) * Pi) / (180.0))
#define radians(a)				(arg(a) < 0 ? 2 * Pi + arg(a) : arg(a))
#define dot(a, b)				real(conj(a) * (b))
#define cross(a, b)				imag(conj(a) * (b))
#define length(a)				sqrt(dot(a, a))
#define rotate_by(p, a, r)		((p - a) * exp(point(0, r)) + a)
#define reflect(p, a1, a2)		(conj((p - a1) / (a2 - a1)) * (a2 - a1) + a1)
#define area2(a, b, c)			cross(b - a, c - a)
#define right(a, b, c)			EQ(dot(b - a, c - a), 0.0)
#define point_line(p, a, b)		abs(cross(p - a, b - a) / length(b - a))
#define int_seg(a, b, p, q)		(!(area2(a, b, p) * area2(a, b, q) > - EPS) && !(area2(p, q, a) * area2(p, q, b) > - EPS))
#define int_lines(a, b, p, q)	(!EQ(cross(a - b, p - q), 0.0))
#define intersect(a, b, p, q)	((cross(p - a, b - a) * q - cross(q - a, b - a) * p) / (cross(p - a, b - a) - cross(q - a, b - a)))
#define bisector(a, b)			Segment(rotate_by(b, (a + b) * 0.5, pi * 0.5), rotate_by(a, (a + b) * 0.5, pi * 0.5))



inline LL strtoint(const string &s) {stringstream ss;ss<<s;LL ret;ss>>ret;return ret;}
inline string inttostr(const LL &a) {stringstream ss;ss<<a;string ret;ss>>ret;return ret;}

const double INF = 1e50;
const double EPS = 1e-7;
const double Pi = acos(- 1.0);
const int MAX = 1 << 28;
const int MIN = - MAX;
const int MAX_N = 10000;


int N, Q;
double R[MAX_N], ans[MAX_N];
point p[MAX_N], q[MAX_N];









void Read()
{
	cin >> N >> Q;
	
	f(i, N) cin >> p[i].X >> p[i].Y;
	f(i, Q) cin >> q[i].X >> q[i].Y;
	
//	system("pause");
}

int sign(double d)
{
	if(EQ(d, 0.0)) return 0;
	
	if(d < 0.0) return - 1;
	
	return  1;
}

bool inside_rect(point a, point b, point c, point d, point p)
{
	if(sign(area2(a, b, p)) == sign(area2(b, c, p)) && sign(area2(a, b, p)) == sign(area2(c, d, p)) && sign(area2(a, b, p)) == sign(area2(d, a, p))) return true;
	
	return false;
}

double rec(point a, point b, point c, point d)
{
double mid_x = (a.X + b.X) * 0.5, mid_y = (a.Y + d.Y) * 0.5;
double ret = 0.0;
	
//	cout << a << "  " << b << "  " << c << "  "<< d << "\n";
//	system("pause");
	
	
	if((b.X - a.X) * (d.Y - a.Y) < EPS) return 0.0;
	
	f(i, N)
	{
	bool good = false;
		
		if(LESS(length(a - p[i]), R[i])) good = true;
		if(LESS(length(b - p[i]), R[i])) good = true;
		if(LESS(length(c - p[i]), R[i])) good = true;
		if(LESS(length(d - p[i]), R[i])) good = true;
		
		if(inside_rect(a, b, c, d, p[i])) good = true;
		
		if(LESS(point_line(p[i], a, b), R[i]) && a.X <= p[i].X && p[i].X <= b.X) good = true;
		if(LESS(point_line(p[i], b, c), R[i]) && b.Y <= p[i].Y && p[i].Y <= c.Y) good = true;
		if(LESS(point_line(p[i], c, d), R[i]) && d.X <= p[i].X && p[i].X <= c.X) good = true;
		if(LESS(point_line(p[i], d, a), R[i]) && a.Y <= p[i].Y && p[i].Y <= d.Y) good = true;
		
		if(! good) return 0.0;
	}
	
	
	
	f(i, N)
	{
		if(LESS(R[i], length(a - p[i]))) goto next;
		if(LESS(R[i], length(b - p[i]))) goto next;
		if(LESS(R[i], length(c - p[i]))) goto next;
		if(LESS(R[i], length(d - p[i]))) goto next;
	}
	
	return (b.X - a.X) * (d.Y - a.Y);
	
next:
	
	ret += rec(point(a), point(mid_x, b.Y), point(mid_x, mid_y), point(a.X, mid_y));
	ret += rec(point(mid_x, a.Y), point(b), point(b.X, mid_y), point(mid_x, mid_y));
	ret += rec(point(mid_x, mid_y), point(b.X, mid_y), point(c), point(mid_x, c.Y));
	ret += rec(point(a.X, mid_y), point(mid_x, mid_y), point(mid_x, d.Y), point(d));
	
	return ret;
}

double fuck()
{
double d = length(p[0] - p[1]), ret = 0.0;
	
//	cout << p[0] << "  " << p[1] << "\n";
	
//	printf("%.5lf\n", d);
	
	if(EQ(d, R[0] + R[1])) return 0.0;
	
	double alpha = acos((sqr(R[0]) + sqr(d) - sqr(R[1])) / (2.0 * R[0] * d));
	
	alpha *= 2.0;
	
	ret += (alpha / (2.0 * Pi)) * (Pi * sqr(R[0]));
	ret -= sqr(R[0]) * sin(alpha) / 2.0;
	
	
	double beta = acos((sqr(R[1]) + sqr(d) - sqr(R[0])) / (2.0 * R[1] * d));
	
	beta *= 2.0;
	
	ret += (beta / (2.0 * Pi)) * (Pi * sqr(R[1]));
	ret -= sqr(R[1]) * sin(beta) / 2.0;
	
	
	return ret;
}

void Solve()
{
	f(i, Q)
	{
		f(j, N) R[j] = length(p[j] - q[i]);
		
		ans[i] = fuck();
	}
	
//	system("pause");
}

void Write(const int test_case)
{
	printf("Case #%d:", test_case);
	
	f(i, Q) printf(" %.9lf", ans[i]);
	
	printf("\n");
}

int main()
{
int TESTS;
	
	scanf("%d", & TESTS);
	
	for(int i = 1; i <= TESTS; i ++)
	{
		Read();
		
		Solve();
		
		Write(i);
	}
	
//	system("pause");
	
	return 0;
}

/*
1
2 4
0 20
20 0
-20 10
40 20
0 19
10 10 

*/
