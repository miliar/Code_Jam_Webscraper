
#include <cstdio>
#include <cstring>

int N, D, L;
char w[5010][20], buf[1010], has[100][256];

int main() {
//  freopen("A-large.in", "r", stdin);  
//  freopen("A-large.out", "w", stdout);
    
  int res = 0, x = 0;

  scanf("%d %d %d", &L, &D, &N);
  for ( int i = 1; i <= D; ++i )
    scanf("%s", w[i] + 1);
  
  for ( int i = 1; i <= N; ++i ) {
    scanf("%s", buf + 1);
    memset( has, 0, sizeof( has ) );
    res = 0;
    
    //printf("%s\n", buf + 1);
    
    
    x = 1;
    for ( int j = 1; j <= L; ++j ) {
      if ( buf[x] != '(' ) {
        has[j][ buf[x]-'a' ] = 1;
        ++x;   
      } else {
        ++x;
        while ( buf[x] != ')' ) {
          has[j][ buf[x] - 'a' ] = 1;
          ++x;      
        }
        ++x; 
      }
    }
    
    //printf("aloha\n");
    //return 0;
    
    for ( int j = 1; j <= D; ++j ) {
      bool bOk = true;
      for ( int k = 1; bOk && k <= L; ++k )
        if ( !has[k][ w[j][k] - 'a' ] )
          bOk = false;    
      if ( bOk )
        ++res;
    }
    
    printf("Case #%d: %d\n", i, res);
  }  
    
  return 0;    
}
