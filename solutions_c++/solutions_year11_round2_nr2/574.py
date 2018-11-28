#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <ctype.h>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int P[25];
int V[25];
int C, D;

double fabs( double x );

int can( double now ) {
  int i, j;
  double t;

  t = (double) P[0] - now;
  for ( i = 0; i < C; i++ ) {
    if ( t < P[i] - now ) {
      t = P[i] - now;
    }

    for ( j = 0; j < V[i]; j++ ) {
      if ( fabs( (double) P[i] - t ) > now + 1e-8 ) return 0;
      t += (double) D;
    }
  }

  return 1;
}

int main(){
  int T, ca, time, i;
  double h, t, m;

  scanf("%d\n", &T );

  for ( ca = 1; ca <= T; ca++ ) {
    scanf("%d %d\n", &C, &D );

    for ( i = 0; i < C; i++ ) {
      scanf("%d %d\n", &P[i], &V[i] );
    }

    h = 0.0;
    t = 1e10;

    for ( time = 0; time < 300; time++ ) {
      m = ( h + t ) / 2.0;

      if ( can( m ) ) {
	t = m;
      }
      else {
	h = m;
      }
    }

    printf("Case #%d: %lf\n", ca, t );
  }

  return 0;
}
