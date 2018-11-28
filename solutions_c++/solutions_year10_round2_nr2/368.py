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

int n,k;
LL B,T;

LL x[100],v[100];
int need[100];


void solve(){
   scanf("%d %d %lld %lld",&n,&k,&B,&T);
   FOR(i,n) { scanf("%lld",&x[i]); x[i]=B-x[i]; }
   FOR(i,n) scanf("%lld",&v[i]);
   for(int i=n-1;i>=0;i--){
      need[i]=987654321;
//      printf("%lld %lld\n",T*v[i],x[i]);
      if(T*v[i]<x[i]) ; else{
        need[i]=n-i-1;
        FR(j,i+1,n) need[i]=min(need[i],j-i-1+need[j]);
      }
//      printf(" %d\n",need[i]);
   }
//   FOR(i,n) printf(" %d",need[i]); PN;
   sort(need,need+n);
   bool ok=true;
   int ret=0;
   FOR(i,k){
      if(need[i]==987654321){ ok=false; break; }
      ret+=need[i];
   }
   if(ok) printf("%d\n",ret); else printf("IMPOSSIBLE\n");
}



int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
