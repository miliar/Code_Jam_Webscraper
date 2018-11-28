#include<iostream>
#include<math.h>
using namespace std;

struct Point{
    double x;
    double y;
    double r;
}point[45];

double di[50];

double dis( Point a, Point b ){
    return sqrt( ( a.x - b.x ) * ( a.x - b.x ) + ( a.y - b.y ) * ( a.y - b.y ) );
}

int main( ){
    int i, t, cas, mi, n;
    double r1, r2;
    freopen( "D-small-attempt2.in", "r", stdin );
    freopen( "D-small-attempt2.out", "w", stdout );
    scanf( "%d", &t );
    for( cas = 1; cas <= t; cas++ ){
        scanf( "%d", &n );
        for( i = 0; i < n; i++ )
            scanf( "%lf %lf %lf", &point[i].x, &point[i].y, &point[i].r );
        printf( "Case #%d: ", cas );
        if( n == 1 ){
            printf( "%.5lf\n", point[0].r );
            continue;
        }else if( n == 2 ){
            if( point[0].r > point[1].r )
                printf( "%.5lf\n", point[0].r );
            else
                printf( "%.5lf\n", point[1].r );
            continue;
        }
        mi = 1000000000;
        int u;
        for( i = 0; i < n; i++ ){
            di[i] = ( dis( point[i], point[(i + 1 ) % n]) + point[i].r + point[(i +1 ) %n].r ) / 2;
            if( mi > di[i] ){
                mi = di[i];
                u = i;
            }
        }
        if( u == 0 ){
            r2 = point[2].r;
            r1 = di[u];
            if( r1 > r2 ) printf( "%.5lf\n", r1 );
            else printf( "%.5lf\n", r1 );
        }else if( u == 1 ){
            r2 = point[0].r;
            r1 = di[u];
            if( r1 > r2 ) printf( "%.5lf\n", r1 );
            else printf( "%.5lf\n", r1 );
        }else{
            r2 = point[1].r;
            r1 = di[u];
            if( r1 > r2 ) printf( "%.5lf\n", r1 );
            else printf( "%.5lf\n", r1 );
        }

    }
    return 0;
}
