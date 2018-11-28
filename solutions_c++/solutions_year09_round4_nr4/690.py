#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<string.h>
using namespace std;
#define EPS 1e-8

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
  //bool operator > (const Point &a)const{ return x<a.x-EPS || (fabs(x-a.x)<EPS && y<a.y-EPS); }
  bool operator == (const Point &a)const{ return fabs(x-a.x)<EPS && fabs(y-a.y)<EPS; }
  bool operator != (const Point &a)const{ return fabs(x-a.x)>EPS || fabs(y-a.y)>EPS; }

  double len2()const{ return x*x+y*y; }
  double len()const{ return sqrt(x*x+y*y); }
  Point resize(double d)const{ return Point(x/len()*d,y/len()*d); }
  Point rot()const{ return Point(y,-x); }
};
Point a[100];
int r[100];
int n;
int main(){
	int ca; scanf("%d",&ca);
	for (int tt=1; tt<=ca; tt++){
		scanf("%d",&n);
		for (int i=0; i<n; i++) scanf("%lf%lf%d",&a[i].x,&a[i].y,&r[i]);
		double ans=1e10,mxr=0;
		for (int i=0; i<n; i++) mxr=max(mxr,(double)r[i]);
		for (int i=0; i<n; i++){
			for (int j=i+1; j<n; j++){
				ans=min(ans,(a[i]-a[j]).len()+r[i]+r[j]); 
			} 
		}
		ans/=2;
		if (n==1) ans=r[0];
		if (n==2) ans=mxr;
		printf("Case #%d: %f\n",tt,ans+1e-12);
	}
	return 0;
}
