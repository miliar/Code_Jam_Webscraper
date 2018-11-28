#include <cstdio>

char bio[5001][5001];
int memo[5001][5001];

int cnt( int n, int m ) {
   if( n == 0 ) return 1;
   if( n > m ) return 0;

   if( bio[n][m] ) return memo[n][m];
   bio[n][m] = 1;

   return memo[n][m] = cnt( n-1, m ) + cnt( n, m-1 );
}

int main( void ) {
   int sum = 0;
   for( int i = 1; i <= 5000; ++i ) sum += cnt( i, i );

   printf( "%d\n", sum );
   return 0;
}
