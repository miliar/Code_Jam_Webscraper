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


int p;
int v[1<<(12)];
int n;
LL r[1<<12][11];
int uz[1<<12][11];
int need[1<<11];

LL ries(int q, int mam){
    LL &ret=r[q][mam];
    if(uz[q][mam]) return ret;
    uz[q][mam]=true;
    int left=2*q;
    int right=2*q+1;
    if(left>=n || right>=n) {
      if(need[left-n]<=mam && need[right-n]<=mam) return ret=0;  
      if(need[left-n]<=mam+1 && need[right-n]<=mam+1) return ret=v[q];
      return ret=987654321;
    }
    ret=(LL)v[q]+ries(left,mam+1)+ries(right,mam+1);
    ret=min(ret,ries(left,mam)+ries(right,mam));
    return ret;
}

void solve(){
   scanf("%d",&p);
   for(int i=(1<<p)-1;i>=0;i--) { scanf("%d",&need[i]); need[i]=p-need[i]; }
   int q=(1<<p)-1;
   n=q+1;
   FOR(i,p){
      FOR(j,(1<<(p-i-1))){ scanf("%d",&v[q]); q--; }
   }
//   FOR(i,n) printf(" %d",v[i]);
//   PN;
   CL(uz); CL(r);
   printf("%lld\n",ries(1,0));
}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
