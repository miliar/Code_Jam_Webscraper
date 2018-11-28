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

int d[1001];
int p[1001];
int g[1001];
int next[1001],nextS[1001];
LL ne[20][1001],neS[20][1001];

int R,k,n;

void vyrataj_next(){
   int j=0;
   LL S=0;
   FOR(i,n){
      while(1){
        if(g[j]+S<=k) { S+=g[j]; j++; j%=n; } else break;
        if(j==i) break;
      }
      next[i]=j; nextS[i]=S;
      S-=g[i];
   }

   FOR(i,n) ne[0][i]=next[i], neS[0][i]=nextS[i];
   FR(q,1,20){
      FOR(i,n) {
        ne[q][i]=ne[q-1][ne[q-1][i]];
        neS[q][i]=neS[q-1][i]+neS[q-1][ne[q-1][i]];
      }
   }
}

LL simuluj(int q, int R){
//  printf("%d %d\n",q,R);
  if(R==0) return 0;
  if(R==1) return nextS[q];
  int ee=0;
  for(int e=19;e>=0;e--){
    if(R>=(1<<e)){
       ee=e; break;    
    }
  }
  return neS[ee][q]+simuluj(ne[ee][q],R-(1<<ee));
}

void solve(){
   scanf("%d %d %d",&R,&k,&n);
   FOR(i,n) scanf("%d",&g[i]);
   //vyratat next
   vyrataj_next();
//   FOR(i,n) printf(" %d",next[i]); printf("\n");
   printf("%lld\n", simuluj(0,R));


}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);
     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
