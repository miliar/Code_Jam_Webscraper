
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<queue>
#include<cstdio>

using namespace std;
int  n;
int m[5400];
long long int dp[5000][50];
int c[5000];
int main()
{
   int p, k, t, tests;
   int itest;
   for(itest = 1, scanf("%d",&tests); itest <= tests; itest++) {

       scanf("%d",&p);
       int i,j;
       for(i = 0; i < (1<<p); i++) {
	   
	   scanf("%d", &m[i]); 
       }
       for(i = (1<<p) - 2; i >= 0; i--) {
	   scanf("%d", &c[i]); 
       }
       for(i = 0; i < (1<<(p-1)); i++) {
	   /*
	   for(j = 0; j < p; j++) {
	       dp[(1<<(p)) - 2 - i][j] = 0;
	   }
	   */
	   
	   dp[(1<<(p)) - 2 - i][min(m[2*i],m[2*i+1])] = c[(1<<(p))-2-i];

	   for(j = 0; j < min(m[2*i],m[2*i+1]); j++) {
		   dp[(1<<(p)) - 2 - i][j] = 0;
	   }
	   for(j = min(m[2*i],m[2*i+1])+1;j<=p; j++) {
		   dp[(1<<(p)) - 2 - i][j] = 100000000000000LL;
	   }
	   /*
	   printf("i=%d : ",(1<<p)-2-i);
	   for(j = 0; j < p; j++) printf("%d ",dp[(1<<(p)) - 2 - i][j]); puts("");
	   */
       }

       for(i = (1<<(p-1)) - 2; i >= 0; i--) {
	   for(j = 0; j <= p; j++) {
	       dp[i][j] = min( dp[2*i+2][j+1] + dp[2*i+1][j+1], dp[2*i+2][j] + dp[2*i+1][j] + c[i]);
	    //   printf("i=%d j=%d %d, c = %d,o = %d\n",i,j,dp[i][j],c[i], dp[2*i+2][j+1]+dp[2*i+1][j+1]);
	   }
	  // for(j = 0; j <= p; j++) printf("%d ",dp[i][j]); puts("");
       }

       printf("Case #%d: %lld\n", itest,dp[0][0]);//min(dp[0][0], dp[0][1]+c[0]));
   }
   return 0;
}
