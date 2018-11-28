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

#define LESS(a, b)				(a + EPS < b)
#define EQ(a, b)				(fabs(a - b) < EPS)

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
#define sqr(a)					((a) * (a))
#define cl(x, el)				memset(x, el, sizeof(x))
#define wait					system("pause")
#define Get_Time(time)			(double)((double)(clock() - time) / (double)CLOCKS_PER_SEC)

inline LL strtoint(const string &s) {stringstream ss;ss<<s;LL ret;ss>>ret;return ret;}
inline string inttostr(const LL &a) {stringstream ss;ss<<a;string ret;ss>>ret;return ret;}

const double INF = 1e10;
const double EPS = 1e-9;
const double Pi = acos(- 1.0);
const int MAX = 1 << 28;
const int MIN = - MAX;
const int MAX_N = 50;

typedef struct circle
{
	point O;
	double R;
	
	circle(const point & _O = point(), const double & _R = 0.0) : O(_O), R(_R){}
};


int N;
circle c[MAX_N];
VP p;
double ans;


void Read()
{
	cin >> N;
	
	f(i, N) cin >> c[i].O.X >> c[i].O.Y >> c[i].R;
	
//	system("pause");
}

VP circle_circle_intersection(circle a, circle b)
{
double d = length(a.O - b.O), alpha;
point C;
VP ret;
	
	if(LESS(a.R + b.R, d)) return ret;
	
	if(EQ(a.R + b.R, d))
	{
		ret.pb((a.O + b.O) * 0.5);
		
		return ret;
	}
	
	alpha = acos((d * d + a.R * a.R - b.R * b.R) / (2.0 * d * a.R));
//	printf("%.9lf\n", (d * d + a.R * a.R - b.R * b.R) / (2.0 * d * a.R));
//	printf("%.9lf\n", alpha);
//	wait;
	
	C = (b.O - a.O) / d;
	C *= a.R;
	C += a.O;
	
	ret.pb(rotate_by(C, a.O, + alpha));
	ret.pb(rotate_by(C, a.O, - alpha));
	
	return ret;
}

bool ok(const double & R)
{
//	printf("R = %.9lf\n", R);
	
	p.clear();
	
	f(i, N) p.pb(c[i].O);
	
	fo(i, 0, N - 1) fo(j, i + 1, N - 1)
	{
	circle a = c[i], b = c[j];
	VP temp;
		
		a.R = R - a.R;
		b.R = R - b.R;
		
		temp = circle_circle_intersection(a, b);
		
		f(i, sz(temp))
		{
//			cout << temp[i] << "\n";
			
			p.pb(temp[i]);
		}
		
		
	}
	
	f(i, sz(p)) f(j, sz(p)) if(i < j)
	{
	double ok = true;
		
		f(k, N)
		{
		double d1 = length(p[i] - c[k].O) + c[k].R;
		double d2 = length(p[j] - c[k].O) + c[k].R;
			
			if(LESS(R, d1) && LESS(R, d2))
			{
				ok = false;
				
				break;
			}
		}
		
		if(ok) return true;
	}
	
	return false;
}

void Solve()
{
double low = 0.0, mid, high = INF;
	
//	ok(7.1);
	
	for(int iter = 0; iter < 1000; iter ++)
	{
		mid = (low + high) * 0.5;
		
		if(ok(mid)) high = mid;
		else low = mid;
	}
	
	ans = (low + high) * 0.5;
	
//	system("pause");
}

void Write(const int test_case)
{
	printf("Case #%d: ", test_case);
	
	if(N == 1) printf("%.9lf\n", c[0].R);
	else printf("%.9lf\n", ans);
}

int main()
{
int TESTS;
	
	cin >> TESTS;
	
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
5
3
20 10 2
20 20 2
40 10 3
3
20 10 3
30 10 3
40 10 3
5
100 100 1
140 100 1
100 130 1
100 500 1
150 500 1
8
100 100 1
110 100 1
100 110 1
110 110 1
200 200 1
210 200 1
200 210 1
210 210 1
4
100 100 1
200 100 1
200 103 1
300 103 1
*/
