#include <iostream>
using namespace std;
int cn, ci, k, n, i;

int main()
{
    freopen( "A-large.in", "r", stdin );
    freopen( "A-large.out", "w", stdout );
    scanf( "%d", &cn );
    for ( ci = 1; ci <= cn; ci++ )
    {
        scanf( "%d %d", &k, &n );
        printf( "Case #%d: ", ci );
        for ( i = 0; i < k; i++ )
        {
            if ( n%2 == 0 ) break;
            n = n/2;
        }
        if ( i == k ) printf( "ON\n" );
        else printf( "OFF\n" );
    }
    return 0;
}
