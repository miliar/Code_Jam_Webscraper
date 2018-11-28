#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std; 

#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FOR2(i, a, b) for (int i = (a); i > (b); --i)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1 << 29;
typedef long long ll;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=last_bit(n); return res; }

template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

const double PI = 3.14159265358979323846264338327950288;

struct Vector
{
	double x, y;
	
	Vector(double a = 0.0, double b = 0.0): x(a), y(b) { }
	Vector(const Vector & v): x(v.x), y(v.y) { }

	Vector & operator=(const Vector & v) { x = v.x; y = v.y; return *this; }
	Vector operator+(const Vector & v) const { return Vector(x + v.x, y + v.y); }
	Vector & operator+=(const Vector & v) { x += v.x; y += v.y; return *this; }
	Vector operator-(const Vector & v) const { return Vector(x - v.x, y - v.y); }
	Vector & operator-=(const Vector & v) { x -= v.x; y -= v.y; return *this; }
	Vector operator*(double n) const { return Vector(x * n, y * n); }
	Vector & operator*=(double n) { x *= n; y *= n; return *this; }
	Vector operator/(double n) const { return Vector(x / n, y / n); }
	Vector & operator/=(double n) { x /= n; y /= n; return *this; }

	bool operator==(const Vector & v) const { return EQ(x, v.x) && EQ(y, v.y); }
	bool operator!=(const Vector & v) const { return !EQ(x, v.x) || !EQ(y, v.y); }
	bool operator<(const Vector & v) const { return x < v.x || (EQ(x, v.x) && y < v.y); }

	double size() const { return sqrt(x*x + y*y); }
	double size2() const { return x*x + y*y; }
	double angle() const { return atan2(y, x); }
};

Vector goats[2];

void Solve(int tc)
{	
	int N, M;
	cin >> N >> M;
	FOR(i, 0, N) cin >> goats[i].x >> goats[i].y;

	printf("Case #%d:", tc);
	FOR(step, 0, M)
	{
		Vector bucket;
		cin >> bucket.x >> bucket.y;

		double r1 = (goats[0]-bucket).size(), r2 = (goats[1]-bucket).size();
		double c = (goats[0]-goats[1]).size();

		double CBD = 2.0 * acos((r2*r2 + c*c - r1*r1) / (2.0*r2*c));
		double CAD = 2.0 * acos((r1*r1 + c*c - r2*r2) / (2.0*r1*c));
		double res = 0.5 * (CBD * r2*r2 - r2*r2*sin(CBD)) + 0.5 * (CAD*r1*r1-r1*r1*sin(CAD));
		printf(" %.9lf", res);
	}
	printf("\n");
}

int main()
{
	int T;
	cin >> T;
	FOR(step, 0, T) Solve(step+1);

	return 0;
}