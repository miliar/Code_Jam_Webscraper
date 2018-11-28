#include <cstdio>
#include <cstring>

const char alph[] = "yhesocvxduiglbkrztnwjpfmaq";

int T;
char buff[ 105 ];

int main( void )
{
  scanf( "%d\n", &T );

  for( int tc = 1; tc <= T; ++tc ) {
    printf( "Case #%d: ", tc );

    gets( buff ); 
    int n = strlen( buff );

    for( int j = 0; j < n; ++j ) {
      if( buff[j] != ' ' ) putchar( alph[buff[j] - 'a'] );
      else putchar( ' ' );
    }

    putchar( '\n' );
  }
  
  return 0;
}
