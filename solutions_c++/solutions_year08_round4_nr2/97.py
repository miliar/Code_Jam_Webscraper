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

int main()
{
    int C;
    cin >> C;
    for( int c = 1; c <= C; ++c )
    {
        int n, m, a;
        cin >> n >> m >> a;

        bool ok = false;
        for( int ax = 0; ax <= n; ++ax )
        {
            for( int bx = 0; bx <= n; ++bx )
            for( int by = 0; by <= m; ++by )
            for( int cx = 0; cx <= n; ++cx )
            for( int cy = 0; cy <= m; ++cy )
            {
                if( abs(bx*cy - by*cx - ax*(cy - by)) == a )
                {
                    cout << "Case #" << c << ": " << ax << " 0 " << bx << ' ' << by << ' ' << cx << ' ' << cy << endl;
                    ok = true;
                    goto done;
                }
            }
        }

        for( int ay = 0; ay <= m; ++ay )
        {
            for( int bx = 0; bx <= n; ++bx )
            for( int by = 0; by <= m; ++by )
            for( int cx = 0; cx <= n; ++cx )
            for( int cy = 0; cy <= m; ++cy )
            {
                if( abs(bx*cy - by*cx - ay*(bx - cx)) == a )
                {
                    cout << "Case #" << c << ": 0 " << ay << ' ' << bx << ' ' << by << ' ' << cx << ' ' << cy << endl;
                    ok = true;
                    goto done;
                }
            }
        }
done:
        if( !ok )
            cout << "Case #" << c << ": IMPOSSIBLE" << endl;
        //int sb, sh;
        //for( int b = 1; b*b <= a; ++b )
        //{
        //    if( a % b )
        //        continue;

        //    int h = a / b;
        //    if( b <= n && h <= m )
        //    {
        //        sb = b;
        //        sh = h;
        //        ok = true;
        //        break;
        //    }
        //    else if( b <= m && h <= n )
        //    {
        //        sb = h;
        //        sh = b;
        //        ok = true;
        //        break;
        //    }
        //}

        //cout << "Case #" << c << ": "; 
        //if( ok )
        //    cout << "0 0 " << sb << " 0 0 " << sh;
        //else
        //    cout << "IMPOSSIBLE";
        //cout << endl;
    }

    return 0;
}