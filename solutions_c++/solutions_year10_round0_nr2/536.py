#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

#define MaxN 1003

inline int gcd ( int a, int b ){ return b == 0 ? a : gcd ( b, a % b ); }

int test, t, N;
int V [ MaxN ];

int main ( void ){
  scanf("%d",&t);
  while ( t-- > 0 ){
    ++test;
    scanf("%d",&N);
    
    for ( int i = 0; i < N; ++i )
      scanf("%d",&V[i]);
    
    sort ( V, V + N );

    int g = V[1] - V[0];
    for ( int i = 1; i + 1 < N; ++i )
      g = gcd ( g, V[i+1] - V[i] );

    int first = ( V[0] / g ) * g;
    while ( first < V[0] )
      first += g;

    printf("Case #%d: %d\n",test,first-V[0]);
  }

  return 0;
}
