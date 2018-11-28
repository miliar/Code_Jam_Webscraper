#include <stdio.h>
#include <stdlib.h>

int map[100][100];
int tmp[100][100];

int main() {
   int tt,t,n,i,j,k,h,f,a[4],x,y;
   scanf("%d",&tt);
   for( t=0; t<tt; t++ ) {
      scanf("%d",&n);
      for( i=0; i<n; i++ ) {
         for( j=0; j<=i; j++ ) {
            scanf("%d",&map[i-j][j]);
         }
      }
      for( i=n-1; i>=0; i-- ) {
         for( j=1; j<=i; j++ ) {
            scanf("%d",&map[n-j][j+n-i-1]);
         }
      }
      for( h=0; h<4; h++ ) {
         for( i=n; i>=1; i-- ) {
            f = 1;
            for( j=0; j<i; j++ ) {
               for( k=0; k<i; k++ ) {
                  if(map[j][k]!=map[i-k-1][i-j-1]) {
                     f = 0;
                     goto out;
                  }
               }
            }
out:
            if(f) break;
         }
         a[h] = i;
         for( i=0; i<n; i++ ) {
            for( j=0; j<n; j++ ) {
               tmp[i][j] = map[i][j];
            }
         }
         for( i=0; i<n; i++ ) {
            for( j=0; j<n; j++ ) {
               map[i][j] = tmp[j][n-i-1];
            }
         }
      }
      x = a[0]>a[2]?a[0]:a[2];
      y = a[1]>a[3]?a[1]:a[3];
      printf("Case #%d: %d\n",t+1,(n-x+n-y+n)*(n-x+n-y+n)-n*n);
   }
   return 0;
}
