#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_N 51
#define MAX_LEN 51

int n, t;
int a[MAX_N];
char s[MAX_LEN];

inline void Swap( int &_a, int &_b ) { int _t = _a; _a = _b; _b = _t; }
int main( )
{
    freopen( "in.txt", "r", stdin );
    freopen( "out.txt", "w", stdout );
    scanf( "%d", &t );
    for( int m = 1; m <= t; ++m )
    {
        scanf( "%d", &n );
        memset( a, 0, sizeof( a ) );
        for( int i = 0; i < n; ++i )
        {
            scanf( "%s", s );
            for( int j = n - 1;j >= 0; --j )
                if( s[j] == '1' ) { a[i] = j; break; }
        }
        int count = 0;
        for( int i = 0; i < n; ++i )
        {
            for( int j = i; j < n; ++j )
                if( a[j] <= i )
                {
                    for( int k = j; k > i; --k )
                        Swap( a[k], a[k-1] ), count++;
                    break;
                }
        }
        printf( "Case #%d: %d\n", m, count );
    }
    
}
