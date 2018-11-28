#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;
#define MAX 1111111111
#define MAX_R 111
#define MAX_P 111
int n, m;
int a[MAX_R];
bool f[MAX_P];
int t;
int Get( )
{
    int sum = 0;
    int s, e;
    memset( f, 0, sizeof( f ) );
    for( int i = 0; i < m; ++i ){
        f[a[i]] = 1;
        s = a[i] - 1;
        e = a[i] + 1;
        while( s > 0 )
        {
            if( f[s] ) break;
            ++sum;
            --s;
        }
        while( e <= n )
        {
            if( f[e] ) break;
            ++sum;
            ++e;
        }
    }
    return sum;
}

int main( )
{
    freopen( "C-small-attempt1.in", "r", stdin );
    freopen( "C-small-attempt1.out", "w", stdout );
    scanf( "%d", &t );
    for( int i = 1; i <= t; ++i )
    {
        scanf( "%d %d", &n, &m );
        for(int j = 0; j < m; j++ )
            scanf( "%d", &a[j] );
        int max = MAX;
        do
        {
            int temp = Get( );
            if( temp < max ) max = temp;
        } while( next_permutation( a, a + m ) );
        printf( "Case #%d: %d\n", i, max );
    }
    return 0;
}
