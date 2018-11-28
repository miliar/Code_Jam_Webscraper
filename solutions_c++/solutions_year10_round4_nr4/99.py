#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<utility>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<cctype>
using namespace std;
#define inf 1e100
#define eps 1e-6
template<class T> void chkmax(T&a,T b){if(a<b)a=b;}
template<class T> void chkmin(T&a,T b){if(a>b)a=b;}

#define sqr(x) ((x)*(x))

double PI=acos(-1.0);

double cal_area(double r,double y,double x){
  double angle=atan(x/y);
  if(angle<0)angle+=PI;
  double cir=r*r*angle;
  double tri=x*y;
  //printf("cal_area(%lf %lf %lf):%lf %lf %lf\n",r,y,x,angle,cir,tri);
  return cir-tri;
}

double cal(double r1,double r2,double L){
  if(r1>r2)swap(r1,r2);
  //printf("cal(%lf %lf %lf\n",r1,r2,L);
  double det=(r1*r1-r2*r2)/L;
  double y1=(L+det)/2;
  double y2=(L-det)/2;
  double x=sqrt(r1*r1-y1*y1);
  //printf("<><><><>%lf %lf %lf %lf %lf\n",y1,y2,x,r1,r2); 
  double res=cal_area(r1,y1,x);
  res+=cal_area(r2,y2,x);
  return res;
}

int main(){
  int Cas,ca=0;
  scanf("%d",&Cas);
  while(Cas--){
    int n,m;
    double x1,x2,y1,y2,x,y;
    scanf("%d%d",&n,&m);
    scanf("%lf%lf%lf%lf",&x1,&y1,&x2,&y2);
    double L=sqrt(sqr(x1-x2)+sqr(y1-y2));
    printf("Case #%d:",++ca);
    int i;
    for(i=0;i<m;++i){
      scanf("%lf%lf",&x,&y);
      double r1=sqrt(sqr(x-x1)+sqr(y-y1));
      double r2=sqrt(sqr(x-x2)+sqr(y-y2));
      double ans=cal(r1,r2,L);
      printf(" %.12lf",ans);
    }
    putchar(10);
  }
  return 0;
}
