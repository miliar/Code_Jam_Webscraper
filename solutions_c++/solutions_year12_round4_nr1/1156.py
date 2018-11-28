#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <queue>
using namespace std;
int len[10005], d[10005], l[10005], n, D;
bool spfa() {
    if ( d[0] * 2 >= D ) return 1;
    memset( len, 0, n << 2 );
    len[0] = d[0];
    queue<int> q;
    int nxt, tmp, i, j, k;
    q.push( 0 );
    while ( !q.empty() ) {
        nxt = q.front();
        q.pop();
        for ( i = nxt + 1; i < n; ++i ) {
            if ( d[i] - d[nxt] > len[nxt] ) break;
            k = min( d[i] - d[nxt], l[i] );
            if ( k > len[i] ) {
                len[i] = k;
                if ( k + d[i] >= D ) return 1;
                q.push( i );
            }
        }
    }
    return 0;
}
int main( int argc, char *argv[] )
{
    freopen( "A-large.in", "r", stdin );
    freopen( "A-large.out", "w", stdout );
    int t, i, j, cas = 0;
    scanf( "%d", &t );
    while ( t-- ) {
        scanf( "%d", &n );
        for ( i = 0; i < n; ++i ) {
            scanf( "%d%d", d + i, l + i );
        }
        scanf( "%d", &D );
        printf( "Case #%d: ", ++cas );
        if ( spfa() ) puts( "YES" );
        else puts( "NO" );
    }
    return 0;
}
