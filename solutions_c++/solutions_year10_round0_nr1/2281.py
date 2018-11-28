#include <iostream>
#include <cstdio>
using namespace std;

void work( int t )
{
    int n, k;
    cin >> n >> k;
    long long x = ( 1 << n );
    cout << "Case #" << t << ": ";
    if( x == 0 )
    {
        cout << "OFF" << endl;
        return ;
    }

    if( ( k + 1 ) % x == 0 )
        cout << "ON" << endl;
    else
        cout << "OFF" << endl;
}


int main()
{
    freopen ( "A-large.in", "r" , stdin );
    freopen ( "A-large.out", "w", stdout );
    int t;
    cin >> t;
    for( int k = 0; k < t; k++ )
        work( k + 1 );

    return 0;
}

