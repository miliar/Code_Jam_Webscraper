#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <iostream>
#include <functional>
#include <algorithm>

using namespace std;

int m[110][110];
int H, W;

int solve( int r, int c )
{
    if (m[r][c] == -2) return 0;
    if (m[r][c] != -1) return m[r][c];

    int x = 0;
    if (r+2 <= H && c+1 <= W) x += solve( r+2, c+1 );
    if (r+1 <= H && c+2 <= W) x += solve( r+1, c+2 );
    m[r][c] = (x % 10007);
    return x;
}

int main( void )
{
    int TC;
    cin >> TC;

    for (int tc = 1; tc <= TC; tc++)
    {
        int R;
        cin >> H >> W >> R;
        memset( m, -1, sizeof( m ) );
        for (int i = 0; i < R; i++)
        {
            int r, c;
            cin >> r >> c;
            m[r][c] = -2;
        }
        m[H][W] = 1;

        int cnt = (solve( 1, 1 ) % 10007);

        cout << "Case #" << tc << ": " << cnt << endl;
    }

    return 0;
}
