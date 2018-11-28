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

int n;
int x[1001];
int y[1001];
int z[1001];
int p[1001];
int b[3][2];    // bounds
double  bc[3];  // battle cruiser

double calc()
{
    double rv = 0;
    for( int i = 0; i != n; ++i )
    {
        double d = abs(bc[0] - x[i]) + abs(bc[1] - y[i]) + abs(bc[2] - z[i]);
        rv = max(rv, double(d) / p[i]);
    }
    return rv;
}

double solve(int coord)
{
    if( coord == 3 )
        return calc();

    double l = b[coord][0], r = b[coord][1];
    double const EPS = 1e-7;

    while( r - l > EPS )
    {
        double a = (2*l + r) / 3.0;
        double b = (l + 2*r) / 3.0;
        
        bc[coord] = a;
        double fa = solve(coord + 1);

        bc[coord] = b;
        double fb = solve(coord + 1);

        if( fa < fb )
            r = b;
        else
            l = a;
    }

    bc[coord] = l;
    return solve(coord + 1);
}

int main()
{
    int T;
    cin >> T;
    int &mnx = b[0][0], &mxx = b[0][1],
        &mny = b[1][0], &mxy = b[1][1],
        &mnz = b[2][0], &mxz = b[2][1];

    for( int c = 1; c <= T; ++c )
    {
        cin >> n;
        for( int i = 0; i != n; ++i )
        {
            cin >> x[i] >> y[i] >> z[i] >> p[i];
            if( i )
                mnx = min(mnx, x[i]), mxx = max(mxx, x[i]),
                mny = min(mny, y[i]), mxy = max(mxy, y[i]),
                mnz = min(mnz, z[i]), mxz = max(mxz, z[i]);
            else
            {
                mnx = mxx = x[i];
                mny = mxy = y[i];
                mnz = mxz = z[i];
            }
        }

        printf("Case #%d: %.6f\n", c, solve(0));
    }
    return 0;
}