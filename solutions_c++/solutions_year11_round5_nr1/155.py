// pre-written code {{{
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <numeric>
#include <iostream>
#include <cassert>
#include <set>
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
// }}}

struct bod{
   double x,y;
   bod();
   bod(int x, int y) : x(x),y(y){}
};

vector<bod> dole, hore;
vector<double> sdole, shore;

int n,m,g,w;

inline double daj_obsah(bod A, bod B){
   double dy=fabs(A.y-B.y);
   double dx=fabs(A.x-B.x);
   return dx*(max(A.y,B.y))-dx*dy/2;
}

double obsah(double r, const vector<bod> & v){
   double S=0.0;
   FORSZ(i,v){
      if(i==0) continue;
      if(r>v[i].x){
         S+=daj_obsah(v[i],v[i-1]);
      } else {
         double dy=fabs(v[i].y-v[i-1].y);
         double dx=fabs(v[i].x-v[i-1].x);
         S+=(r-v[i-1].x)*v[i-1].y;
         S+=(r-v[i-1].x)*(v[i].y-v[i-1].y)*(r-v[i-1].x)/(v[i].x-v[i-1].x)/2;
         break;
//         double dyy=(v[i].y-v[i-1].y)*(r-v[i-1].x)/(v[i].x-v[i-1].x);
//         S+=daj_obsah(v[i-1],bod(r,v[i-1].y+dyy));
      }
   }
   return S;
}


void solve(){
   scanf("%d %d %d %d",&w,&n,&m,&g);
   PN;
   dole.clear(); hore.clear();
   int x,y;
   FOR(i,n) {
      scanf("%d %d",&x,&y); 
      y+=1000;
      dole.PB(bod(x,y));
   }
   FOR(i,m){
      scanf("%d %d",&x,&y); 
      y+=1000;
      hore.PB(bod(x,y));
   }
   double S=obsah(w,hore)-obsah(w,dole);
//   printf("S: %.8lf\n",S);
   FOR(i,g-1){
      double ss=(double)(i+1)*S/g;
      //printf("ss: %.8lf\n",ss);
      double left=0.0,right=w;
      while(fabs(right-left)>1e-8){
         double c=(left+right)/2;
         if(obsah(c,hore)-obsah(c,dole)>ss) right=c; else left=c;
      }
      double c=(left+right)/2;
//      printf("%.8lf %.8lf %.8lf\n",c,obsah(c,hore),obsah(c,dole));
      printf("%.8lf\n",c);
   }
}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
