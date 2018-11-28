#include <cstring>
#include <cstdio>
const int MAXN = 1010;

typedef long long int llint;

int rounds, k, n;
int g[ MAXN ];
int next[ MAXN ];
llint sum_next[ MAXN ];
llint bio[ MAXN ];
int kad[ MAXN ];
llint total_sum;

llint sol;

void input( void ) {
  total_sum = 0;
  scanf( "%d%d%d", &rounds, &k, &n );
  
  for( int i = 0; i < n; ++i ) {
    scanf( "%d", g+i );
    total_sum += g[i];
  }

  if( total_sum < k ) throw 0xC;
}

void preprocess( void ) {
  llint sum = 0;
  int j = 0;
  bool finished = false;
  
  for( int i = 0; !finished; ++i ) {
    sum += g[i%n];

    while( sum > k ) {
      next[j] = i%n;
      sum_next[j] = sum - g[i%n];
      sum -= g[j];
      if( ++j == n ) {
        finished = true;
        break;
      }
    }
  }
}

llint solve( void ) {
  int gdje = 0;
  llint sum = 0;
  int i;
  
  memset( bio, -1, sizeof( bio ) ); 
  memset( kad, -1, sizeof( kad ) ); 
  
  for( i = 0; i < rounds; ++i ) {
    if( kad[ gdje ] != -1 ) break;
    bio[gdje] = sum;
    kad[gdje] = i;
    
    sum += sum_next[gdje];
    gdje = next[gdje];
  }

  if( i == rounds ) return sum;
  llint cycle_sum = sum - bio[gdje];
  int cycle_len = i - kad[gdje];

  for( ; i + cycle_len < rounds; i += cycle_len )
    sum += cycle_sum;
  
  for( ; i < rounds; ++i ) {
    sum += sum_next[ gdje ];
    gdje = next[ gdje ];
  }
  
  return sum;
}

int main( void ) {
  int t;
  scanf( "%d", &t );
 
  for( int i = 0; i < t; ++i ) {
    try {
      input();
      preprocess();
      printf( "Case #%d: %lld\n", i+1, solve() );
    } catch( int x ) {
      printf( "Case #%d: %lld\n", i+1, rounds * total_sum );
    }
  }
  
  return 0;
}

