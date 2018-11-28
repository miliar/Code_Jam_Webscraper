#include <cstdio>

#include <algorithm>
using namespace std;

typedef long long llint;

int n;
llint L, H;
llint freq[10000];
llint lcm[10000];
llint gcd[10000];

llint mult( llint a, llint b ) {
   if( H/b < a ) return H+1;
   return a*b;
}

void update( llint &ans, llint w ) {
   if( w >= L && w <= H && w < ans ) ans = w;
}

llint povecaj( llint a, llint b ) {
   if( a >= L ) return a;

   llint x = L - L%a;
   while( x < L ) x += a;
   if( b == -1 ) return x;

   for( int i = 0; i < 100000000 && x <= H; x += a, ++i )
      if( b%x == 0 ) return x;
   return H+1;
}

int main( void ) {
   int tc;
   scanf( "%d", &tc );
   for( int t = 1; t <= tc; ++t ) {
      fprintf( stderr, "t = %d...\n", t );
      scanf( "%d %lld %lld", &n, &L, &H );
      for( int i = 0; i < n; ++i ) scanf( "%lld", &freq[i] );
      sort( freq, freq+n );

      lcm[0] = freq[0];
      for( int i = 1; i < n; ++i ) {
         llint g = __gcd( lcm[i-1], freq[i] );
         lcm[i] = mult( freq[i]/g, lcm[i-1] );
      }

      gcd[n-1] = freq[n-1];
      for( int i = n-2; i >= 0; --i )
         gcd[i] = __gcd( gcd[i+1], freq[i] );

      llint ans = H+1;
      update( ans, povecaj( lcm[n-1], -1 ) );
      update( ans, povecaj( 1, gcd[0] ) );

      for( int i = 0; i+1 < n; ++i ) {
         llint a = lcm[i];
         llint b = gcd[i+1];
         if( a <= b && b%a == 0 ) update( ans, povecaj( a, b ) );
      }

      printf( "Case #%d: ", t );
      if( ans >  H ) printf( "NO\n" );
      if( ans <= H ) printf( "%lld\n", ans );
   }
   return 0;
}

