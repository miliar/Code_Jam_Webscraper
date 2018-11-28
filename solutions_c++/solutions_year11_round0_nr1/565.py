#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN 
#define eps (1e-8)
#define INF 1000000000
#define abs(x) ( (x) > 0? (x): -(x) )
#define sqr(x) ((x) * (x))
#define MAX(a, b) ((a) > (b)? (a): (b))
#define MIN(a, b) ((a) < (b)? (a): (b))

typedef long long LL;

int n;
int pos1, pos2, time1, time2, now;

void swap( int &x, int &y ) { int temp = x; x = y; y = temp; }

int main()
{
    int T, ca = 0;
    scanf( "%d", &T );
    while ( T-- )
    {
        pos1 = pos2 = 1;
        time1 = time2 = now = 0;
        scanf( "%d", &n );
        for ( int i = 1; i <= n; ++i )
        {
            char type[5];
            int but;
            scanf( "%s%d", type, &but );
            if ( type[0] == 'O' )
            {
                int dt = MAX( abs( pos1 - but ), now - time1 );
                now = time1 = time1 + dt + 1;
                pos1 = but;
            }
            else
            {
                int dt = MAX( abs( pos2 - but ), now - time2 );
                now = time2 = time2 + dt + 1;
                pos2 = but;
            }
        }
        printf( "Case #%d: %d\n", ++ca, MAX( time1, time2 ) );
    }
    return 0;
}
