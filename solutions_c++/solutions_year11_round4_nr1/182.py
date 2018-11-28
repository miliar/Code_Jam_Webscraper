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

priority_queue<pair<double,double> > Q;
double length,speed,rspeed,rtime;
int n;

void solve(){
   scanf("%lf %lf %lf %lf %d",&length,&speed,&rspeed,&rtime,&n);
   rspeed-=speed;
   double lx=0;
   FOR(i,n){      
      double x,y,v;
      scanf("%lf %lf %lf",&x,&y,&v);
//      printf("%lf %lf %lf %lf\n",lx,x,y,v);
      if(lx!=x) Q.push(MP(-speed,x-lx));
      Q.push(MP(-speed-v,y-x));
      lx=y;
   }
   Q.push(MP(-speed,length-lx));
   double ret=0.0;
   while(!Q.empty()){
      double speed=-Q.top().first;
      double d=Q.top().second;
//      printf("%.3lf %.3lf\n",speed,d);
      Q.pop();
      if( d/(speed+rspeed) <= rtime){
         //zoberieme to behom
         double t=d/(speed+rspeed);
         rtime-=t;
         ret+=t;
      } else{
         d-= (speed+rspeed)*rtime;
         ret+=rtime;
         rtime=0;
         double t=d/speed;
         ret+=t;
      }
//      printf("%.8lf\n",ret);
   }
   printf("%.10lf\n",ret);

}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
