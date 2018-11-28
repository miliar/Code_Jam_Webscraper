#include <cstdio>
#include <cstring>

int T, N;
char m[ 200 ][ 200 ];

int win[ 200 ];
int tot[ 200 ];
double OWP[ 200 ];

int main( void )
{
  scanf( "%d", &T );

  for( int tc = 1; tc <= T; ++tc ) {
    scanf( "%d", &N );

    for( int i = 0; i < N; ++i ) {
      scanf( "%s", m[i] );
      tot[i] = win[i] = 0;

      for( int j = 0; j < N; ++j ) {
	if( m[i][j] == '.' ) continue;
	win[i] += m[i][j]-'0';
	tot[i] += 1;
      }
    }

    for( int i = 0; i < N; ++i ) {
      OWP[i] = 0.0;

      for( int j = 0; j < N; ++j ) {
	if( m[i][j] == '.' ) continue;
	OWP[i] += double( win[j] - ( m[j][i]-'0' ) ) / double( tot[j]-1 );
      }

      OWP[i] /= double( tot[i] );
    }

    printf( "Case #%d:\n", tc );

    for( int i = 0; i < N; ++i ) {
      double WP = double( win[i] ) / double( tot[i] );
      double OOWP = 0.0;

      for( int j = 0; j < N; ++j ) {
	if( m[i][j] == '.' ) continue;
	OOWP += OWP[j];
      }

      OOWP /= double( tot[i] );

      printf( "%.6lf\n", 0.25*WP + 0.5*OWP[i] + 0.25*OOWP );
    }
  }


  return 0;
}
  
