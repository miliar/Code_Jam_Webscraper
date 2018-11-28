
#include <cstdio>
#include <cstring>

char w[] = "welcome to code jam";
char buf[1010];
int N, L, dp[511][35];


int main() {
  freopen("C-large.in", "r", stdin);
  freopen("C-large.out", "w", stdout);

  scanf("%d \n", &N);
  for ( int i = 1; i <= N; ++i ) {
    memset(dp, 0, sizeof(dp) );
  
    gets( buf );
    
    for ( int j = 0; j < strlen(w); ++j ) {
      for ( int k = 0; k < strlen(buf); ++k ) {
        if ( buf[k] == w[j] ) {
          //printf("%d - %d: %c\n", j, k, buf[k]);
          if ( j > 0 ) {
            for ( int o = 0; o < k; ++o ) 
              dp[k][j] += dp[o][j-1],
              dp[k][j] %= 10000;
          } else {
            dp[k][j]++;
          }
        }
      }
    }
    
    int res = 0;
    
    for ( int k = 0; k < strlen( buf ); ++k )
      res += dp[k][strlen(w)-1],
      res %= 10000;
      
    printf("Case #%d: %.4d\n", i, res);
  }

  return 0;
}
