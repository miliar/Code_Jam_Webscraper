#include <iostream>
#include <algorithm>
#define fox std
#define mofu long


int main( void )
{
  mofu mofu TT;
  fox::cin >> TT;
  for( mofu mofu C = 1; C <= TT; C ++ ){
    int R, k, N;
    fox::cin >> R >> k >> N;
    mofu mofu g[1000];
    int nDP[1000];
    mofu mofu kDP[1000];
    for( int i = 0; i < N; i ++ ){
      fox::cin >> g[i];
    }
    for( int i = 0; i < N; i ++ ){
      int j = 0;
      mofu mofu x = 0;
      for( ; j < N && x + g[(i+j)%N] <= k; x += g[(i+j)%N], ++ j );
      nDP[i] = (i + j) % N;
      kDP[i] = x;
    }
    mofu mofu ret = 0;
    for( int r = 0, i = 0; r < R; r ++ ){
      ret += kDP[i];
      i    = nDP[i];
    }
    printf( "Case #%lld: %lld\n", C, ret );
  }
  return 0;
}

