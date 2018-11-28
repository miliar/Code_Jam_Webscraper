#include <stdio.h>

char str[101][101];
char map[100][100];
int mm[4][2]={{0,1},{1,-1},{1,0},{1,1}};

int main() {
   int tt,t,n,m,i,j,k,h,x,y,B,R;
   scanf("%d",&tt);
   for( t=0; t<tt; t++ ) {
      scanf("%d %d",&n,&m);
      for( i=0; i<n; i++ ) {
         scanf("%s",str[i]);
      }
      for( i=0; i<n; i++ ) {
         for( j=0; j<n; j++ ) {
            map[j][n-i-1] = 0;
         }
         k = n-1;
         for( j=n-1; j>=0; j-- ) {
            if(str[i][j]=='B') {
               map[k--][n-i-1] = 1;
            }else if(str[i][j]=='R') {
               map[k--][n-i-1] = 2;
            }
         }
      }
      B = R = 0;
      for( i=0; i<n; i++ ) {
         for( j=0; j<n; j++ ) {
            if(map[i][j]) {
               for( k=0; k<4; k++ ) {
                  x = i;
                  y = j;
                  h = 0;
                  while(x>=0 && y>=0 && x<n && y<n && map[x][y]==map[i][j]) {
                     h++;
                     x+=mm[k][0];
                     y+=mm[k][1];
                  }
                  if(h>=m) {
                     if(map[i][j]==1) {
                        B = 1;
                     }else {
                        R = 1;
                     }
                  }
               }
            }
         }
      }
      printf("Case #%d: ",t+1);
      if(B) {
         if(R) {
            puts("Both");
         }else {
            puts("Blue");
         }
      }else {
         if(R) {
            puts("Red");
         }else {
            puts("Neither");
         }
      }
   }
   return 0;
}
