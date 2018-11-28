#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <functional>
#include <iomanip>
#include <cassert>

#define _USE_MATH_DEFINES
#include <cmath>

using namespace std;

typedef vector<int> VI; typedef vector<int>::iterator VII;
typedef list<int> LI; typedef list<int>::iterator LII;
typedef set<int> SI; typedef set<int>::iterator SII;

typedef vector<string> VS; typedef vector<string>::iterator VSI;
typedef list<string> LS; typedef list<string>::iterator LSI;
typedef set<string> SS; typedef set<string>::iterator SSI;

typedef vector<double> VD; typedef vector<double>::iterator VDI;
typedef list<double> LD; typedef list<double>::iterator LDI;
typedef set<double> SD; typedef set<double>::iterator SDI;

#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define All(c) (c).begin(), (c).end()

double EPS= 1e-9;
template<typename T> inline T sqr(T a) { return a*a; }
inline bool deq(double a, double b) { return (a > b-EPS) && (a < b+EPS); }
inline bool dless(double a, double b) { return !deq(a,b) && (a < b); }
inline bool dmore(double a, double b) { return !deq(a,b) && (a > b); }

struct Point
{
  Point() : x(0.), y(0.) {}
  Point(double x, double y) : x(x), y(y) {}
  inline bool operator==(const Point& p) { return (x==p.x) && (y==p.y); }
  inline Point operator+(const Point& p) { return Point(x+p.x, y+p.y); }
  inline Point operator-(const Point& p) { return Point(x-p.x, y-p.y); }
  static inline bool lessX(const Point& p1, const Point& p2) { return p1.x < p2.x; }
  static inline bool lessY(const Point& p1, const Point& p2) { return p1.y < p2.y; }
  inline double dist(const Point& p) { return sqrt(sqr(p.x-x)+sqr(p.y-y)); }
  inline double mod_vect() { return sqrt(sqr(x)+sqr(y)); }
  double x, y;
};
struct Point3D
{
  Point3D() : x(0.), y(0.), z(0) {}
  Point3D(double x, double y, double z) : x(x), y(y), z(z) {}
  bool operator==(const Point3D& p) { return (x==p.x) && (y==p.y) && (z==p.z); }
  Point3D operator+(const Point3D& p) { return Point3D(x+p.x, y+p.y, z+p.z); }
  Point3D operator-(const Point3D& p) { return Point3D(x-p.x, y-p.y, z-p.z); }
  double x, y, z;
};
double chord_area(double r, const Point &p1, const Point &p2)
{
  double c = sqrt(sqr(p2.x-p1.x) + sqr(p2.y-p1.y)) / 2;
  double res = sqr(r) * asin(c/r) - c*(sqrt(sqr(r)-sqr(c)));
  return res;
}
double asin2(double x) {
	double res = asin(max(-1.0, min(1.0, x)));
	assert(-M_PI_2 <= res && res <= M_PI_2);
	return res;
}

struct Sym
{
  Sym(int p, int index) :p(p), index(index), ord(0) {}
  bool operator <(const Sym& s) { return p>s.p; };
  int p;
  int index;
  int ord;
};

int main(size_t argc, const char * argv[])
{
  if (1 == argc)
    return -1;

  ifstream is(argv[1]);
  ofstream os("data.out");

  int T;
  is >> T; is.ignore();

  For(t, 1, T)
  {
    int P,K,L;
    is >> P >> K >> L; is.ignore();
    vector<Sym> r;
    Rep(i,L)
    {
      int v; is >> v; r.push_back(Sym(v,i));
    }
    is.ignore();

    os << "Case #" << t << ": ";

    if (P*K<L)
      os << "Impossible";
    else
    {
      sort(All(r));
      For(p,1,P)
        Rep(k,K)
          For(i,(p-1)*K, min(p*K-1,L-1))
            r[i].ord=p;

      int s(0);
      Rep(l,L)
        s+= r[l].ord*r[l].p;

      os << s;
    }

    os.flags(os.flags() | os.fixed);
    os << setprecision(6);
    os << endl;
  }

  return 0;
}
