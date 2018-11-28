#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;

long long gcd(long long large,long long small) {
  // printf("%d %d\n",large,small);
   if(small==0)
   return large;
   
   return gcd(small,large%small);

}

int main() {
   int testcases;
   scanf("%d",&testcases);
   for(int tc=1;tc<=testcases;tc++) {
      long long PD,WG,WD,D=100,G=100,PG;
      long long N;
      bool res=1;
      scanf("%lld %lld %lld\n",&N,&PD,&PG);
      WD = PD;
      WG = PG;
      
      long long hcfd = gcd(D,WD);
      //printf("%d\n",hcfd);
      WD = WD/hcfd;
      D  = D/hcfd;
      
      long long hcfg = gcd(G,WG);
      //printf("%d\n",hcfd);
      WG = WG/hcfg;
      G  = G/hcfg;
      
      long long discG = G;
      long long discWG = WG;
      
      if(D>N) {
//         printf("Due to Daily percent\n");
         res=0;
      }

      if(res) {
         while((G<D)) {
            G+=discG;
            WG+=discWG;
         }
         
       /*  while((WG<WD)) {
            G+=G;
            WG+=WG;
         }*/
         
         if(G==WG && D!=WD) {
            //printf("100 percent G & not 100 percent D\n");
            res=0;
         }
         
         if(PG==0 && PD!=0) {
            res=0;
         }
         
    /*     int diffW = WG-WD;
         int diffT = G-D;
         
         while((WG-WD)>(G-D)) {
            //diffT+=discG;
            //diffW+=discWG;
            G+=discG;
            
         }*/
         
         
//         if((WG-WD)
      
      
      }
   
      printf("Case #%d: ",tc);
    //  printf("%d %d %d %d %d",N,D,WD,G,WG);
      if(res)
      printf("Possible\n");
      else
      printf("Broken\n");      
   
   }
   return 0;
}

