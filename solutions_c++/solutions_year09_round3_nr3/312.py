#include<iostream>
#include<algorithm>
using namespace std;

int n, p;
int a[10];
bool f[105];

int get( ){
    int i, j, sum = 0, s, e;
    memset( f, false, sizeof( f ) );
    for( i = 0; i < p; i++ ){
        f[a[i]] = true;
        s = a[i] - 1;
        e = a[i] + 1;
        while( s > 0 ){
            if( f[s] ) break;
            sum++;
            s--;
        }
        while( e <= n ){
            if( f[e] ) break;
            sum++;
            e++;
        }
    }
    return sum;
}

int main( ){
    int i, t, cas, ans, tmp;
    freopen( "C-small-attempt0.in", "r", stdin );
    freopen( "C-small-attempt0.out", "w", stdout );
    scanf( "%d", &t );
    for( cas = 1; cas <= t; cas++ ){
        scanf( "%d %d", &n, &p );
        for( i = 0; i < p; i++ )
            scanf( "%d", &a[i] );
        ans = 1000000000;
        do{
            tmp = get( );
            if( tmp < ans ) ans = tmp;
        }while( next_permutation( a, a + p ) );
        printf( "Case #%d: %d\n", cas, ans );
    }
    return 0;
}
