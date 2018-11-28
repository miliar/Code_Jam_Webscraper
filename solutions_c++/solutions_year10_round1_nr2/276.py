#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <algorithm>

using namespace std;

const int inf = (int)1e+9;

int a[101][257];
int v[101];
int D, I, m, n;

int main()
{
    freopen ( "b.in", "rt", stdin );
    freopen ( "b.out", "wt", stdout );

    int test_cnt;
    cin >> test_cnt;
    for ( int test_id = 0; test_id < test_cnt; ++test_id )
    {
        cin >> D >> I >> m >> n;
        for ( int i = 0; i < n; ++i )
            cin >> v[i];
        for ( int i = 0; i <= n; ++i )
            for ( int j = 0; j <= 256; ++j )
                a[i][j] = inf;
        a[0][256] = 0; // empty
        for ( int i = 0; i < n; ++i )
        {
            a[i + 1][256] = a[i][256] + D;
            for ( int j = 0; j < 256; ++j )
            {
                a[i + 1][j] = min ( a[i][j] + D, a[i][256] + abs ( j - v[i] ) );
                for ( int jj = max ( 0, j - m ); jj <= min ( 255, j + m ); ++jj )
                    a[i + 1][j] = min ( a[i + 1][j], a[i][jj] + abs ( j - v[i] ) );
            }

            bool done = false;
            while ( !done ) {
                done = true;
                for ( int j = 0; j < 256; ++j )
                    for ( int jj = max ( 0, j - m ); jj <= min ( 255, j + m ); ++jj )
                        if ( a[i + 1][j] > a[i + 1][jj] + I )
                            a[i + 1][j] = a[i + 1][jj] + I, done = false;
            }
        }

        int ans = inf;
        for ( int j = 0; j <= 256; ++j )
            ans = min ( ans, a[n][j] );
        printf ( "Case #%d: %d\n", test_id + 1, ans );
    }

    return 0;
}
