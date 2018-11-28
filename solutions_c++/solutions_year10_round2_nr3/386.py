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


void solve(){
   int n; scanf("%d",&n);
//   if(n==2) { printf("%d\n",1); return; }
   int ret=0;
   int p[27];
   VI e; e.PB(1);
   FOR(mask,1<<(n-2)){      
      p[0]=p[1]=0;
      FR(i,2,n){
         if(i) p[i]=p[i-1]; else p[i]=0;
         if(mask&(1<<(i-2))) { p[i]++; e.PB(i); }
      }
      p[n]=p[n-1]+1;
      int x=p[n];
      bool ok=true;
      while(x!=1){ if(mask&(1<<(x-2))) x=p[x]; else { ok=false; break; }  }
      if(ok) { ret++; }
   }
   printf("%d\n",ret%100003);
}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
