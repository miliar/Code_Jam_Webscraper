#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int n;
int a[1024], b[1024];

int main()
{
    int i, j, k, T;
    scanf( "%d", &T );
    for ( int tt = 1; tt <= T; tt++ )
    {
        scanf( "%d", &n );
        for ( i = 1; i <= n; i++ )
        {
            scanf( "%d %d", &a[i], &b[i] );
        }
        k = 0;
        for ( i = 1; i <= n; i++ )
        {
            for ( j = i + 1; j <= n; j++ )
            {
                if ( ( a[i] > a[j] ) && ( b[i] < b[j] ) )
                    k++;
                else if ( ( a[i] < a[j] ) && ( b[i] > b[j] ) )
                    k++;
            }
        }
        printf( "Case #%d: %d\n", tt, k );
    }
    return 0;
}
