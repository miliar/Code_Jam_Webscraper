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


long long r[105][105];

int height,wight;
int n;
int x[11],y[11];
const LL M=10007;

void solve(){
   CL(r);
   r[1][1]=1;
   scanf("%d %d %d",&height,&wight,&n);
   FOR(i,n) { scanf("%d %d",&x[i],&y[i]); r[x[i]][y[i]]=-1; }
   FR(i,1,height+1) FR(j,1,wight+1) if(r[i][j]!=-1){
      r[i][j]%=M;
      if(r[i+2][j+1]!=-1) { r[i+2][j+1]+=r[i][j]; r[i+2][j+1]%=M; }
      if(r[i+1][j+2]!=-1) { r[i+1][j+2]+=r[i][j]; r[i+1][j+2]%=M; }
   }
   printf("%lld\n",r[height][wight]);
 
}

main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
