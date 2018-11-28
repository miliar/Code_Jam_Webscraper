#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

bool fless(double a,double b){ return b-a>1e-8; }
bool fequal(double a,double b){ return fabs(b-a)<=1e-8; }

struct Point{
    double x,y;
    Point(){}
    Point(double x,double y):x(x),y(y){}

    Point operator-(const Point &p)const{ return Point(x-p.x,y-p.y); }
    Point operator+(const Point &p)const{ return Point(x+p.x,y+p.y); }
    Point operator*(double u)const{ return Point(x*u,y*u); }
    double operator^(const Point &p)const{ return x*p.y-y*p.x; }
    double operator*(const Point &p)const{ return x*p.x+y*p.y; }

    void read(){ scanf("%lf%lf",&x,&y); }
    double len()const{ return sqrt(x*x+y*y); }

    Point setLen(double l)const{
        double u = l/len();
        return Point(x*u,y*u);
    }
};

bool intersect(const Point &a, const Point &b, const Point &c, const Point &d){
    double w = (b-a)^(d-c);
    if (fequal(w,0)){
        return 0;
    }
    double u = ((c-a)^(d-c))/w;
    double v = ((c-a)^(b-a))/w;
    return !fless(v,0) && !fless(1,v) && fless(0,u) && fless(u,1);
}

double angle(const Point &a, const Point &b){
    int w = (fless(0,a^b))?1:-1;
    return acos((a*b)/a.len()/b.len())*w;
}

double f(const Point &p1, double r1, const Point &p2, double r2){
  double len = (p1-p2).len();
  double max_r = max(r1,r2);
  if (fless(len+r1, r2)){
    return r2*0.5;
  }else if (fless(len+r2,r1)){
    return r1*0.5;
  }else{
    return (len+r1+r2)*0.5;
  }
}

int main(){
  int tt; scanf("%d",&tt);
  for (int ti=1;ti<=tt;ti++){
    int n; scanf("%d",&n);
    Point P[n];
    double R[n];
    for (int i=0;i<n;i++){
      P[i].read(); scanf("%lf",&R[i]);
    }
    double ans=1e10;

    while(n>3);
 
    if (n==1)ans = R[0];
    else if (n==2)ans = max(R[0],R[1]);
    else{
      ans = min(ans, max(f(P[0],R[0],P[1],R[1]),R[2]));
      ans = min(ans, max(f(P[0],R[0],P[2],R[2]),R[1]));
      ans = min(ans, max(f(P[1],R[1],P[2],R[2]),R[0]));
    }
    printf("Case #%d: %10lf\n",ti,ans);
  }

  return 0;
}
