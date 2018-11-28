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
#include <algorithm>
using namespace std; 

#define DEBUG(x) fout << '>' << #x << ':' << x << endl;
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FOR2(i, a, b) for (int i = (a); i > (b); --i)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }
const int INF = 1 << 29;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
#ifdef WIN32
typedef __int64 ll;
#else
typedef long long ll;
#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////// 

FILE *fin  = fopen ("input.in", "r");
FILE *fout = fopen ("output.out", "w");

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

inline double dot_product(const Vector & v1, const Vector & v2) { return v1.x * v2.x + v1.y * v2.y; }
inline double cross_product(const Vector & v1, const Vector & v2) { return v1.x * v2.y - v1.y * v2.x; }
inline double angle(const Vector & v1, const Vector & v2)
{
	return acos(fabs(dot_product(v1, v2)) / (v1.size() * v2.size()));
}

double count_area(const vector<Vector> & polygon)
{
	double res = 0.0;
	FOR(i, 0, polygon.size())
		res += cross_product(polygon[i], polygon[(i+1) % polygon.size()]);
	return fabs(res) / 2.0;
}

double count_area(Vector p1, Vector p2, double r)
{
	double alpha = angle(p1, p2);
	return r*r*(alpha-sin(alpha)) / 2.0;
}

int main()
{
	int T;
	fscanf(fin, "%d", &T);

	FOR(step, 0, T)
	{
		double f, R, t, r, g;
		fscanf(fin, "%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);

		double res = 0.0;

		double radius = R-t-f;
		double left = r+f, right=r+g-f;
		while (left < radius)
		{
			double bottom = r+f, top = r+g-f;
			double left_height = sqrt(radius*radius - left*left), right_height = sqrt(max(0.0, radius*radius - right*right));
			while (bottom < left_height)
			{
				//cely je vo vnutri
				if (top < right_height)
				{
					res += (g - 2.0*f) * (g - 2.0*f);
				}
				//len pravy horny roh chyba
				else if (top < left_height && right_height < top && bottom < right_height)
				{
					Vector p1(sqrt(radius*radius - top*top), top), p2(right, sqrt(radius*radius - right*right));
					vector<Vector> polygon;
					polygon.push_back(Vector(left, bottom));
					polygon.push_back(Vector(left, top));
					polygon.push_back(p1);
					polygon.push_back(p2);
					polygon.push_back(Vector(right, bottom));
					res += count_area(polygon) + count_area(p1, p2, radius);
				}
				//prava strana
				else if (top < left_height && right_height < bottom)
				{
					Vector p1(sqrt(radius*radius - top*top), top), p2(sqrt(radius*radius - bottom*bottom), bottom);
					vector<Vector> polygon;
					polygon.push_back(Vector(left, bottom));
					polygon.push_back(Vector(left, top));
					polygon.push_back(p1);
					polygon.push_back(p2);
					res += count_area(polygon) + count_area(p1, p2, radius);
				}
				//horna strana
				else if (left_height < top && bottom < right_height)
				{
					Vector p1(left, sqrt(radius*radius - left*left)), p2(right, sqrt(radius*radius - right*right));
					vector<Vector> polygon;
					polygon.push_back(Vector(left, bottom));
					polygon.push_back(p1);
					polygon.push_back(p2);
					polygon.push_back(Vector(right, bottom));
					res += count_area(polygon) + count_area(p1, p2, radius);
				}
				//ostal len levy dolny roh
				else if (bottom < left_height)
				{
					Vector p1(left, sqrt(radius*radius - left*left)), p2(sqrt(radius*radius - bottom*bottom), bottom);
					vector<Vector> polygon;
					polygon.push_back(Vector(left, bottom));
					polygon.push_back(p1);
					polygon.push_back(p2);
					res += count_area(polygon) + count_area(p1, p2, radius);
				}

				bottom += g+2.0*r;
				top += g+2.0*r;
			}

			left += g+2.0*r;
			right += g+2.0*r;
		}
		
		fprintf(fout, "Case #%d: %.6lf\n", step+1, 1.0 - res * 4.0 / (3.1415926535897932384626 * R * R));
	}

	return 0;
}
