#include<stdio.h>
#include<math.h>
#include<string>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
typedef long long LL;
const double EPS = 1e-8;
const int INF = (1<<29);

struct Point{
  double x,y;
  Point(){}
  Point(double x,double y):x(x),y(y){}
  Point operator - (const Point &a)const{ return Point(x-a.x,y-a.y); }
  Point operator + (const Point &a)const{ return Point(x+a.x,y+a.y); }
  Point operator * (const double &a)const{ return Point(x*a,y*a); }
  double operator ^ (const Point &a)const{ return x*a.y-y*a.x; }
  double operator * (const Point &a)const{ return x*a.x+y*a.y; }

  bool operator > (const Point &a)const{ return x>a.x+EPS || (fabs(x-a.x)<EPS && y>a.y+EPS); }
  bool operator < (const Point &a)const{ return x<a.x-EPS || (fabs(x-a.x)<EPS && y<a.y-EPS); }
  bool operator == (const Point &a)const{ return fabs(x-a.x)<EPS && fabs(y-a.y)<EPS; }
  bool operator != (const Point &a)const{ return fabs(x-a.x)>EPS || fabs(y-a.y)>EPS; }

  double len2()const{ return x*x+y*y; }
  double len()const{ return sqrt(x*x+y*y); }
  Point resize(double d)const{ return Point(x/len()*d,y/len()*d); }
  Point rot()const{ return Point(y,-x); }
  Point rot(double d)const{ return Point(cos(d)*x+sin(d)*y, -sin(d)*x+cos(d)*y); }
};

Point a[2000],b[2000];

double getang(double a,double b,double c){
  return acos((a*a+b*b-c*c)/(2*a*b));
}

int n,m;
int main(){
  int ca; scanf("%d",&ca);
  for (int tt=1; tt<=ca; tt++){
    scanf("%d%d",&n,&m);
    for (int i=0; i<n; i++) scanf("%lf%lf",&a[i].x,&a[i].y);
    for (int i=0; i<m; i++) scanf("%lf%lf",&b[i].x,&b[i].y);
    printf("Case #%d:",tt);
    for (int t=0; t<m; t++){
      double r1=(b[t]-a[0]).len(), r2=(b[t]-a[1]).len();
      double a1 = getang(r1,(a[0]-a[1]).len(),r2)*2;
      double a2 = getang(r2,(a[0]-a[1]).len(),r1)*2;
//      printf("\n %d>> %f %f\n",t,a1,a2);
 //     printf(">. %lf %lf %lf\n",r1,r2,(a[0]-a[1]).len());
//      Point p1 = a[0] + (a[1]-a[0]).rot(ang).resize(r1);
 //     Point p2 = a[0] + (a[1]-a[0]).rot(-ang).resize(r1);
  //    double d = (p1-p2).len();
      double ans = a1*r1*r1/(2) + a2*r2*r2/2 - (0.5*r1*r1*sin(a1)) - (0.5*r2*r2*sin(a2));
      printf(" %.7f",ans+1e-20);
    }
    printf("\n");
  }
  return 0;
}
