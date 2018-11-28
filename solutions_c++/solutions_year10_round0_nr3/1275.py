#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long llint;

const int MAX = 1010;

int R, K, n;
int gr[MAX];

int dist[MAX];
llint val[MAX];

pair<int,llint> next( int x ) {
  llint sum = 0;
  for( int i = x; ; i = (i+1)%n ) {
    sum += gr[i];
    if( sum > K ) return make_pair( i, sum-gr[i] );
  }
  return make_pair( x, 0LL );
}

int main( void ) {
  int tc; scanf( "%d", &tc );
  for( int t = 0; t < tc; ++t ) {
    scanf( "%d %d %d", &R, &K, &n );
    llint all = 0;
    for( int i = 0; i < n; ++i ) {
      scanf( "%d", &gr[i] );
      all += gr[i];
    }

    if( all <= K ) {
      printf( "Case #%d: %lld\n", t+1, all*R );
      continue;
    }

    int x = 0;
    int d = 0;
    llint cur = 0;
    for( int i = 0; i < n; ++i ) dist[i] = -1;

    while( 1 ) {
      if( dist[x] != -1 ) {
        llint w = cur - val[x];
        llint p = d - dist[x];
        cur += w*(R/p);
        R %= p;
      }
      if( R == 0 ) break;

      dist[x] = d;
      val[x] = cur;

      pair<int,llint> p = next( x );
      x = p.first;
      cur += p.second;
      --R, ++d;
    }

    printf( "Case #%d: %lld\n", t+1, cur );
  }
  return 0;
}

