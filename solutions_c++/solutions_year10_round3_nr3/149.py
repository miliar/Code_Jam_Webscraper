#include <iostream>
#include <cstring>
using namespace std;

int n, m;
char row[512];
int dp[512][512];
bool b[512][512];
bool us[512][512];
bool ok[512][512][512];
int sol[512];

int main()
{
    int i, j, k;
    int l, a, bk;
    int neus;
    int T;
    int bi, bj;
    scanf( "%d", &T );
    for ( int tt = 1; tt <= T; tt++ )
    {
        scanf ( "%d %d", &m, &n );
        for ( i = 1; i <= m; i++ )
        {
            scanf( "%s", &row );
            for ( j = 0; j < n/4; j++ )
            {
                if ( ( row[j] >= '0' ) && ( row[j] <= '9' ) )
                    a = row[j] - '0';
                else
                    a = 10 + row[j] - 'A';
                for ( l = 4; l > 0; l-- )
                {
                    b[i][4*j+l] = a % 2;
                    a = a / 2;
                }
            }
        }

        memset( us, 0, sizeof( us ) );
        memset( sol, 0, sizeof( sol ) );
        neus = 0;
        while ( neus < n*m )
        {
//            cout << neus << endl;
            for ( i = 1; i <= m; i++ )
            {
                for ( j = n; j > 0; j-- )
                {
                    if ( ( j < n ) && ( b[i][j+1] != b[i][j] ) )
                        dp[i][j] = dp[i][j+1] + 1;
                    else
                        dp[i][j] = 1;

                    if ( us[i][j] == 1 )
                        dp[i][j] = 0;
//                    cout << "DP " << i << " " << j << " " << dp[i][j] << endl;
                }
            }

            bk = -1;
            bi = -1;
            bj = -1;
            for ( i = 1; i <= m; i++ )
            {
                for ( j = 1; j <= n; j++ )
                {
                    k = dp[i][j];
                    if ( dp[i][j] > 0 )
                    {
                        if ( bk < 0 )
                        {
                            bk = 0;
                            bi = i;
                            bj = j;
                        }
                    }
                    if ( us[i][j] == 1 )
                        continue;
                    for ( l = 1; ( i + l <= m ) && ( j + l <= n ) && ( l+1 <= k ); l++ )
                    {
                        if ( b[i+l-1][j] == b[i+l][j] )
                            break;
                        k = min( k, dp[i+l][j] );
                        if ( l + 1 <= k )
                        {
                            if ( bk < l )
                            {
                                bk = l;
                                bi = i;
                                bj = j;
                            }
                        }
                    }
                }
            }
            if ( bk >= 0 )
            {
                sol[bk+1]++;
//                cout << bk << " " << bi << " " << bj << endl;
                for ( i = bi; i <= bi + bk; i++ )
                {
                    for ( j = bj; j <= bj + bk; j++ )
                    {
                        us[i][j] = 1;
//                        cout << "US " << i << " " << j << endl;
                        neus++;
                    }
                }
            }
        }

        k = 0;
        for ( i = 1; i <= 512; i++ )
        {
            if ( sol[i] > 0 )
                k++;
        }
        printf( "Case #%d: %d\n", tt, k );
        for ( i = 512; i > 0; i-- )
        {
            if ( sol[i] > 0 )
            {
                printf( "%d %d\n", i, sol[i] );
            }
        }
    }
    return 0;
}
