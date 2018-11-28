#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <functional>
#include <sstream>
#include <iostream>
#include <ctime>
#include <algorithm>
using namespace std;

#define DEBUG(x...) printf(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define _foreach(it, b, e) for(__typeof__(b) it = (b); it != (e); ++it)
#define foreach(x...) _foreach(x)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll; // sao dois L's!!!
const double eps = 1e-9;

inline int cmp(double x, double y = 0)
{ return (x < y + eps) ? (x + eps < y) ? -1 : 0 : 1; }

struct point
{
  double x, y;
  point(double x=0, double y=0) : x(x), y(y) {}
  inline point operator-(const point &p) const {return point(x-p.x, y-p.y);}
  inline point operator+(const point &p) const {return point(x+p.x, y+p.y);}
  inline point operator*(const double &c) const {return point(x*c, y*c);}
  inline point operator/(const double &c) const {return point(x/c, y/c);}
  
  inline int cmp(const point &p) const
  { if(int t = ::cmp(x, p.x)) return t; return ::cmp(y, p.y); }
  inline bool operator==(const point &p) const { return cmp(p) == 0; }
  inline bool operator!=(const point &p) const { return cmp(p) != 0; }
  inline bool operator<(const point &p) const { return cmp(p) < 0; }

  static point pivot; // para radial_lt
};

point point::pivot;

struct line
{
  point a, b;
  line(point a = point(0, 0), point b = point(0, 0)) : a(a), b(b) {}
};

inline double dot(const point &a, const point &b) {return a.x*b.x+a.y*b.y;}
inline double cross(const point &a, const point &b) {return a.x*b.y-a.y*b.x;}
inline double norm(const point &p) {return sqrt(dot(p,p));}
inline double arg(const point &p) {return atan2(p.y,p.x);}
inline double angle(const point &a, const point &b, const point &c)
{ point u=a-b,v=c-b; return atan2(cross(u,v),dot(u,v)); }

inline bool between(const point &a, const point &b, const point &p)
{ return cmp(cross(p-a,p-b))==0 && cmp(dot(a-p,b-p))<=0; }

int ccw(const point &a, const point &b, const point &c)
{
  double k = cross(b-a,c-a);
  if( k > eps ) return 1;
  if( k < -eps ) return -1;
  if( dot(c-a,b-a) < -eps ) return -1;
  if( dot(a-b,c-b) < -eps ) return 1;
  return 0;
}

// Falha se line a ou line b for pontual, ver se pode ocorrer!
bool intersect(const line &a, const line &b)
{
  return ( ccw(a.a, a.b, b.a) * ccw(a.a, a.b, b.b) <= 0 ) &&
    ( ccw(b.a, b.b, a.a) * ccw(b.a, b.b, a.b) <= 0 );
}

// distancia de r a pq (segmento)
double linedist(const point &p, const point &q, const point &r)
{
  point A = r - q, B = r - p, C = q - p;
  double a = dot(A,A), b = dot(B,B), c = dot(C,C);
  if (cmp(b, a + c) >= 0) return sqrt(a);
  else if (cmp(a, b + c) >= 0) return sqrt(b);
  else return fabs(cross(A,B)) / sqrt(c);
}

// 0: ext; -1: front; 1: int
int inside(const point &p, const vector<point> &T)
{
  double a = 0; int n = T.size();
  for (int i = 0; i < n; i++)
    {
      if (between(T[i], T[(i+1)%n], p)) return -1;
      a += angle(T[i], p, T[(i+1) % n]);
    }
  return cmp(a) != 0;
}

bool radial_lt(const point &p, const point &q)
{
  point P = p - point::pivot, Q = q - point::pivot;
  double r = cross(P, Q);
  if(cmp(r)) return r>0;
  return cmp(dot(P, P), dot(Q, Q)) < 0;
}

vector<point> convex_hull(vector<point>& T)
{
  int j = 0, k, n = T.size(); vector<point> U(n);
  point::pivot = *min_element(all(T));
  sort(all(T), radial_lt);
  for (k = n-2; k >= 0 && cmp(cross(T[0] - T[k], T[n-1] - T[k])) == 0; k--);
  reverse((k+1) + all(T));
  for (int i = 0; i < n; i++) {
    // troque o <= por < para manter pontos colineares
    while (j > 1 && cmp(cross(U[j-1] - U[j-2], T[i] - U[j-2])) <= 0) j--;
    U[j++] = T[i];
  }
  U.erase(j + all(U));
  return U;
}

// area orientada
double poly_area(vector<point>& T)
{
  double s = 0; int n = T.size();
  for (int i = 0; i < n; i++)
    s += cross(T[i], T[(i+1) % n]);
  return s / 2;
}

// interseccao de retas
point line_intersect(const line &r, const line &s)
{
  point a = r.b - r.a, b = s.b - s.a, c = point(cross(r.a,r.b),cross(s.a,s.b));
  return point(cross(point(a.x, b.x),c), cross(point(a.y, b.y),c)) / cross(a,b);
}

// spanning circle
typedef pair<point, double> circle;
bool in_circle(circle C, point p){
  return cmp(norm(p - C.first), C.second) <= 0;
}

point circumcenter(point p, point q, point r) {
  point a = p - r, b = q - r, c = point(dot(a, p + r) / 2, dot(b, q + r) / 2);
  return point(cross(c, point(a.y, b.y)), cross(point(a.x, b.x), c)) / cross(a, b);
}

circle spanning_circle(vector<point>& T) {
  int n = T.size();
  random_shuffle(all(T));
  circle C(point(), -INFINITY);
  for (int i = 0; i < n; i++) if (!in_circle(C, T[i])) {
      C = circle(T[i], 0);
      for (int j = 0; j < i; j++) if (!in_circle(C, T[j])) {
	  C = circle((T[i] + T[j]) / 2, norm(T[i] - T[j]) / 2);
	  for (int k = 0; k < j; k++) if (!in_circle(C, T[k])) {
	      point o = circumcenter(T[i], T[j], T[k]);
	      C = circle(o, norm(o - T[k]));
	    }
	}
    }
  return C;
}





int l,u;
double w;
point ll[5555];
point uu[5555];
int main ()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      int g;
      scanf("%lf %d %d %d",&w,&l,&u,&g);
      for(int i=0;i<l;i++)
	scanf("%lf %lf",&ll[i].x,&ll[i].y);
      for(int i=0;i<u;i++)
	scanf("%lf %lf",&uu[i].x,&uu[i].y);
      double st = w;
      vector<point> ax;
      for(int i=0;i<l;i++)
	ax.push_back(ll[i]);
      for(int i=0;i<u;i++)
	ax.push_back(uu[u-i-1]);

      double area = fabs(poly_area(ax))/g;
      printf("Case #%d:\n",pp);
      vector<double> saida;
      for(int kkk=0;kkk<g-1;kkk++)
	{
	  double men = 0, mai= st;
	  double meio = 0;
	  int fl,fu;
	  point tmp1,tmp2;
	  for(int p=0;p<300;p++) {
	    meio = (men+mai)/2;
	    ax.clear();
	    for(int i=0;i<l;i++)
	      {
		ax.push_back(ll[i]);
		if(meio+eps>ll[i].x && ll[i+1].x+eps>meio)
		  {
		    fl=i;
		    tmp1 = point(meio, (meio-ll[i].x)/(ll[i+1].x-ll[i].x)*(ll[i+1].y-ll[i].y) + ll[i].y);
		    ax.push_back(tmp1);
		    break;
		  }
	      }	      
	    int gaga = 0;
	    for(gaga = 0;gaga<u;gaga++)
	      {
		if(meio+eps>uu[gaga].x && uu[gaga+1].x+eps>meio)
		  {
		    fu = gaga;
		    tmp2 = point(meio, (meio-uu[gaga].x)/(uu[gaga+1].x-uu[gaga].x)*(uu[gaga+1].y-uu[gaga].y) + uu[gaga].y);
		    ax.push_back(tmp2);
		    break;
		  }
	      }
	    for(int i=gaga;i>=0;i--)
	      ax.push_back(uu[i]);
	    if(cmp(poly_area(ax),(g-kkk-1)*area)>0)
	      mai=meio;
	    else
	      men=meio;
	  }
	  l = fl+1;
	  u = fu+1;
	  ll[l]=tmp1,uu[u]=tmp2;
	  saida.push_back(meio);
	  st = meio;
	  
	}
      reverse(all(saida));
      for(int i=0;i<saida.size();i++)
	printf("%lf\n",saida[i]);
    }
  return 0;
}
