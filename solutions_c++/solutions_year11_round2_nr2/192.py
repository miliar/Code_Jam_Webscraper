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

int n;
LL d;
LL x[205],p[205];

bool dasa(LL T){
   LL xx=1000000000; xx*=xx; xx*=-1;
   FOR(i,n){
      LL zx=max(xx,x[i]-T);
      if(abs(zx-x[i])>T) return false;
      LL kx=zx+(p[i]-1)*d;
      if(abs(kx-x[i])>T) return false;
      xx=kx+d;
   }
   return true;
}

void solve(){
   scanf("%d %lld\n",&n,&d);
   d*=2;
   FOR(i,n) scanf("%lld %lld\n",&x[i],&p[i]);
   FOR(i,n) x[i]*=2;
   LL left=0,right=2000000000;
   right*=right;
   while(right-left>5){
      LL T=(right+left)/2;
      if(dasa(T)) right=T; else left=T;
   }
   LL ret=0;
   for(LL T=left;T<=right;T++){
      if(dasa(T)){
         ret=T; break;
      }
   }
   printf("%lld",ret/2);
   if(ret%2) printf(".5"); else printf(".0");
   PN;
}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
