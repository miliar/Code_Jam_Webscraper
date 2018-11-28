/*
 * Code by globalpointer
 */

/*
 * BEGIN TEMPLATE
 */

////// Libraries

// I/O
#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>

// Data structures
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>

// Utility
#include <cstdlib>
#include <utility>
#include <cassert>

// Data types
#include <cctype>
#include <climits>

// String utility
#include <cstring>
#include <string>
#include <sstream>

// Algorithm
#include <algorithm>
#include <cmath>

using namespace std;

////// Typedefs
typedef unsigned int 		uint;
typedef long long			ll;
typedef unsigned long long	ull;

////// Constants

// Maths
const double	pi			= acos(-1.0);
const double	eps 		= 1e-9;

// Large values
const int		large_int	= 200000000;
const uint 		large_uint	= 4000000000u;
const ll		large_ll	= 9000000000000000000ll;
const ull		large_ull	= 18000000000000000000ull;
const int       large       = large_int;

////// Utilities

//// Defines
#define SZ(x)               ((int)(x).size())
#define LEN(x)              ((int)(x).length())
#define MP(x,y) 		    (make_pair(x,y))
#define two(x)			    (1 << (x))
#define two_ll(x)		    (1ll << (x))

// Loops
#define FOR(i,n)            for(int (i)=0;(i)<(n);(i)++)
#define FOR_LL(i,n)         for(ll (i)=0ll;(i)<(n);(i)++)
#define FOR_T(t,i,n)        for((t) (i)=((t)0);(i)<((t)(n));(i)++)
#define FOR_SE(i,s,e)       for(int (i)=(s);(i)<(e);(i)++)
#define FOR_LL_SE(i,s,e)    for(ll (i)=(s);(i)<(e);(i)++)
#define FOR_T_SE(t,i,s,e)   for((t) (i)=((t)(s));(i)<((t)(e));(i)++)
#define FOR_ALL(t,i,a)      for((t)::iterator (i)=(a).begin();(i)!=(a).end();(i)++)

//// Bithax
template<class T> bool bitset(T &x, int n) { return x & (((T)1) << n); }
template<class T> void setbit(T &x, int n) { x = x | (((T)1) << n); }
template<class T> void clearbit(T &x, int n)	{ x = x & ~(((T)1) << n); }
template<class T> void togglebit(T &x, int n) { x = x ^ (((T)1) << n); }
template<class T> T    lowestbit(T &x, int n) { return (n^(n-((T)1)))&n; }
template<class T> int  bitcount(T &x) { return x ? (((T)1) + bitcount(x & (x-((T)1)))) : ((T)0); }

//// Maths
template<class T> T sqr(T a) { return a*a; }
template<class T> T gcd(T a, T b) { return (b ? gcd(b, a%b) : a); }
template<class T> T lcm(T a, T b) { return a * (b / gcd(a, b)); }
template<class T> vector<pair<T,int> > decompose(T n) { vector<pair<T,int> > r; int k; for (T d = (T)2; n > (T)1 && d*d <= n; d++) {
    for (k = 0; !(n%d); k++) n /= d; if (k) r.push_back(d, k); } if (n > 1) r.push_back(n, 1); return r; }
template<class T> bool prime(const T &n) { if (n <= (T)1) return false; for (T d = (T)2; d*d <= n; d++)
    if (!(n%d)) return false; return true; }

//// Computation Geometry

// Floating point number comparisons
bool eq(double a, double b) { return abs(a-b) < eps; }
bool ne(double a, double b) { return abs(a-b) >= eps; }
bool lt(double a, double b) { return a <= b-eps; }
bool gt(double a, double b) { return a >= b+eps; }
bool lteq(double a, double b) { return a < b+eps; }
bool gteq(double a, double b) { return a > b-eps; }

// Point
struct P { double x, y; P() : x(0.0), y(0.0) { } P(double x_, double y_) : x(x_), y(y_) { } P(const P &p) : x(p.x), y(p.y) { } };
P operator-(P a, P b) { return P(a.x-b.x, a.y-b.y); }
P operator+(P a, P b) { return P(a.x+b.x, a.y+b.y); }
double operator*(P a, P b) { return a.x*b.x + a.y*b.y; }
double operator^(P a, P b) { return a.x*b.y - a.y*b.x; }
bool operator<(P a, P b) { return (abs(a.x-b.x) < eps) ? (a.y <= b.y-eps) : (a.x <= b.x-eps); }
bool operator==(P a, P b) { return (abs(a.x-b.x) < eps) && (abs(a.y-b.y) < eps); }
double length(P a) { return sqrt(sqr(a.x)+sqr(a.y)); }
double dist(P a, P b) { return length(b-a); }

// Vector comparisons
bool left_turn(P a, P b, P c) { return ((b-a)^(c-b)) >= eps; }
bool right_turn(P a, P b, P c) { return ((b-a)^(c-b)) <= -eps; }
bool collinear(P a, P b, P c) { return abs((b-a)^(c-b)) < eps; }

// Area
double area(P a, P b, P c) { return 0.5 * abs((a^b)+(b^c)+(c^a)); }
double area(vector<P> f) { if (SZ(f) < 3) return 0.0; double sum = 0.0; FOR(i,SZ(f)-1)
    sum += (f[i] ^ f[i+1]); sum += (f[f.size()-1] ^ f[0]); return 0.5 * abs(sum);  }

// Intersections
//P intersection(P a, P b) { }
//bool intersects(P a, P b) { }
bool point_in_line(P a, P b, P p) { if (!collinear(a, b, p)) return false; P u = a-p; P v = b-p; return ((u.x*v.x) <= 0) && ((u.y*v.y) <= 0); }
bool point_in_polygon(P p, vector<P> f) { int c = 0; for (int i = 0; i < SZ(f); i++) { P a = f[i], b = (i == SZ(f)-1) ? f[0] : f[i+1];
    if (a == p || point_in_line(a, b, p)) return true; if ((a.y <= p.y) && (b.y > p.y) && left_turn(a, b, p)) c++;
    if ((a.y > p.y) && (b.y <= p.y) && right_turn(a, b, p)) c--; } return c != 0; }
// vector<P> convex_hull(vector<P> f) { }

//// EVIL
//#define EVIL
#ifdef EVIL
# define if(x) while(x)
# define true false
#endif

/*
 * END TEMPLATE
 */

#define c_io
//#define cpp_io

#if defined c_io
    FILE *in = fopen("B.in", "r");
    FILE *out = fopen("B.out", "w");
    int input_test_cases() { int tmp; fscanf(in, "%d ", &tmp); return tmp; }
    void output_test_case_num(int test_id) { fprintf(out, "Case #%d: ", test_id); }
    void output_test_case_end() { fprintf(out, "\n"); }
#elif defined cpp_io
    ifstream in("B.in");
    ofstream out("B.out");
    int input_test_cases() { int tmp; in >> tmp; return tmp;}
    void output_test_case_num(int test_id) { out << "Case #" << test_id << ": "; }
    void output_test_case_end() { out << "\n"; }
#endif

int max_b;
int speed;
int stars;
int rep;
int d[1000010]; // d[i] = Distance from star i to star i+1
int best[2][1000010];

int main()
{
    int test_cases;
    test_cases = input_test_cases();
    for (int test_id = 1; test_id <= test_cases; test_id++)
    {
        for (int i = 0; i < 1000010; i++)
            best[0][i] = best[1][i] = large;
        best[0][0] = 0;
        fscanf(in, "%d%d%d%d", &max_b, &speed, &stars, &rep);
        for (int i = 0; i < rep; i++) {
            fscanf(in, "%d", &d[i]);
            d[i] *= 2;
        }
        for (int i = rep; i < stars; i++)
            d[i] = d[i-rep];
        
        speed *= 2;
        
        for (int i = 1; i <= stars; i++) {
            int cur = i%2;
            int prev = (i+1)%2;
            
            best[cur][0] = best[prev][0] + (d[i-1]*2);
            for (int b = 1; b <= max_b; b++) {
                int use_b;
                if (best[prev][b-1] >= speed) {
                    use_b = best[prev][b-1] + d[i-1];
                } else if(best[prev][b-1] + (d[i-1]*2) <= speed) {
                    use_b = large;
                } else {
                    int foo = speed - best[prev][b-1];
                    assert ((foo % 2) == 0);
                    use_b = best[prev][b-1] + foo +
                        (d[i-1] - (foo/2));
                }
                best[cur][b] = min(best[prev][b] + (d[i-1]*2),
                                   use_b);
            }
        }
        
        int answer = large;
        for (int i = 0; i <= max_b; i++)
            answer = min(best[(stars)%2][i], answer);
    
        output_test_case_num(test_id);
        fprintf(out, "%d", answer/2);
        output_test_case_end();
    }
    
	return 0;
}
