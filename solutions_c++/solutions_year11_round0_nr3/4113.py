//Author: Doan Minh Quy
//@BEGIN SOURCE CODE
#include <cstdio>
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int tc, n , array , mn , sum , pos;
    scanf("%d",&tc);
    for ( int cs = 1 ; cs <= tc ;++cs )
    {
        scanf("%d",&n);
        pos = sum = 0 ; mn = 1000000000;
        for ( int i = 0 ; i < n ; ++i)
        {
            scanf("%d",&array);
            sum += array;
            pos ^= array;
            if ( array < mn )
                mn = array;
        }
        if ( pos != 0 )
            printf("Case #%d: NO\n",cs);
        else
            printf("Case #%d: %d\n",cs,sum-mn);
    }
}
//@END SOURCE CODE
