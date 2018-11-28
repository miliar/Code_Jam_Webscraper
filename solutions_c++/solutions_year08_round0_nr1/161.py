#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <numeric>
#include <iostream>
#include <cassert>
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

char r[1000],rr[1000];;
int n,m;
VI a;
map<string,int> cislo;

int dp[1005][105];

void solve(){
   a.clear(); cislo.clear();
   fgets(r,sizeof(r),stdin); sscanf(r,"%d",&n);
   FOR(i,n){ fgets(r,sizeof(r),stdin); cislo[r]=i; }
   fgets(r,sizeof(r),stdin); sscanf(r,"%d",&m);
   FOR(i,m){ fgets(r,sizeof(r),stdin); a.PB(cislo[r]); }

   FOR(i,n) dp[0][i]=0;
   FR(j,1,m+1){
      int naj1=1001,naj2=1001;
      int kde1=0,kde2=0;
      FOR(i,n){
         //minimum zo stlplca j-1
         if(dp[j-1][i]<naj1){
            naj2=naj1; 
            kde2=kde1;
            naj1=dp[j-1][i];
            kde1=i;
         } else if(dp[j-1][i]<naj2){
            naj2=dp[j-1][i];
            kde2=i;
         }
      }
      FOR(i,n){
         if(a[j-1]==i) { dp[j][i]=1001; continue; }
         dp[j][i]=dp[j-1][i];
         if(kde1!=i) { dp[j][i]=min(dp[j][i],naj1+1); }
         if(kde2!=i) { dp[j][i]=min(dp[j][i],naj2+1); }
      }
   }
//   FOR(i,m) printf(" %d",a[i]); PN;
//   FOR(j,m+1){ FOR(i,n) printf(" %d",dp[j][i]); PN; }
   int ret=1001;
   FOR(i,n) ret=min(ret,dp[m][i]);
   printf(" %d\n",ret);
}

main(){
  fgets(r,sizeof(r),stdin);
  int pvs; sscanf(r,"%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d:",ppp);

     solve();
  }
}


