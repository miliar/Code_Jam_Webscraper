#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <iostream>
#include <functional>
#include <algorithm>

using namespace std;

bool m[12010][12010];
int x, y, d;
int off[4][2] = { { 0, -1 }, { 1, 0 }, { 0, 1 }, { -1, 0 } };
int lc, rc;
int ix, iy, ax, ay;

void move( char c )
{
    if (c == 'F')
    {
        x += off[d][0];
        y += off[d][1];
        m[y][x] = true;
        //printf( "%d %d\n", y, x );
        ix = min( x, ix );
        ax = max( x, ax );
        iy = min( y, iy );
        ay = max( y, ay );
        x += off[d][0];
        y += off[d][1];
    }
    else if (c == 'L')
    {
        d = (d+3) % 4;
        lc++;
    }
    else
    {
        d = (d+1) % 4;
        rc++;
    }
}

int main( void )
{
    int TC;
    cin >> TC;

    for (int tc = 1; tc <= TC; tc++)
    {
        int L;
        cin >> L;
        string s;
        int t;
        ix = ax = x = 6005;
        iy = ay = y = 6005;
        d = 0;
        rc = 0;
        lc = 0;
        memset( m, false, sizeof( m ) );
        m[y][x] = true;
        for (int i = 0; i < L; i++)
        {
            cin >> s >> t;
            for (int j = 0; j < t; j++)
            {
                for (int k = 0; k < s.size(); k++)
                {
                    move( s[k] );
                }
            }
        }

        int cnt = 0;
        for (int i = iy - (iy%2); i <= ay; i += 2)
        {
            bool in = false;
            bool found = false;
            int c = 0;
            for (int j = ix; j <= ax; j++)
            {
                if (j % 2)
                {
                    if (m[i][j])
                    {
                        if (!in && found)
                        {
                            cnt += c;
                            for (int k = 0; k < c; k++)
                            {
                                m[i][j-k*2-1] = true;
                            }
                            c = 0;
                        }
                        in = !in;
                        found = true;
                    }
                }
                else
                {
                    if (found && !in)
                    {
                        c++;
                    }
                }
            }
        }

        for (int j = ix - (ix%2); j <= ax; j += 2)
        {
            bool in = false;
            bool found = false;
            int c = 0;
            for (int i = iy; i <= ay; i++)
            {
                if (i % 2)
                {
                    if (m[i][j])
                    {
                        if (!in && found)
                        {
                            cnt += c;
                            c = 0;
                        }
                        in = !in;
                        found = true;
                    }
                }
                else
                {
                    if (found && !in && !m[i][j])
                    {
                        c++;
                    }
                }
            }
        }

        cout << "Case #" << tc << ": " << cnt << endl;
    }

    return 0;
}
