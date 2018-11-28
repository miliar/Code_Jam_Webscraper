#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <ctype.h>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

char a[200][200];
int win[200];
int games[200];
double wp[200];
double owp[200];
double oowp[200];

int main() {
  int T, ca;
  int i, j, N;

  scanf("%d\n", &T );
  for ( ca = 1; ca <= T; ca++ )  {
    scanf("%d\n", &N );

    for ( i = 0; i < N; i++ )
      gets( a[i] );

    memset( games, 0, sizeof( games ) );
    memset( win, 0, sizeof( win ) );

    for ( i = 0; i < N; i++ )
      for ( j = 0; j < N; j++ )
	if ( a[i][j] == '1' ) {
	  games[i]++;
	  win[i]++;
	}
	else if ( a[i][j] == '0' ) {
	  games[i]++;
	}

    for ( i = 0; i < N; i++ ) {
      wp[i] = (double) win[i] / (double) games[i];
    }

    for ( i = 0; i < N; i++ ) {
      owp[i] = 0.0;
      for ( j = 0; j < N; j++ )
	if ( a[i][j] == '1' ) {
	  if ( games[j] > 0 )
	    owp[i] += (double) ( win[j] ) / (double) ( games[j] - 1.0 );
	}
	else if ( a[i][j] == '0' ) {
	  if ( games[j] > 0 )
	    owp[i] += (double) ( win[j] - 1.0 ) / (double) ( games[j] - 1.0 );
	}
      owp[i] /= (double) games[i];
    }

    for ( i = 0; i < N; i++ ) {
      oowp[i] = 0.0;
      for ( j = 0; j < N; j++ )
	if ( a[i][j] != '.' )
	  oowp[i] += owp[j];
      oowp[i] /= (double) games[i];
    }

    printf("Case #%d:\n", ca);
    for ( i = 0; i < N; i++ ) {
      printf("%.10lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] );
    }
  }

  return 0;
}
