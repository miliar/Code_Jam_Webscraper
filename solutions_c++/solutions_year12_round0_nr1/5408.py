#include <cstdio>
#include <cctype>
#include <cstring>
#include <map>

using namespace std;

int main() {
    map< char, char > m;
    char c;
    int N;

    const char *s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y e q z";
    const char *s2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a o z q";
    int l = strlen( s1 );

    for ( int i = 0; i < l; ++i ) {
        m[ s1[ i ] ] = s2[ i ];
    }

    FILE *fo = fopen( "inp.in", "r" );
    FILE *fi = fopen( "output.out", "w" );
    fscanf( fo, "%d\n", &N );
    for ( int i = 1; i <= N; ++i ) {
        fprintf( fi, "Case #%d: ", i );
        do {
            fscanf( fo, "%c", &c );
            if ( isalpha( c ) ) {
                fprintf( fi, "%c", m[ c ] );
            }
            else {
                fprintf( fi, "%c", c );
            }
        } while ( c != '\n' );
    }

    return 0;
}