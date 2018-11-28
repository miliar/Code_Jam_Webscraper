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
#include <algorithm>

using namespace std;

#define sqr(a) ((a)*(a))
#define det2(a,b,c,d) ((a)*(d) - (b)*(c))

long long a[800], b[800];

int main()
{
    int i, j, n, cas, T;

    scanf( "%d", &T );
    for ( cas = 1 ; cas <= T ; cas++ )
    {
        scanf( "%d", &n );
        for ( i = 0 ; i < n ; i++ )
            scanf( "%I64d", &a[i] );
        for ( i = 0 ; i < n ; i++ )
            scanf( "%I64d", &b[i] );
        sort(a, a+n);
        sort(b, b+n);
        long long res = 0;
        for ( i = 0 ; i < n ; i++ )
            res += a[i] * b[n-1-i];
    
        printf( "Case #%d: %I64d\n", cas, res );
    }

    return 0;
}
