#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LEN 30

int t;
int len;
char s[MAX_LEN];

void Swap( char &_a, char &_b )
{
    char t = _a;
    _a = _b;
    _b = t;
}

bool Solve( int ind )
{
    if( ind == len - 1 ) return 0;
    if( Solve( ind + 1 ) ) return 1;
    char min = '9' + 1;
    int temp = -1;
    for( int i = ind + 1; i < len; ++i )
        if( s[i] < min && s[i] > s[ind] )
        {
            temp = i;
            min = s[i];
        }
    if( temp < 0 ) return 0;
    Swap( s[temp], s[ind] );
    for( int i = ind + 1; i < len; ++i )
        for( int j = i + 1; j < len; ++j )
            if( s[i] > s[j] ) Swap( s[i], s[j] );
    return 1;
}

int main( )
{
    freopen( "B-large.in", "r", stdin );
    freopen( "out.txt", "w", stdout );
    scanf( "%d", &t );
    for( int i = 1; i <= t; ++i )
    {
        scanf( "%s", s );
        len = strlen( s );
        if( Solve( 0 ) )
            printf( "Case #%d: %s\n", i, s );
        else
        {
            for( int i = 0; i < len; ++i )
                for( int j = i + 1; j < len; ++j )
                    if( s[i] > s[j] ) Swap( s[i], s[j] );
            for( int i = 0; i < len; ++i )
                if( s[i] != '0' )
                {
                    Swap( s[i], s[0] );
                    break;
                }
            printf( "Case #%d: %c0", i, s[0] );
            printf( "%s\n", s + 1 );
        }
    }
    return 0;
}
