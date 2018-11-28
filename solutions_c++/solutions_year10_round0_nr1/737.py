#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    freopen ( "a.in", "rt", stdin );
    freopen ( "a.out", "wt", stdout );

    int test_cnt;
    cin >> test_cnt;
    for ( int test_id = 0; test_id < test_cnt; ++test_id )
    {
        int n, k;
        cin >> n >> k;
        printf ( "Case #%d: ", test_id + 1 );
        if ( ( k + 1 ) % ( 1 << n ) == 0 )
            printf ( "ON" );
        else
            printf ( "OFF" );
        printf ( "\n" );
    }

    return 0;
}


