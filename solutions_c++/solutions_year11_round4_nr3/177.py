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

const int MAXI=2000000;
bool p[MAXI];
LL n;
VI e;

int najrychlejsie(int n){
   int ret=0;
   FR(i,2,n+1) if(!p[i]) ret++;
   if(ret==0) ret=1;
   return ret;
}

int najpomalsie(int n){
   int ret=0;
   FR(i,1,n+1){
      int poc=0;
      FORSZ(j,e){
         int p=e[j];
         if(i%p==0) poc++;
      }
      if(poc<=1) {
         ret++;
//         printf(" %d",i);
      }
   }
   return ret;
}

int fsolve(LL n){
   int ret=0;
   FORSZ(i,e){
      LL p=e[i];
      while(p*e[i]<=n) p*=e[i],ret++;
   }
   if(n>=2) ret++;
   return ret;

}

void solve(){
   scanf("%lld",&n);
///   printf("%d\n",najrychlejsie(n));
//   printf("%d\n",najpomalsie(n));
//   int ret=najpomalsie(n)-najrychlejsie(n);
//   printf("%d\n",ret);
   printf("%d\n",fsolve(n));
   
}

int main(){
  CL(p);
  FR(i,2,MAXI) if(!p[i]){
    for(int j=i+i;j<MAXI;j+=i) p[j]=true;
  }
  FR(i,2,MAXI) if(!p[i]) e.PB(i);
  //FORSZ(i,e) printf(" %d",e[i]);

  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
