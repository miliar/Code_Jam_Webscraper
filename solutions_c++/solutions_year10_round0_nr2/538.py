#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int gcd( int a , int b )    {
    return b == 0 ? a : gcd( b , a % b);
}
int a[1001];

int main()
{
    int n , m , i , j , k , t , factor;
    freopen("/home/madfrog/下载/B-small-attempt0.in","r",stdin);
    freopen("/home/madfrog/下载/B-small-attempt0.out","w",stdout);
    scanf("%d" , &t);
    for ( k = 1;k <= t;k ++ )   {

        scanf("%d%d" , &n , &a[0]);
        factor = 0;
        for ( i = 1;i < n;i ++ )    {
            scanf("%d" , &a[i]);//printf("%d\n" , factor);
            factor = gcd( abs(a[i] - a[0]) , factor);
            //printf("%d\n" , factor);
        }
        if ( factor < 0 ) factor = -factor;

        printf("Case #%d: %d\n" ,k , (a[0] / factor + (a[0] % factor != 0)) * factor  - a[0] );
    }
    return 0;

}
