#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <algorithm>

using namespace std;

const int nmax = 1001;

int R, k, n;
int g[nmax];
int u[nmax];
long long price[nmax];

int main()
{
    freopen ( "c.in", "rt", stdin );
    freopen ( "c.out", "wt", stdout );

    int test_cnt;
    cin >> test_cnt;
    for ( int test_id = 0; test_id < test_cnt; ++test_id )
    {
        scanf ( "%d%d%d", &R, &k, &n );
        long long s = 0;
        for ( int i = 0; i < n; ++i )
        {
            scanf ( "%d", &g[i] );
            s += g[i];
        }
        
        memset ( u, -1, sizeof ( u ) );
        int c = 0, step = 0;
        while ( u[c] == -1 )
        {
            u[c] = step;
            price[step] = 0;
            for ( int cc = 0, kk = k; cc < n && kk >= g[c]; ++cc )
                price[step] += g[c], kk -= g[c], c = ( c + 1 ) % n;

            step++;
        }

        long long ret = 0, period = 0;
        for ( int i = 0; i < min ( R, step ); ++i )
        {
            if ( i < u[c] )
                ret += price[i];
            else
                period += price[i];
        }
        if ( R <= step )
            ret += period;
        else
        {
            int t = ( ( R - u[c] ) / ( step - u[c] ) );
            ret += t*period;
            R -= t*( step - u[c] );
            for ( int i = u[c]; i < R; ++i )
                ret += price[i];
        }
        
        printf ( "Case #%d: ", test_id + 1 );
        cout << ret << endl;
    }

    return 0;
}
