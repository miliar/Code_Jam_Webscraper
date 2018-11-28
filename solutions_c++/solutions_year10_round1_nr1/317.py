#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <algorithm>

using namespace std;

const int inf = (int)1e+9;
const int nmax = 51;
const int dx[] = { 1, 1, 0, -1 };
const int dy[] = { 0, 1, 1, 1  };

int a[nmax][nmax];
int b[nmax][nmax];
int n, k;

bool same ( int x, int y )
{
    for ( int c = 0; c < 4; ++c )
    {
        int i;
        for ( i = 0; i < k; ++i )
        {
            int nx = x + dx[c]*i;
            int ny = y + dy[c]*i;
            if ( nx < 0 || nx >= n || ny < 0 || ny >= n )
                break;
            if ( b[nx][ny] != b[x][y] )
                break;
        }
        if ( i == k )
            return true;
    }
    return false;
}

int main()
{
    freopen ( "a.in", "rt", stdin );
    freopen ( "a.out", "wt", stdout );

    int test_cnt;
    cin >> test_cnt;
    for ( int test_id = 0; test_id < test_cnt; ++test_id )
    {
        scanf ( "%d%d\n", &n, &k );
        for ( int i = 0; i < n; ++i )
        {
            char c;
            for ( int j = 0; j < n; ++j )
            {
                scanf ( "%c", &c );
                if ( c == '.' ) a[i][j] = 0;
                if ( c == 'R' ) a[i][j] = 1;
                if ( c == 'B' ) a[i][j] = 2;
            }
            scanf ( "\n" );
        }

        for ( int i = 0; i < n; ++i )
            for ( int j = 0; j < n; ++j )
                b[j][n - i - 1] = a[i][j];

        for ( int j = 0; j < n; ++j )
        {
            int c = n - 1;
            for ( int i = n - 1; i >= 0; --i )
                if ( b[i][j] != 0 )
                    b[c--][j] = b[i][j];
            while ( c >= 0 )
                b[c--][j] = 0;
        }

        bool status[3] = { false, false, false };
        for ( int i = 0; i < n; ++i )
            for ( int j = 0; j < n; ++j )
                if ( same ( i, j ) )
                    status[b[i][j]] = true;
        string s;
        if ( status[1] && status[2] )
            s = "Both";
        if ( status[1] && !status[2] )
            s = "Red";
        if ( !status[1] && status[2] )
            s = "Blue";
        if ( !status[1] && !status[2] )
            s = "Neither";

        printf ( "Case #%d: %s\n", test_id + 1, s.data() );
    }

    return 0;
}
