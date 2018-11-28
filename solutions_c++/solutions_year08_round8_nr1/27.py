#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <numeric>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long ll;

const double eps=1e-10;

double d(double a1,double a2,double b1,double b2) {
     return a1*b2-a2*b1;
}
ll gcd(ll a,ll b) { 
     if(a<0)a=-a;
     if(b<0)b=-b;
     if(!b)return a;
     return gcd(b,a%b);
}

void relax(ll &a1,ll &b1,ll &c1) {
     ll g=gcd(a1,gcd(b1,c1));
     if(a1<0||a1==0&&b1<0||a1==0&&b1==0&&c1<0)g=-g;
     a1/=g;b1/=g;c1/=g;
}
double len(double x1,double y1,double x2,double y2) {
     return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}
double s(double x1,double y1,double x2,double y2,double x3,double y3) {
     double ab,ac,bc;
     ab=len(x1,y1,x2,y2);
     ac=len(x1,y1,x3,y3);
     bc=len(x2,y2,x3,y3);
     double p=(ab+ac+bc)/2.0;
     return sqrt(p*(p-ab)*(p-ac)*(p-bc));
}
bool inside(double x1,double y1,double x2,double y2,double x3,double y3,double x,double y) {
     return fabs(s(x1,y1,x2,y2,x3,y3)-
                 s(x1,y1,x2,y2,x ,y )-
                 s(x ,y ,x2,y2,x3,y3)-
                 s(x1,y1,x ,y ,x3,y3))<1e-8;

}

int main()
{
     freopen("a.in","r",stdin);
     freopen("a.out","w",stdout);
     int n,test;
	
     for(cin>>n,test=1;test<=n;++test) {
          ll x11,y11,x12,y12,x13,y13,x21,y21,x22,y22,x23,y23;
          ll a1,b1,c1,a2,b2,c2;
          double x,y;
          cin>>x11>>y11>>x12>>y12>>x13>>y13;
          cin>>x21>>y21>>x22>>y22>>x23>>y23;
          a1=(x12-x11)-(x22-x21);
          b1=(x13-x11)-(x23-x21);
          c1=x21-x11;
          a2=(y12-y11)-(y22-y21);
          b2=(y13-y11)-(y23-y21);
          c2=y21-y11;
          relax(a1,b1,c1);relax(a2,b2,c2);
          double a,b;
          if(a1!=a2||b1!=b2) {
               a=d(c1,c2,b1,b2)/d(a1,a2,b1,b2);
               b=d(a1,a2,c1,c2)/d(a1,a2,b1,b2);
               x=x11+a*(x12-x11)+b*(x13-x11);
               y=y11+a*(y12-y11)+b*(y13-y11);
               if(inside(x21,y21,x22,y22,x23,y23,x,y))
                    printf("Case #%d: %.10lf %.10lf\n",test,x,y);
               else printf("Case #%d: No Solution\n",test);
          }
          else if(c1!=c2)printf("Case #%d: No Solution\n",test);
          else if(a1==0&&b1==0) {
               if(c1==0)printf("Case #%d: %.10lf %.10lf\n",test,x21,y21);
               else printf("Case #%d: No Solution\n",test);
          }
          else {
               printf("Case #%d: No Solution\n",test);
               cerr<<"WARNING"<<endl;
          }
     }
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
