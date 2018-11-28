#include <iostream>

using namespace std;

char s[1000]; string s1;

int a[600][30], sum, i, j, n, nt, ans;

int main() {
   freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

   s1 = "welcome to code jam";

   scanf("%d\n", &nt);

   for ( int t = 1; t <= nt; t++ ) {
      gets(s); n = strlen(s);

      memset(a,0,sizeof(a)); a[0][0] = 1;

      for ( j = 1; j <= s1.length(); j++ ) {
         sum = 0;
         for ( i = 1; i <= n; i++ ) {
            sum = (sum + a[i-1][j-1]) % 10000;
            
            if ( s[i-1] == s1[j-1] ) {
               a[i][j] = (a[i][j] + sum) % 10000;   
            }
         }
      }

      printf("Case #%d: ", t);

      ans = 0;

      for ( i = 1; i <= n; i++ ) 
         ans = ( ans + a[i][s1.length() ] ) % 10000;

      printf("%04d\n", ans);
   }
      
   return 0;
}
