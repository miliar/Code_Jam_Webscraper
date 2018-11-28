#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN 1100
#define MAXM 30000
#define eps (1e-8)
#define INF 1000000000
#define abs(x) ( (x) > 0? (x): -(x) )
#define sqr(x) ((x) * (x))
#define MAX(a, b) ((a) > (b)? (a): (b))
#define MIN(a, b) ((a) < (b)? (a): (b))

typedef long long LL;

int n;
int candy[MAXN];

void swap( int &x, int &y ) { int temp = x; x = y; y = temp; }

int main()
{
    int T, ca = 0;
    scanf( "%d", &T );
    while ( T-- )
    {
        scanf( "%d", &n );
        for ( int i = 1; i <= n; ++i ) scanf( "%d", candy + i );
        int sum = 0, tot = 0;
        for ( int i = 1; i <= n; ++i ) 
        {
            sum ^= candy[i];
            tot += candy[i];
        }
        printf( "Case #%d: ", ++ca );
        if ( sum ) puts( "NO" ); else
        {
            int minc = candy[1];
            for ( int i = 2; i <= n; ++i ) minc = MIN( minc, candy[i] );
            printf( "%d\n", tot - minc );
        }
    }
    return 0;
}
