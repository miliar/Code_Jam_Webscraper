#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

double a[3][3];
int t, n;

double Get( double r1, double r2, double dx, double dy )
{
    return ( sqrt( dx * dx + dy * dy ) + r1 + r2 ) / 2;
}
int main( )
{
    freopen( "in.txt", "r", stdin );
    freopen( "out.txt", "w", stdout );
    scanf( "%d", &t );
    for( int i = 1; i <= t; ++i )
    {
        scanf( "%d", &n );
        for( int j = 0; j < n; ++j )
            scanf( "%lf %lf %lf", &a[j][0], &a[j][1], &a[j][2] );
        printf( "Case #%d: ", i );
        if( n == 1 ) printf( "%lf\n", a[0][2] );
        else if( n == 2 )
        {
            double r1 = Get( a[0][2], a[1][2], a[0][0] - a[0][1], a[1][0] - a[1][1] );
            double r2 = 0;
            if( r2 < a[1][2] ) r2 = a[1][2];
            if( r2 < a[0][2] ) r2 = a[0][2];
            if( r1 > r2 ) r1 = r2;
            printf( "%lf\n", r1 );
        }
        else if( n == 3 )
        {
             double r0 = Get( a[0][2], a[1][2], a[0][0] - a[1][0], a[0][1] - a[1][1] );
             if( r0 < a[2][2] ) r0 = a[2][2];
             double r1 = Get( a[0][2], a[2][2], a[0][0] - a[2][0], a[0][1] - a[2][1] );
             if( r1 < a[1][2] ) r1 = a[1][2];
             double r2 = Get( a[1][2], a[2][2], a[1][0] - a[2][0], a[1][1] - a[2][1] );
             if( r2 < a[0][2] ) r2 = a[0][2];
             if( r0 > r1 ) r0 = r1;
             if( r0 > r2 ) r0 = r2;
             printf( "%lf\n", r0 );
        }
    }
    return 0;
}
