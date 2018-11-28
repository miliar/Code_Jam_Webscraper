#include <stdio.h>
#include <stdlib.h>

int c[1024];
int g[1024];
int dp[1024][11];
int n;

int calc(int p,int x) {
   if(dp[p][x]!=-1) {
      return dp[p][x];
   }
   int d,i,j,s;
   dp[p][x] = 100000000;
   for( i=0; i<=n; i++ ) {
      for( j=0; j<=n; j++ ) {
         d = i>j?i:j;
         if(d<=x) {
            s = calc(p*2,i)+calc(p*2+1,j);
            if(s<dp[p][x]) dp[p][x] = s;
         }else if(d-1==x) {
            s = calc(p*2,i)+calc(p*2+1,j)+g[p];
            if(s<dp[p][x]) dp[p][x] = s;
         }
      }
   }
   return dp[p][x];
}

int main() {
   int tt,t,i,j,k,r,d,md;
   scanf("%d",&tt);
   for( t=0; t<tt; t++ ) {
      scanf("%d",&n);
      r = (1<<n);
      for( i=0; i<r; i++ ) {
         scanf("%d",&c[i]);
      }
      k = r;
      for( i=n-1; i>=0; i-- ) {
         d = (1<<i);
         k/=2;
         for( j=0; j<d; j++ ) {
            scanf("%d",&g[k+j]);
         }
      }
      for( j=1; j<r; j++ ) {
         for( k=0; k<=n; k++ ) {
            dp[j][k] = -1;
         }
      }
      for( k=0; k<r; k+=2 ) {
         i = k/2+(1<<(n-1));
         d = n-c[k]>n-c[k+1]?n-c[k]:n-c[k+1];
         for( j=0; j<d-1; j++ ) {
            dp[i][j] = 1000000000;
         }
         if(d) dp[i][d-1] = g[i];
         for( j=d; j<=n; j++ ) {
            dp[i][j] = 0;
         }
      }
      printf("Case #%d: %d\n",t+1,calc(1,0));
   }
   return 0;
}
