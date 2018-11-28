// Compiler : MS VC++ 8.0
// input  file : data.in
// output file : data.out

#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <iomanip>
#include <iostream>
#include <cassert>
#include <fstream>

using namespace std;
typedef long long lint;
typedef vector<int> VI; typedef vector<VI> VVI;
typedef vector<lint> VL; typedef vector<VL> VVL;
typedef vector<double> VD; typedef vector<VD> VVD;
typedef vector<string> VS;
#define SIZE(c) ((int)(c).size())
#define SEQ(c) (c).begin(),(c).end()
#define FOR(i,a,b) for(int _U(b),i=(a);i<_U;++i)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int _U(a),i=(b)-1;i>=_U;--i)
#define FORS(i,c) FOR(i,0,SIZE(c))
#define REPD(i,n) FORD(i,0,n)
template<class T>string tostr(T v){ostringstream o;o<<v;return o.str();}
string tostrdouble(double v) {ostringstream o;o<<fixed<<setprecision(7)<<v; return o.str();}
#define UNIQUE(c) {sort(SEQ(c)); (c).erase(unique(SEQ(c)),(c).end());}
typedef pair<int,int> PII;
#define MIN(A,B) if ((B)<(A)) (A)=(B)
#define MAX(A,B) if ((B)>(A)) (A)=(B)
const int inf = 1000100100;
const double Pi = acos(-1.);
///////////////////////////////////////////////////////////////////////////////////
template <class T>
vector<T> splitString(string s, string sep = " ") {
  vector<T> ret;
  int pos = -1, posPrev = -2;
  do {
    posPrev = pos;
    pos = (int)s.find_first_of(sep, posPrev+1);
    if (pos == -1) pos = (int)s.size();
    if (pos-posPrev > 1) {
      istringstream is(s.substr(posPrev+1,pos-posPrev-1));
      T v; is >> v; ret.push_back(v);
    }
  } while (posPrev < (int)s.size());
  return ret;
}
///////////////////////////////////////////////////////////////////////////////////
string caseNo(int i) {return "Case #" + tostr(i) + ":";}

///////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////

typedef double Coord;
const Coord Eps = 1e-12;
int czero(Coord v) {if (v<-Eps) return -1; if (v>Eps) return 1; return 0;}

struct Vec {
  Coord x, y;
  explicit Vec(Coord _x=0, Coord _y=0) : x(_x), y(_y) {}
};
typedef Vec Point;

Vec operator+ (const Vec& v0, const Vec& v1) {return Vec(v0.x+v1.x,v0.y+v1.y);}
Vec operator- (const Vec& v0, const Vec& v1) {return Vec(v0.x-v1.x,v0.y-v1.y);}
Coord operator* (const Vec& v0, const Vec& v1) {return v0.x*v1.x+v0.y*v1.y;}
Coord operator^ (const Vec& v0, const Vec& v1) {return v0.x*v1.y-v0.y*v1.x;}
Vec operator* (const Vec& v, const Coord& sc) {return Vec(v.x*sc, v.y*sc);}

Coord length2(const Vec& v){return v.x*v.x+v.y*v.y;}
Coord length(const Vec& v) {return sqrt(v.x*v.x+v.y*v.y);}

///////////////////////////////////////////////////////////////////////////////////

double areaSlice(const Point& a, const Point& b, double r2) {
  double len = length(a-b);
  double cos_ang = (2*r2 - len*len) / (2*r2);
  double ang = acos(cos_ang);
  double ret = Pi * r2 * ang / (2*Pi);
  ret -= abs(a^b)/2.;
  return ret;
}

double areaPoly(const vector<Point>& vec) {
  int k = SIZE(vec);
  assert(3 <= k && k <= 5);
  double ret = 0;
  FORS (i,vec) {
    double cur = vec[i]^vec[(i+1)%k];
    ret += cur;
  }
  ret = abs(ret)/2.;
  return ret;
}

double getIntersect(double r2, double x) {
  double ret = sqrt(r2 - x*x);
  return ret;
}

vector<Point> poly;

double intersectArea(const Point& mn, const Point& mx, double r) {
  double r2 = r*r;
  if (length2(mn) >= r2) return 0.;
  double dx = mx.x - mn.x;
  double dy = mx.y - mn.y;
  assert(czero(dx-dy) == 0);
  if (length2(mx) <= r2) return dx*dy;

  double y_xmn = getIntersect(r2, mn.x);
  double x_ymn = getIntersect(r2, mn.y);

  poly.clear();
  Point p1, p2;

  if (y_xmn < mx.y)
    if (x_ymn < mx.x) { // a
      p1 = Point(mn.x, y_xmn);
      p2 = Point(x_ymn, mn.y);
      poly.push_back(mn);
    } else // b
    {
      double y_xmx = getIntersect(r2, mx.x);
      p1 = Point(mn.x, y_xmn);
      p2 = Point(mx.x, y_xmx);
      poly.push_back(Point(mx.x, mn.y));
      poly.push_back(mn);
    }
  else 
    if (x_ymn < mx.x) // c
    {
      double x_ymx = getIntersect(r2, mx.y);
      p1 = Point(x_ymx, mx.y);
      p2 = Point(x_ymn, mn.y);
      poly.push_back(mn);
      poly.push_back(Point(mn.x, mx.y));
    }
    else 
    {
      double x_ymx = getIntersect(r2, mx.y);
      double y_xmx = getIntersect(r2, mx.x);
      p1 = Point(x_ymx, mx.y);
      p2 = Point(mx.x, y_xmx);
      poly.push_back(Point(mx.x, mn.y));
      poly.push_back(mn);
      poly.push_back(Point(mn.x, mx.y));
    }

    poly.push_back(p1);
    poly.push_back(p2);
    double ret = areaPoly(poly);
    ret += areaSlice(p1, p2, r2);
    return ret;
}

double f, R, t, r, g;

double solve() {
  double Rin = R-t;
  if (Rin <= f) return 1.; // too small inside inner radius
  if (g <= 2*f) return 1.; // no space between strings

  Rin -= f;
  r += f;
  g -= 2*f;

  double areaAll = Pi * R * R;
  double areaLost = 0.;

  double xmin = r, xmax = r + g;
  while (xmin < Rin) {
    double ymin = r, ymax = r + g;
    double sq;
    do {
      sq = intersectArea(Point(xmin,ymin), Point(xmax,ymax), Rin);
      areaLost += sq;
      ymin = ymax + 2*r;
      ymax = ymin + g;
    } while (sq > 0);
    xmin = xmax + 2*r;
    xmax = xmin + g;
  }

  areaLost *= 4;

  double ret = 1. - areaLost / areaAll;
  return ret;
}

void main()
{
  ifstream ifs("data.in");
  ofstream ofs("data.out");
  int ntests;
  ifs >> ntests;
  getline(ifs,string());
  FOR (test,1,ntests+1) {
    ofs << caseNo(test);
    cout << caseNo(test) << endl;
    //-------------------------------------------------------------
    ifs >> f >> R >> t >> r >> g;
    double ret = solve();
    ofs << " " << setprecision(9) << ret;
	  //-------------------------------------------------------------
    ofs << endl;
  }
}
