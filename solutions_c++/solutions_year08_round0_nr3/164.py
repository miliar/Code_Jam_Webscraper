#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <numeric>
#include <iostream>
#include <cassert>
#define FOR(i,n) for(int _n=n,i=0;i<_n;++i)
#define FR(i,a,b) for(int _b=b,i=a;i<_b;++i)
#define CL(x) memset(x,0,sizeof(x))
#define PN printf("\n");
#define MP make_pair
#define PB push_back
#define SZ size()
#define ALL(x) x.begin(),x.end()
#define FORSZ(i,v) FOR(i,v.size())
#define FORIT(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();it++)
using namespace std;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
///////////////////////////////////////////////////////////////////////////////////

double f,R,t,r,g;
double PI=acos(-1);
double EPS=1e-8;

inline bool dnu(const double &x, const double &y){
    return x*x+y*y<=R*R;
}

inline double ries_rovn(double h){
  return sqrt(fabs(R*R-h*h));
}

inline double obsahT(double x1, double y1, double x2, double y2, double x3, double y3){
   double dxa=x1-x2;
   double dya=y1-y2;
   double dxb=x3-x2;
   double dyb=y3-y2;
   return fabs(dxa*dyb-dxb*dya)/2;
}



inline double usek(double x1, double y1, double x2, double y2){
   double d=sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
   d/=2;
   double alpha=asin(d/R);
   double ret=(R*R*(alpha))-obsahT(0,0,x1,y1,x2,y2);   
   return ret;
}


double obsahS(double x, double y){
   double w_dole=ries_rovn(y);
   double w_vlavo=ries_rovn(x);
   double ret=0.0;
   if(w_dole<=x+g && w_vlavo<=y+g) return obsahT(x,y, x,w_vlavo, w_dole,y)+usek(x,w_vlavo, w_dole,y);              
   if(w_dole>=x+g){
     double w_vpravo=ries_rovn(x+g);
     ret+=(w_vpravo-y)*g;
     if(w_vlavo<=y+g){
        ret+=obsahT(x,w_vpravo, x+g,w_vpravo, x,w_vlavo)+usek(x,w_vlavo, x+g,w_vpravo);   
     } else{
        double w_hore=ries_rovn(y+g);
        ret+=obsahT(x,w_vpravo, x+g,w_vpravo, x,y+g)+ obsahT(x,y+g, w_hore,y+g, x+g,w_vpravo)+ usek(w_hore,y+g, x+g,w_vpravo);  
     }              
   } else{
     double w_hore=ries_rovn(y+g);
     ret+=(w_hore-x)*g;
     ret+=obsahT(w_hore,y+g, w_hore,y, w_dole,y)+usek(w_hore,y+g, w_dole,y);   
   }
   return ret;
}


void solve(){

  scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
  if(2*f>=g || t+f>=R){ printf(" %.8lf\n",1.0); return ;}
  double obsah=PI*R*R/4;
  r+=f; g-=2*f;
  R-=t; R-=f; 

  double ret=0.0;
  double x=r,y=r;
  while(dnu(r,y)){
     while(dnu(x,y)){
        double moj=0;
        if(dnu(x+g,y+g)) moj+=g*g; else moj=obsahS(x,y);
        ret+=moj;
        x+=2*r+g;
     }
     y+=2*r+g;
     x=r;
  }
  printf(" %.8lf\n",1.0-ret/obsah);
}

main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d:",ppp);

     solve();
//     if(ppp==2) break;
  }
}


