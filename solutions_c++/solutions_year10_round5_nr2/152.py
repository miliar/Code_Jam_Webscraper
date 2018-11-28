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
LL L;
int d[100];
int v[1000205];

void solve(){
   scanf("%lld %d",&L,&n);
   FOR(i,n) scanf("%d",&d[i]);
   sort(d,d+n);
   LL maxi=2000000000; maxi*=maxi; maxi++;
   LL ret=maxi;
   FOR(x,1000005){    
     v[x]=987654321;
     FOR(i,n) if(x>=d[i]) v[x]=min(v[x],v[x-d[i]]+1);
     if(x==0) v[x]=0;
     if(v[x]==987654321) continue;
     if((L-x)%d[n-1]==0) ret=min(ret,(LL)v[x]+(L-x)/d[n-1]);
   }
   if(ret==maxi) printf("IMPOSSIBLE\n"); else printf("%lld\n",ret); 
   
}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
