
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int T, N, P, Q[111];

int brute() {
  int A[111], res = (1<<30);
  char u[111];
  
  for ( int i = 1; i <= N; ++i )
    A[i] = i;
    
  do {
    int cur = 0;
  
    for ( int i = 1; i <= P; ++i )
      u[i] = 1;
    u[0] = u[P+1] = 0;
  
    for ( int i = 1; i <= N; ++i ) {
      for ( int x = Q[ A[i] ] - 1; x >= 1 && u[x]; --x )
        ++cur;
      for ( int x = Q[ A[i] ] + 1; x <= P && u[x]; ++x )
        ++cur;
      u[ Q[ A[i] ] ] = 0;
    }
    
    if ( cur < res )
      res = cur;
      
  } while ( next_permutation( A + 1, A + N + 1 ) );

  return res;
}

int main() {
  freopen("C-small-attempt0.in", "r", stdin);
  freopen("C-small-attempt0.out", "w", stdout);

  scanf("%d", &T);
  
  for ( int i = 1; i <= T; ++i ) {
    printf("Case #%d: ", i);
    
    scanf("%d %d", &P, &N);
    for ( int i = 1;  i <= N; ++i )
      scanf("%d ", Q + i);
      
    sort(Q + 1, Q + N + 1);
    
    printf("%d\n", brute());
  }

  return 0;
}
