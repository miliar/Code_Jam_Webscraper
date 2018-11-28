#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>
#include <complex>

#define oo 1000000005
#define eps 1e-11

#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a), _b = (b); i < _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i > _b; i--)
#define RESET(c,x) memset (c, x, sizeof (c))

#define PB push_back
#define MP make_pair
#define F first
#define S second

using namespace std;

const double EPS = 1e-8;
const double INF = 1e12;
#define curr(P, i) P[i]
#define next(P, i) P[(i+1)%P.size()]
#define prev(P, i) P[(i+P.size()-1) % P.size()]
typedef complex<double> Point;
namespace std {
   bool operator < (const Point& a, const Point& b) {
      return real(a) != real(b) ? real(a) < real(b) : imag(a) < imag(b);
   }
}
double cross(const Point& a, const Point& b) { return imag(conj(a)*b); }
double dot(const Point& a, const Point& b) { return real(conj(a)*b); }
struct Line : public vector<Point> {
   Line(const Point &a, const Point &b) {
      push_back(a); push_back(b);
   }
};
double area2(const vector<Point>& P) {
   double A = 0;
   for (int i = 0; i < P.size(); ++i) 
      A += cross(curr(P, i), next(P, i));
   return A;
}
Point crosspoint(const Line &l, const Line &m) {
   double A = cross(l[1] - l[0], m[1] - m[0]);
   double B = cross(l[1] - l[0], l[1] - m[0]);
   if (abs(A) < EPS && abs(B) < EPS) return m[0]; // same line   
   return m[0] + B / A * (m[1] - m[0]);
}



int ntest;
int L,V,G; double W,x,y;
vector<Point> vt,LP,UP;
double area;
double f(double x){
    vector<Point> temp;
    int i;
    for(i=0; real(LP[i])-x < 1e-6 ; i++)
        temp.PB(LP[i]);
    temp.PB(crosspoint( Line(LP[i],LP[i-1]), Line( Point(x,0), Point(x,1) ) ) );
    
    for(i=UP.size()-1; real(UP[i])-x > 1e-6 ; i--);
    temp.PB(crosspoint(Line(UP[i],UP[i+1]),Line( Point(x,0), Point(x,1) ) ) );
    for(; i>-1; i--) temp.PB(UP[i]);
    return area2(temp);
}
int main () {
    freopen("A-small-attempt0.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&ntest);
    REP(test,ntest){
        printf("Case #%d:\n",test+1);  vt.clear(); UP.clear(); LP.clear();
        scanf("%lf %d %d %d", &W,&L,&V,&G);
        REP(i,L){ scanf("%lf %lf",&x,&y); LP.PB(Point(x,y)); }
        REP(i,V){ scanf("%lf %lf",&x,&y); UP.PB(Point(x,y)); }
        REP(i,L) vt.PB(LP[i]); REPD(i,V) vt.PB(UP[i]);
        area = area2(vt)/G;        
        double t=0;
        REP(i,G-1){
            double l=t,h=W;
            while(fabs(h-l)>1e-7){
                double m = (h+l)/2.0;
                if (f(m) < area ) l=m;
                else h=m;              
            }
            printf("%.6lf\n",l);
            t=l;
            vector<Point> temp;
            int i=0;
            for(;real(LP[i])-t < 1e-6 ; i++); temp.PB(crosspoint( Line(LP[i],LP[i-1]), Line( Point(t,0), Point(t,1) ) ) );
            for(;i<LP.size(); i++) temp.PB(Point(LP[i]));
            LP=temp; temp.clear();            
            i=0;
            for(;real(UP[i])-t < 1e-6 ; i++); temp.PB(crosspoint( Line(UP[i],UP[i-1]), Line( Point(t,0), Point(t,1) ) ) );
            for(;i<UP.size(); i++)temp.PB(Point(UP[i]));            
            UP=temp;            
        }
    }    
    return 0;
}
