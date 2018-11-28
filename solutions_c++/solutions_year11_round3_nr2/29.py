#include <cstdio>

#include <set>
using namespace std;

typedef long long llint;

int L, T, N, C;
int dist[1000];

int main( void ) {
   int tc;
   scanf( "%d", &tc );
   for( int t = 1; t <= tc; ++t ) {
      scanf( "%d %d %d %d", &L, &T, &N, &C );
      for( int i = 0; i < C; ++i ) scanf( "%d", &dist[i] );

      multiset<int> S;
      for( int i = 0; i < N; ++i ) S.insert( dist[i%C] );

      llint ans = 0;
      for( int i = 0; i < N; ++i ) {
         S.erase( S.find( dist[i%C] ) );
         if( ans + 2*dist[i%C] <= T ) {
            ans += 2*dist[i%C];
         } else {
            if( (T-ans) % 2 == 0 ) {
               int a = (T-ans)/2;
               int b = dist[i%C] - a;
               ans += 2*a;
               S.insert( b );
            } else {
               ans += 2*dist[i%C];
            }
            break;
         }
      }

      for( ; L > 0 && !S.empty(); --L ) {
         ans += *(--S.end());
         S.erase( --S.end() );
      }

      while( !S.empty() ) {
         ans += 2 * (*S.begin());
         S.erase( S.begin() );
      }

      printf( "Case #%d: %lld\n", t, ans );
   }
   return 0;
}

