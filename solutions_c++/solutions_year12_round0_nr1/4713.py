#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>

using namespace std;

#define MAXN 110

int T , len;
char s[MAXN];
char c;

char G ( char c ) {
     if ( c == '_' ) return ( '_' );
     if ( c == 'a' ) return ( 'y' );
     if ( c == 'b' ) return ( 'h' );
     if ( c == 'c' ) return ( 'e' );
     if ( c == 'd' ) return ( 's' );
     if ( c == 'e' ) return ( 'o' );
     if ( c == 'f' ) return ( 'c' );
     if ( c == 'g' ) return ( 'v' );
     if ( c == 'h' ) return ( 'x' );
     if ( c == 'i' ) return ( 'd' );
     if ( c == 'j' ) return ( 'u' );
     if ( c == 'k' ) return ( 'i' );
     if ( c == 'l' ) return ( 'g' );
     if ( c == 'm' ) return ( 'l' );
     if ( c == 'n' ) return ( 'b' );
     if ( c == 'o' ) return ( 'k' );
     if ( c == 'p' ) return ( 'r' );
     if ( c == 'q' ) return ( 'z' );
     if ( c == 'r' ) return ( 't' );
     if ( c == 's' ) return ( 'n' );
     if ( c == 't' ) return ( 'w' );
     if ( c == 'u' ) return ( 'j' );
     if ( c == 'v' ) return ( 'p' );
     if ( c == 'w' ) return ( 'f' );
     if ( c == 'x' ) return ( 'm' );
     if ( c == 'y' ) return ( 'a' );
     if ( c == 'z' ) return ( 'q' );
}

int main ( ) {

    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);

    scanf ( "%d" , &T );

    for ( int i = 1; i <= T; ++i ) {

     printf ( "Case #%d: " , i );

     do {
      scanf ( "%s" , s);
      scanf ( "%c" , &c );
      len = strlen(s);
      for ( int j = 0; j < len; ++j )
       printf ( "%c" , G(s[j]) );
      printf ( "%c" , c );
      //printf ( "%s%c" , s , c );
     }while ( c != '\n' );

    }

    return 0;

}


