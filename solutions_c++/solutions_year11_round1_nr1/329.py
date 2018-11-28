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

void swap( int &x, int &y ) { int temp = x; x = y; y = temp; }

int gcd( int a, int b )
{
    return (b)? gcd( b, a % b ): a;
}

int main()
{
    int T, ca = 0;
    scanf( "%d", &T );
    while ( T-- )
    {
        printf( "Case #%d: ", ++ca );
        LL n;
        int a, b;
        scanf( "%lld%d%d", &n, &a, &b );
        int g = gcd( a, 100 );
        if ( n >= 100 / g )
        {
            if ( b == 100 && a < 100 || b == 0 && a > 0 )
                puts( "Broken" );
            else
                puts( "Possible" );
        }
        else 
            puts( "Broken" );
    }
    return 0;
}
