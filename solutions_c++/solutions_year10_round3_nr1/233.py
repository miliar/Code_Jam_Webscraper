#include <cstdio>
#include <cstdlib>
#define MAX 1005

int A[MAX], B[MAX];

int solve() {
  int n;
  scanf("%d", &n);
  for( int i = 0; i < n; ++i ) 
    scanf("%d%d", &A[i], &B[i]);
  
  int cnt = 0;

  for( int i = 0; i < n; ++i ) 
    for( int j = i+1; j < n; ++j ) 
      if( A[i] > A[j] && B[i] < B[j]
|| A[i] < A[j] && B[i] > B[j] )
        ++cnt;

  return cnt;
}

int main() {
  int tc;
  scanf("%d", &tc);
  for( int i = 0; i < tc; ++i ) {
    printf("Case #%d: %d\n", i+1, solve());
  }
  return 0;
}
