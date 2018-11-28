#pragma comment(linker, "/STACK:134217728")

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define sqr(a) ((a)*(a))
#define det2(a,b,c,d) ((a)*(d) - (b)*(c))

void ext(int a, int b, int &x, int &y, int &d)
{
    if ( b == 0 )
    {
        d=a;
        x=1;
        y=0;
        return;
    }

    int dd, xx, yy;
    ext(b, a%b, xx, yy, dd);
    d=dd;
    x = yy;
    y = xx - int(a/b) * yy;    
}

int main()
{
    int i, j, n, m, a, b, x, y, d, A, x1, x2, y1, y2, x3, y3;
    int TST, cas;
    
    scanf( "%d", &TST );
    for ( cas = 1 ; cas <= TST ; cas++ )
    {
        scanf( "%d%d%d", &n, &m, &A );
        bool ok = 0;
        printf( "Case #%d: ", cas );

        if ( n*m < A )
        {
            if ( !ok )
                printf( "IMPOSSIBLE\n" );
            continue;
        }

        for ( x1 = 0 ; x1 <= n ; x1++ ) if ( !ok )
            for ( y1 = 0 ; y1 <= m ; y1++ ) if ( !ok )
        for ( x2 = 0 ; x2 <= n ; x2++ ) if ( !ok )
            for ( y2 = 0 ; y2 <= m ; y2++ ) if ( !ok )
        for ( x3 = 0 ; x3 <= n ; x3++ ) if ( !ok )
        {
            int aa = A - x1*y2 - x3*y1 + y1*x2 + y2*x3;
            if ( x2 - x1 == 0 )
            {
                if ( aa==0 )
                {
                    y3 = 0;
                    ok = 1;
                    printf( "%d %d %d %d %d %d\n", x1, y1, x2, y2, x3, y3 );
                }
            }
            else if ( aa % (x2-x1) == 0 )
            {
                y3 = aa / (x2-x1);
                if ( 0 <= y3 && y3 <= m )
                {
                    ok = 1;
                    printf( "%d %d %d %d %d %d\n", x1, y1, x2, y2, x3, y3 );
                }
            }
                
        }

        if ( !ok )
            printf( "IMPOSSIBLE\n" );
//        else
//        {
//            int dx=-min(0,x2), dy=-min(0,y2);
//            printf( "%d %d %d %d %d %d\n", dx, dy, x1+dx, y1+dy, x2+dx, y2+dy );
//        }
    }


    return 0;
}
