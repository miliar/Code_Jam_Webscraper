#include <iostream>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <functional>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define FOR( i, s, n ) for (int i = s; i < n; ++i)
#define CLEAR( x, v ) memset( x, v, sizeof( x ) )

int m[15][15];
int R, C;

int cache[2000000];

int encode( int r, int c )
{
    int v = r + (c<<2);
    FOR( i, 0, R ) FOR( j, 0, C ) if (m[i][j] == 1)
    {
        v |= 1<<((i<<2)+j+4);
    }
#if 0
    cout << "encode" << endl;
    FOR( i, 0, R )
    {
        FOR( j, 0, C )
        {
            if (i == r && j == c) cout << "K";
            else if (m[i][j]) cout << "#";
            else cout << ".";
        }
        cout << endl;
    }
    cout << endl;
#endif
    return v;
}

void decode( int v, int& r, int& c )
{
    CLEAR( m, 0 );
    FOR( i, 0, R ) FOR( j, 0, C ) if (v & 1<<((i<<2)+j+4))
    {
        m[i][j] = 1;
    }
    r = v & 3;
    c = (v>>2) & 3;
    m[r][c] = 2;

#if 0
    FOR( i, 0, R )
    {
        FOR( j, 0, C )
        {
            if (i == r && j == c) cout << "K";
            else if (m[i][j]) cout << "#";
            else cout << ".";
        }
        cout << endl;
    }
    cout << endl;
#endif
}

int solve( int v )
{
    int& res = cache[v];
    if (res != -1) return res;

    int r, c;
    decode( v, r, c );
    for( int i = -1; i <= 1; i++ )
        for( int j = -1; j <= 1; j++ ) if (i || j)
        {
            int nr = r + i;
            int nc = c + j;
            if (nr >= 0 && nr < R && nc >= 0 && nc < C)
            {
                if (m[nr][nc] == 0)
                {
                    m[r][c] = 1;
                    int t = encode( nr, nc );
                    int xx = solve( t );
                    decode( v, r, c );
                    if (xx == 0)
                    {
                        res = 1;
                        return res;
                    }
                }
            }
        }

    decode( v, r, c );
    res = 0;
    return res;
}

int main( void )
{
    int TC;
    cin >> TC;

    FOR( tc, 0, TC )
    {
        int r, c;
        CLEAR( cache, -1 );
        CLEAR( m, 0 );
        cin >> R >> C;
        FOR( i, 0, R )
        {
            string s;
            cin >> s;
            FOR( j, 0, C )
            {
                if (s[j] == '#') m[i][j] = 1;
                else if (s[j] == 'K') { r = i; c = j; m[i][j] = 2; }
            }
        }

        int v = encode( r, c );
        int res = solve( v );

        cout << "Case #" << (tc+1) << ": " << (res ? 'A' : 'B') << endl;
    }

    return 0;
}
