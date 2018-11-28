#include <cstdio>
using namespace std;

bool com[110];
int num[110];
char buf[12];

int sgn( int x ) {
  if ( x == 0 ) return 0;
  return x < 0 ? -1 : 1;
} 

int main() {
  int tc;
  scanf( "%d", &tc );
  for ( int q=1; q<=tc; q++ ) {
    int n;
    scanf( "%d", &n );
    for ( int i=0; i<n; i++ ) scanf( "%s %d", buf, &num[i] ), com[i] = buf[0] == 'O';
    int c1 = 1;
    int c2 = 1;
    int i1 = 0, i2 = 0;
    for ( int day=0; ; day++ ) {
      while ( i1 < n && com[i1] ) i1++;
      while ( i2 < n && !com[i2] ) i2++;

      if ( i1 == n && i2 == n ) {
        printf( "Case #%d: %d\n", q, day );
        break;
      }

      if ( i1 < i2 ) {
        if ( c1 == num[i1] ) i1++;
        else c1 += sgn( num[i1] - c1 );
        c2 += sgn( num[i2] - c2 );
      } else {
        if ( c2 == num[i2] ) i2++;
        else c2 += sgn( num[i2] - c2 );
        c1 += sgn( num[i1] - c1 );
      }
    }
  }
}                        