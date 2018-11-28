#include <cstdio>
#include <cstring>

int a, b ;

int fun( int n )
{
    int tmp1, tmp2, ans ;
    if( n < 10 )    return 0 ;
    if( n < 100 )
    {
        tmp1 = n % 10 ; tmp2 = n / 10 ; ans = tmp1 * 10 + tmp2 ;
        if( ans > n && ans <= b )
        {
            return 1 ;
        }
        return 0 ;
    }
    int sum = 0 ;
    tmp1 = n % 10 ; tmp2 = n / 10 ; ans = tmp1 * 100 + tmp2 ;
    if( ans > n && ans <= b )
    {
        sum++ ;
    }
    tmp1 = n % 100 ;    tmp2 = n / 100; ans = tmp1 * 10 + tmp2 ;
    if( ans > n && ans <= b )
    {
        sum++ ;
    }
    return sum;
}

int main()
{
    freopen( "C-small-attempt0.in", "r", stdin ) ;
    freopen( "C-small-attempt0.out", "w", stdout ) ;
    int t, i, cnt = 0 ;
    scanf( "%d", &t ) ;
    while( t-- )
    {
        int sum = 0 ;
        scanf( "%d%d", &a, &b ) ;
        for( i = a; i <= b; i++ )
        {
            sum += fun( i ) ;
        }
        printf( "Case #%d: %d\n", ++cnt, sum ) ;
    }
    return 0 ;
}
