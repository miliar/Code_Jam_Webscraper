/*
TASK: Snapper Chain
AUTHOR: Yordan Chaparov
*/

#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    int i, j;
    bool fl;
    int T, n;
    long long k;

    scanf( "%d", &T );
    for ( j = 1; j <= T; j++ )
    {
        scanf( "%d", &n );
        cin >> k;
//        cout << k << endl;
        i = 0;
        fl = 0;
        while ( k > 0 )
        {
//            cout << i << " " << k << " " << n << " " << fl << endl;
            if ( k % 2 == 0 )
            {
                fl = 0;
                break;
            }
            if ( i == n-1 )
            {
                fl = 1;
                break;
            }
            i++;
            k = k / 2;
        }

        printf( "Case #%d: ", j );
        if ( fl == 1 )
            printf( "ON\n" );
        else
            printf( "OFF\n" );
    }
    return 0;
}
