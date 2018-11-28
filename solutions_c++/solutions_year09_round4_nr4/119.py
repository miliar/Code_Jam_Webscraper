#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

typedef long double LD;

struct point {
  LD x,y;
  point(LD a=0.0,LD b=0.0):x(a),y(b){}
};

LD INF = 10000000.0;

point a[20];
LD radius[20];
int n;

inline LD sqr(LD x) { return x*x; }
inline LD dist(point &a, point &b) {
  return sqrt(sqr(a.x-b.x)+sqr(a.y-b.y));
}

int main() {
  int d;
  scanf("%d",&d);
  for(int i=1;i<=d;++i) {
    printf("Case #%d: ",i);
    scanf("%d\n",&n);
    for(int j=0;j<n;++j) {
      LD aa,b,c;
      scanf("%Lf %Lf %Lf",&aa,&b,&c);
      a[j]=point(aa,b);
      radius[j]=c;
    }
    if(n==1) printf("%.7Lf\n",radius[0]);
    else if(n==2) printf("%.7Lf\n",max(radius[0],radius[1]));
    else {
      LD ret=INF;
      ret=min(max(radius[0],(radius[1]+radius[2]+dist(a[1],a[2])))/2.0,ret);
      ret=min(max(radius[1],(radius[0]+radius[2]+dist(a[0],a[2])))/2.0,ret);
      ret=min(max(radius[2],(radius[0]+radius[1]+dist(a[0],a[1])))/2.0,ret);
      printf("%.7Lf\n",ret);
    }
  }
  return 0;
}