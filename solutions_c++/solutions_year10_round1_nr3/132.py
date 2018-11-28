#include <stdio.h>

int dp[100][100];
int c[1000005];
int g[1000005];
long long s[1000005];

long long calc(long long x,long long y) {
   int tmp;
   long long w;
   if(x<y) {
      tmp = x;
      x = y;
      y = tmp;
   }
   if(y==0) return 0;
   w = g[x];
   if(y>=w) {
      return w*x-w*(w+1)/2+s[y]-s[w];
   }else {
      return y*x-y*(y+1)/2;
   }
   return 0;
}

int main() {
   int tt,t,r,i,j,k,a1,a2,b1,b2;
   c[0] = 1;
   r = 1;
   for( i=0,j=1; j<1000005; i++ ) {
      if(c[i]==1) {
         c[j++] = 2;
         c[j++] = 1;
      }else {
         c[j++] = 2;
         c[j++] = 2;
         c[j++] = 1;
      }
   }
   for( i=0,j=1,k=0; j<1000005; i++ ) {
      if(c[i]==1) {
         g[j++] = k++;
      }else {
         g[j++] = k;
         g[j++] = k++;
      }
   }
   s[0] = 0;
   for( i=1; i<1000005; i++ ) {
      s[i] = s[i-1]+g[i];
   }
   scanf("%d",&tt);
   for( t=0; t<tt; t++ ) {
      scanf("%d %d %d %d",&a1,&a2,&b1,&b2);
      printf("Case #%d: %lld\n",t+1,calc(a2,b2)-calc(a1-1,b2)-calc(a2,b1-1)+calc(a1-1,b1-1));
   }
   return 0;
}
