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

LL N,M,A;

void solve(){
   scanf("%lld %lld %lld",&N,&M,&A);
   bool uz=false;
   FR(x1,0,N+1) FR(x2,0,N+1) FR(y1,0,M+1){
       if(uz) break;
       long long e=y1*x2+A;   
       if(e<0) e*=-1;
       int y2;
       if(x1==0){
          if(e!=0) continue;
          int y2=0;
       } else{
          if(e%x1) continue;
          y2=e/x1;
          if(y2>M) continue;
       }
       uz=true;
       printf(" %d %d %d %d %d %d\n",0,0,x1,y1,x2,y2);
       
   }
   if(!uz) printf(" IMPOSSIBLE\n");
}

main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d:",ppp);

     solve();
  }
}


