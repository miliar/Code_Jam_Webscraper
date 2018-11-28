#include <stdio.h>
#include <stdlib.h>

int c[101][101];

int main() {
   int tt,t,x1,y1,x2,y2,i,n,j,k,f,count;
   scanf("%d",&tt);
   for( t=0; t<tt; t++ ) {
      scanf("%d",&n);
      for( i=0; i<=100; i++ ) {
         for( j=0; j<=100; j++ ) {
            c[i][j] = 0;
         }
      }
      for( i=0; i<n; i++ ) {
         scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
         for( j=x1; j<=x2; j++ ) {
            for( k=y1; k<=y2; k++ ) {
               c[j][k] = 1;
            }
         }
      }
      f = 1;
      count = -1;
      while(f) {
         f = 0;
         for( i=100; i>0; i-- ) {
            for( j=100; j>0; j-- ) {
               if(c[i][j]) {
                  f = 1;
                  if(!c[i-1][j] && !c[i][j-1]) c[i][j] = 0;
               }else {
                  if(c[i-1][j] && c[i][j-1]) c[i][j] = 1;
               }
            }
         }
         count++;
      }
      printf("Case #%d: %d\n",t+1,count);
   }
   return 0;
}
