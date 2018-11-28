#include <cstdio>
#include <cstring>

#include <stack>
using namespace std;

int C, D;
int komb[256][256];
int opp[256][256];

int n, m;
char str[101];
char stk[101];

int ima( char c ) {
   for( int i = 0; i <= m; ++i )
      if( stk[i] == c )
         return 1;
   return 0;
}

int main( void ) {
   int tc;
   scanf( "%d", &tc );
   for( int t = 1; t <= tc; ++t ) {
      scanf( "%d", &C );
      memset( komb, 0, sizeof komb );
      for( int i = 0; i < C; ++i ) {
         char s[4];
         scanf( "%s", s );
         komb[s[0]][s[1]] = s[2];
         komb[s[1]][s[0]] = s[2];
      }

      scanf( "%d", &D );
      memset( opp, 0, sizeof opp );
      for( int i = 0; i < D; ++i ) {
         char s[3];
         scanf( "%s", s );
         opp[s[0]][s[1]] = 1;
         opp[s[1]][s[0]] = 1;
      }

      scanf( "%d", &n );
      scanf( "%s", str );

      m = -1;
      for( int i = 0; i < n; ++i ) {
         if( m < 0 ) {
            stk[++m] = str[i];
         } else if( komb[stk[m]][str[i]] ) {
            stk[m] = komb[stk[m]][str[i]];
         } else {
            int ok = 1;
            for( int c = 0; c < 256; ++c )
               if( opp[c][str[i]] && ima( c ) )
                  ok = 0;
            
            if( ok ) stk[++m] = str[i];
            else m = -1;
         }
      }

      printf( "Case #%d: [", t );
      for( int i = 0; i <= m; ++i ) {
         if( i > 0 ) printf( ", " );
         printf( "%c", stk[i] );
      }
      printf( "]\n" );
   }
   return 0;
}

