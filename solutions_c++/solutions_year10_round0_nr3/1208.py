#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int g[1001];
int main()
{
    int i ,j , n ,m , t , R , k , N , cas = 1 , ans , sum;
    freopen("/home/madfrog/下载/C-small-attempt0.in","r",stdin);
    freopen("/home/madfrog/下载/C-small-attempt0.out","w" , stdout);
    scanf("%d" , &t);
    while ( t-- )   {
        scanf("%d%d%d" , &R , &k , &N);
        sum = 0;
        for ( i = 0;i < N;i ++ )    {
            scanf("%d" , &g[i]);
            sum += g[i];
        }
        if ( k >= sum ) {
            printf("Case #%d: %d\n" , cas ++ , sum * R);
            continue;
        }

        j = 0;
        ans = 0;
        for ( i = 1;i <= R;i ++ )   {
            int tmp = k;
            while ( tmp >= g[j] ) {
                tmp -= g[j];
                ans += g[j];
                j = (j + 1) % N;
            }
        }

        printf("Case #%d: %d\n" , cas ++ , ans);
    }
    return 0;


}
