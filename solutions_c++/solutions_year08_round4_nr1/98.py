#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <deque>
#include <string>
#include <numeric>
#include <functional>
#include <cstdlib>
#include <cmath>
#include <memory.h>

using namespace std;

int nodes[10001];
int m;
int leaf_start;

bool seen[10001][2];
int  mem [10001][2];

void set(int& rv, int r)
{
    if( rv == -1 || r < rv )
        rv = r;
}

int solve(int i, int v)
{
    if( i >= leaf_start )
        return -(nodes[i] != v);
    if( seen[i][v] )
        return mem[i][v];
    seen[i][v] = true;

    int a = (nodes[i] >> 1) & 1;
    int& rv = mem[i][v];
    rv = -1;
    
    for( int x = 0; x <= (nodes[i] & 1); ++x, a ^= 1 )
    {
        if( a ) // and node
        {
            if( v ) // need both ones
            {
                int r1 = solve(2*i+1, 1);
                if( r1 == -1 )
                    continue;
                int r2 = solve(2*i+2, 1);
                if( r2 == -1 )
                    continue;

                int r = r1 + r2;
                set(rv, r+x);
            }
            else    // need one zero
            {
                int r1 = solve(2*i+1, 0);
                int r2 = solve(2*i+2, 0);
                if( r1 == -1 && r2 == -1 )
                    continue;
                else if( r1 == -1 )
                    set(rv, r2+x);
                else if( r2 == -1 )
                    set(rv, r1+x);
                else
                    set(rv, min(r1, r2)+x);
            }
        }
        else    // or node
        {
            if( v ) // need any
            {
                int r1 = solve(2*i+1, 1);
                int r2 = solve(2*i+2, 1);
                if( r1 == -1 && r2 == -1 )
                    continue;
                else if( r1 == -1 )
                    set(rv, r2+x);
                else if( r2 == -1 )
                    set(rv, r1+x);
                else
                    set(rv, min(r1, r2)+x);
            }
            else    // need bot zero
            {
                int r1 = solve(2*i+1, 0);
                if( r1 == -1 )
                    continue;
                int r2 = solve(2*i+2, 0);
                if( r2 == -1 )
                    continue;

                int r = r1 + r2;
                set(rv, r+x);
            }
        }
    }
    return rv;
}

int main()
{
    int T = 0;
    cin >> T;
    for( int c = 1; c <= T; ++c )
    {
        int v;
        cin >> m >> v;
        for( int i = 0; i != (m-1)/2; ++i )
        {
            int t, c;
            cin >> t >> c;
            nodes[i] = (t<<1) | c;
        }
        leaf_start = (m - 1) / 2;
        for( int i = (m-1)/2; i != m; ++i )
            cin >> nodes[i];

        memset(seen, 0, sizeof(seen));
        int r = solve(0, v);
        if( r != -1 )
            cout << "Case #" << c << ": " << r << endl;
        else
            cout << "Case #" << c << ": " << "IMPOSSIBLE" << endl;
    }

    return 0;
}