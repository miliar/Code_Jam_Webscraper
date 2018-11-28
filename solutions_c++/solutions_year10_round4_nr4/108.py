#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<deque>
#include<queue>
#include<stack>
#include<functional>
#include<sstream>
#include<iostream>
#include<ctime>
#include<algorithm>
using namespace std;

#define DEBUG(x...) printf(x)
#define allv(v) (v).begin(),(v).end()
#define rall(v) (v).begin(),(v).rend()
#define _foreach(it,b,e) for(__typeof__(b); it!=(e);++it)
#define foreach(x...) _foreach(x)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll;//dois L's
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
  line(point a=point(0,0), point b=point(0,0)) : a(a), b(b) {}
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
      if (between(T[i],T[(i+1) % n],p)) return -1;
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


double arr(double a,double r)
{
  return a*r*r/2-r*r*sin(a)/2;
}
double solve(circle x,circle y)
{
  double dist=norm(x.first-y.first);
  double r1=x.second;
  double r2=y.second;
  if(r1+r2<dist)return 0;
  double alfa,beta;
  alfa = 2*acos(-(r2*r2-r1*r1-dist*dist)/(2*r1*dist));
  beta= 2*acos(-(r1*r1-r2*r2-dist*dist)/(2*r2*dist));
  //printf("%lf %lf\n",alfa,beta);
  
  // if(dist>r1 && dist>r2)
  return arr(alfa,r1)+arr(beta,r2);
  if(1);
  else
    {
      if(r1<dist)
	return alfa*r1*r1/2+arr(beta,r2);
      if(r2<dist)
	return arr(alfa,r1)+beta/2*r2*r2;
      else
	return  alfa*r1*r1/2+beta/2*r2*r2;
    }
  return 0;
}

point pole[55];
point buck[55];
int main ()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      int n,m;
      scanf("%d %d",&n,&m);
      for(int i=0;i<n;i++)
	{
	  double x,y;
	  scanf("%lf %lf",&x,&y);
	  pole[i]=point(x,y);
	}
      for(int i=0;i<m;i++)
	{
	  double x,y;
	  scanf("%lf %lf\n",&x,&y);
	  buck[i]=point(x,y);
	}
      double ret[55];
      for(int i=0;i<m;i++)
	{
	  circle x= make_pair(pole[0],norm(pole[0]-buck[i]));
	  circle y= make_pair(pole[1],norm(pole[1]-buck[i]));
	  ret[i]=solve(x,y);

	}
      printf("Case #%d:",pp);
      for(int i=0;i<m;i++)
	printf(" %lf",ret[i]);
      printf("\n");
    }
  return 0;
}
