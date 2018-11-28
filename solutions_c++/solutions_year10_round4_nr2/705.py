#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <algorithm>

using namespace std;

const int inf = (int)1e+9;
const int pmax = 11;

int a[2 << pmax][pmax];
int p, n;
int cost[1 << pmax];
int M[1 << pmax];

int main()
{
    freopen ( "b.in", "rt", stdin );
    freopen ( "b.out", "wt", stdout );

    int test_cnt;
    cin >> test_cnt;
    for ( int test_id = 0; test_id < test_cnt; ++test_id )
    {
        cin >> p;
        n = ( 1 << p );
        for ( int i = 0; i < n; ++i )
            scanf ( "%d", &M[i] );
        int C = n - 2;
        for ( int j = p - 1; j >= 0; --j )
        {
            int lastC = C;
            for ( int i = 0; i < ( 1 << j ); ++i )
            {
                scanf ( "%d", &cost[C--] );
            }
            reverse ( cost + ( C + 1 ), cost + ( lastC + 1 ) );
        }
        for ( int index = 0; index < n; ++index )
            for ( int j = 0; j <= p; ++j )
                a[index + n - 1][j] = ( j >= p - M[index] ) ? 0 : inf;
        for ( int i = n - 2; i >= 0; --i )
            for ( int j = 0; j < p; ++j )
            {
                a[i][j] = min ( a[2*i + 2][j + 1] + a[2*i + 1][j + 1] + cost[i], a[2*i + 2][j] + a[2*i + 1][j] );
                if ( a[i][j] >= inf ) a[i][j] = inf;
            }

        printf ( "Case #%d: %d\n", test_id + 1, a[0][0] );
    }

    return 0;
}
