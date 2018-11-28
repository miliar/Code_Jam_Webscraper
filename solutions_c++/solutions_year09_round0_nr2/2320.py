#include <iostream>

using namespace std;

int di[4] = {-1,0,0,1}, dj[4] = {0,-1,1,0};
int a[110][110], b[110][110], nt, n, m, rx, ry, k, x, y, cur;

void filling() {
   char h[100],ch; int k = 0;

   for ( int i = 1; i <= 50; i++ ) 
      h[i] = ' ';


   for ( int i = 1; i <= n; i++ ) {
      for ( int j = 1; j <= m; j++ ) {
         if ( h[b[i][j]] == ' ' ) {
            k++;
            h[b[i][j]] = char(int('a') + k - 1);
         }
         ch = h[b[i][j]];
         printf("%c", ch);
         if ( j < m ) printf(" ");
      }
      printf("\n");
   }

}

void find_way(int x, int y) {

   if ( b[x][y] != 0 ) {
      cur = b[x][y];
      return;
   }

   rx = x; ry = y;

   for ( int i = 0; i < 4; i++ ) {
      int i1 = x+di[i], j1 = y+dj[i];

      if (( i1 >= 1 ) &&  ( i1 <= n ) && (j1 >= 1) && (j1 <= m))
         if ( a[i1][j1] < a[rx][ry] ) {
            rx = i1; 
            ry = j1;
         }
   }

   if (( rx == x ) && ( ry == y )) {
      k++;
      cur = k;
      b[rx][ry] = cur;
      return;
   } else 
      find_way(rx, ry);

   
   b[x][y] = cur;
   return;
}


int main() {
   freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
   scanf("%d", &nt);
   for ( int t = 1; t <= nt; t++ ) {
      scanf("%d%d", &n, &m);
      for ( int i = 1; i <= n; i++ ) 
         for ( int j = 1; j <= m; j++ )
            scanf("%d", &a[i][j]);

      memset(b,0,sizeof(b));
      
      k = 0;

      for ( int i = 1; i <= n; i++ )
         for ( int j = 1; j <= m; j++ ) {
            x = i; y = j;
            find_way(x,y);
         }

      printf("Case #%d:\n", t);
      filling();

   }
   return 0;
}
