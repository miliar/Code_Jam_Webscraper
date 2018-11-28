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
#define sqr(a)					((a) * (a))
#define cl(x, el)				memset(x, el, sizeof(x))
#define wait					system("pause")
#define Get_Time(time)			(double)((double)(clock() - time) / (double)CLOCKS_PER_SEC)

inline LL strtoint(const string &s) {stringstream ss;ss<<s;LL ret;ss>>ret;return ret;}
inline string inttostr(const LL &a) {stringstream ss;ss<<a;string ret;ss>>ret;return ret;}

const double INF = 1e50;
const double EPS = 1e-9;
const double Pi = acos(- 1.0);
const int MAX = 1 << 28;
const int MIN = - MAX;
const int MAX_N = 1010;



// Vectors Scalar product
// a,b - two vectors
double dot(const Vector &a, const Vector &b)
{
       return real(conj(a) * b);
}

// Vectors Cross product
// a,b - two vectors
double cross(const Vector &a, const Vector &b)
{
       return imag(conj(a) * b);
}

// Returns sqrt( a*a+b*b )
double length(const Vector &a)
{
       return sqrt(dot(a, a));
}

// Rotates the point p around about by radians
point rotate_by(const point &p, const point &about, const double &radians) 
{ 
      return (p - about) * exp(point(0, radians)) + about;
}

// Reflecs p about the line formed by about1 and about2
point reflect(const point &p, const point &about1, const point &about2)
{
      point z = p - about1;
      point w = about2 - about1;
      return conj(z / w) * w + about1;
}

// Returns the 2 times oriented area of a triangle
double area2(const point &a, const point &b, const point &c)
{
       return cross(b - a, c - a);
}

// Reaturns true if the angle <bac is 90 degrees
bool right_angle(const point &a, const point &b, const point &c)
{
     return !dot(b-a,c-a);
}

// Returns the distance between p and ab
double point_line_distance(const point &p, const point &a, const point &b)
{
	return abs(cross(p - a, b - a) / length(b - a));
}

// Returns true if there is an intersection point
// of the segment ab and the segment pq
bool intersects_segments(const point &a, const point &b, const point &p, const point &q)
{
	if( area2(a, b, p) * area2(a, b, q) >= 0.0 ) return false;
	 
	if( area2(p, q, a) * area2(p, q, b) >= 0.0 ) return false;
	
	
	return true;
}





int N, ans;
int h1[MAX_N], h2[MAX_N];






void Read()
{
	scanf("%d", & N);
	
	f(i, N) scanf("%d %d", & h1[i], & h2[i]);
	
//	system("pause");
}

void Solve()
{
	ans = 0;
	
	f(i, N) fo(j, i + 1, N - 1)
	{
	point a(10.0, double(h1[i])), b(100.0, double(h2[i])), p(10.0, double(h1[j])), q(100.0, double(h2[j]));
		
		if(intersects_segments(a, b, p, q)) ans ++;
	}
	
//	system("pause");
}

void Write(const int test_case)
{
	printf("Case #%d: ", test_case);
	
	printf("%d\n", ans);
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
