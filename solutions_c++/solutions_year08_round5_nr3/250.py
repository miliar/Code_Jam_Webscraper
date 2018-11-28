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

vector<string> cr;
int mem[11][11][1<<10][1<<10];
bool seen[11][11][1<<10][1<<10];
int solve(int i, int j, int u, int a)
{
    if( j == cr[0].size() )
        return solve(i + 1, 0, a, 0);
    if( i == cr.size() )
        return 0;

    if( seen[i][j][u][a] )
        return mem[i][j][u][a];

    seen[i][j][u][a] = true;
    int& rv = mem[i][j][u][a];
    rv = solve(i, j+1, u, a);
    if( cr[i][j] != 'x' )
    {
        bool ok = true;
        if( j && (a & (1<<(j-1))) )
            ok = false;
        if( i )
        {
            if( j && (u & (1<<(j-1))) )
                ok = false;
            if( j + 1 < cr[i].size() && (u & (1<<(j+1))) )
                ok = false;
        }
        if( ok )
            rv = max(rv, 1+solve(i, j+1, u, a | (1<<j)));
    }

    return rv;
}

int main()
{
    int C;
    cin >> C;
    for( int cs = 1; cs <= C; ++cs )
    {
        int m, n;
        cin >> m >> n;
        
        vector<string> cr(m);
        for( int i = 0; i != m; ++i )
            cin >> cr[i];

        ::cr = cr;
        memset(seen, 0, sizeof(seen));
        int rv = solve(0, 0, 0, 0);
        cout << "Case #" << cs << ": " << rv << endl;
    }

    return 0;
}