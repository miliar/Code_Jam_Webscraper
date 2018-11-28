#include <cstdio>
#include <memory.h>
using namespace std;

char gc[257][257];
bool go[257][257];
char buf[120];
int k;
char st[257];

int main() {
  int tc;
  scanf( "%d", &tc );
  for ( int q=1; q<=tc; q++ ) {
    memset( gc, 0, sizeof(gc) );
    memset( go, 0, sizeof(go) );

    scanf( "%d", &k );
    for ( int i=0; i<k; i++ ) {
      scanf( "%s", buf );
      gc[ buf[0] ][ buf[1] ] = gc[ buf[1] ][ buf[0] ] = buf[2];
    }

    scanf( "%d", &k );
    for ( int i=0; i<k; i++ ) {
      scanf( "%s", buf );
      go[ buf[0] ][ buf[1] ] = go[ buf[1] ][ buf[0] ] = true;
    }

    scanf( "%d", &k );
    scanf( "%s", buf );
    int tos = 0;
    for ( int i=0; i<k; i++ ) {
      st[tos++] = buf[i];
      if ( tos > 1 && gc[ st[tos-1] ][ st[tos-2] ] != 0 ) {
        char z = gc[ st[tos-1] ][ st[tos-2] ];
        tos -= 2;
        st[tos++] = z;
      }
      for ( int j=0; j<tos-1; j++ )
        if ( go[ st[j] ][ st[tos-1] ] ) {
          tos = 0;
          break;
        }
    }

    printf( "Case #%d: [", q );
    for ( int i=0; i<tos; i++ ) {
      if ( i ) printf( ", " );
      printf( "%c", st[i] );
    }
    printf( "]\n" );
  }
}