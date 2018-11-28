#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 1001;

int g[ MAXN ] = { 0 };
double once[ MAXN ] = { 0 };
int oncek[ MAXN ] = { 0 };

double runOnce( int &nextGroup, double lim, int n )
{
    double now = 0;
    int num = 0;
    while( 1 )
    {
        if( now + g[ nextGroup ] > lim || num >= n )
            break;
        now += g[ nextGroup ];
        nextGroup++;
        nextGroup %= n;
        num++;
    }

    return now;
}

void run( int t )
{
    memset( g, 0, sizeof( g ) );
    memset( oncek, 0, sizeof( oncek ) );

    int r, n;
    double lim;
    cin >> r >> lim >> n;

    for( int k = 0; k < n; k++ )
        once[ k ] = 0;

    for( int k = 0; k < n; k++ )
        cin >> g[ k ];

    for( int k = 0; k < n; k++ )
    {
        int x = k;
        once[ k ] = runOnce( x, lim, n );
        oncek[ k ] = x;
    }

    double total = 0;
    int nextGroup = 0;
    for( int k = 0; k < r; k++ )
    {
        total += once[ nextGroup ];
        nextGroup = oncek[ nextGroup ];
    }
    printf( "Case #%d: %.0lf\n", t, total );
}


void work( int t )
{
    memset( g, 0, sizeof( g ) );
    memset( once, 0, sizeof( once ) );

    int r, lim, n;
    cin >> r >> lim >> n;

    for( int k = 0; k < n; k++ )
        cin >> g[ k ];

    int total = 0;
    int nextGroup = 0;
    for( int k = 0; k < r; k++ )
    {
        int now = 0;
        int num = 0;
        while( 1 )
        {
            if( now + g[ nextGroup ] > lim || num >= n )
                break;
            now += g[ nextGroup ];
            nextGroup++;
            nextGroup %= n;
            num++;
        }

        total += now;
    }
    cout << "Case # "<< t <<": " << total << endl;
}

int main()
{
    freopen ( "C-small-attempt0.in", "r" , stdin );
    freopen ( "C-small-attempt0.out", "w", stdout );
    int t;
    cin >> t;
    for( int k = 0; k < t; k++ )
        run( k + 1 );

    return 0;
}

