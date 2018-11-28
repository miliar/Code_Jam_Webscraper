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


vector<double> x,y,r;
double xx,yy,rr;

double dist(int i, int j){
   return sqrt((x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]));   
}

void solve(){
   int n; scanf("%d",&n); if(n>=4) return;
   x.clear(); y.clear(); r.clear();

   FOR(i,n) { scanf("%lf %lf %lf\n",&xx,&yy,&rr); x.PB(xx); y.PB(yy); r.PB(rr); }

   double ret=1e40;
   if(n==3){
      FOR(i,n) FOR(j,n) if(i!=j) FOR(k,n) if(i!=k && j!=k){
         double moj=1e40;
         moj=dist(i,j)+r[i]+r[j];
         moj=max(moj/2,r[k]);
         ret=min(moj,ret);
      }
   } 
   if(n==2){
      ret=max(r[0],r[1]); 
   }
   if(n==1) ret=r[0];
   printf("%.8lf\n",ret);
}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
