#include <cstdio>
#include <algorithm>

using namespace std;

int main(void) {
  int T, A, B, n, m;
  
  scanf("%d", &T);
  for ( int t = 1; t <= T; ++t ) {
    int result = 0;
    scanf("%d%d", &A, &B);

    int k = 1, pot10 = 1;    
    n = A;
    for (;;) {
      n /= 10;
      if ( !n ) break;
      ++k;
      pot10 *= 10;
    }
    
    for ( n = A; n < B; ++n ) {
      m = n;
      for ( int i = 1; i < k; ++i ) {
        m = m / 10 + (m % 10) * pot10;

        if ( m == n ) break; // repetition
        if ( n > m || m > B ) continue;        
        
        ++result;
      }
    }
    printf("Case #%d: %d\n", t, result);
    fprintf(stderr, "Case #%d: %d\n", t, result);
  }
  return 0;
}
