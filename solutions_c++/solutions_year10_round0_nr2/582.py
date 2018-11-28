#include <stdio.h>
#include<string.h>
#include <algorithm>
using namespace std;
long long a[3];

long long  hcf ( long long  a, long long  b )
{
    long long  r = 0;
    while ( b != 0 )
    {
        r = a % b;
        a = b;
        b = r;
    }
    return ( a );
}


int main () {

    freopen ( "C:\\B-small-attempt0.in", "r", stdin );
    freopen ( "C:\\B.out", "w", stdout );
    int i;
    int n, p;
    long long x, y, z;
    long long ans;

    scanf ( "%d", &p );

    for ( i = 1; i <= p; i++ )
    {
        scanf ( "%d", &n );
        for ( int j = 0; j < n; j++ )
            scanf ( "%I64d", &a[j] );
        sort ( a, a + n );
        ans = 0;
        if ( n == 2 )
        {
            x = a[1] - a[0];
        }
        if ( n == 3 )
        {
            y = a[1] - a[0];
            z = a[2] - a[0];
            x =  hcf ( y, z );
        }
        if ( a[0] % x == 0 )
            printf ( "0\n" );
        else
        {
            ans = x - a[0] % x;
            printf ( "%I64d\n", ans );
        }

    }
    return 0;
}


