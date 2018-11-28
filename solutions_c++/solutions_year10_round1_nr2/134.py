#include <stdio.h>

int g[256];
int c[1000];
int dp[1000][256];

inline int ABS(int x) {
   return x<0?-x:x;
}

int main() {
   int tt,t,n,M,I,D,i,j,k,d;
   scanf("%d",&tt);
   for( t=0; t<tt; t++ ) {
      scanf("%d %d %d %d",&D,&I,&M,&n);
      for( i=1; i<=n; i++ ) {
         scanf("%d",&c[i]);
      }
      g[0] = 0;
      for( i=1; i<256; i++ ) {
         g[i] = 100000000;
         for( j=0; j<i; j++ ) {
            if(g[j]+(i-j)<g[i]) g[i] = g[j]+(i-j);
            if(i-j<=M && g[j]+I<g[i]) g[i] = g[j]+I;
         }
      }
      for( i=0; i<256; i++ ) dp[0][i] = 0;
      for( i=1; i<=n; i++ ) {
         for( j=0; j<256; j++ ) {
            dp[i][j] = dp[i-1][j]+D;
         }
         for( k=0; k<256; k++ ) {
            d = 100000000;
            for( j=0; j<256; j++ ) {
               if(ABS(j-k)<=M && dp[i-1][j]<d) d = dp[i-1][j];
            }
            d+=ABS(k-c[i]);
            for( j=0; j<256; j++ ) {
               if(g[ABS(j-k)]+d<dp[i][j]) dp[i][j] = g[ABS(j-k)]+d;
            }
         }
         /*for( j=0; j<256; j++ ) {
            printf("%d ",dp[i][j]);
         }
         printf("\n");*/
      }
      d = 100000000;
      for( i=0; i<256; i++ ) {
         if(dp[n][i]<d) d = dp[n][i];
      }
      printf("Case #%d: %d\n",t+1,d);
   }
   return 0;
}
