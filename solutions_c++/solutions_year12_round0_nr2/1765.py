#include "stdio.h"
int main()
{
    int cas = 0;
    //freopen("B-small.in", "r", stdin);
    //freopen("B-small.out", "w", stdout);
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);
    scanf("%d", &cas);
    int t = 0;
    while( t < cas )
    {
        int n, s, p, i, a;
        int ct = 0;
        scanf("%d %d %d", &n, &s, &p);
        for( i=0; i<n; i++)
        {
            scanf("%d", &a);
            int tw = a - p;
            int c = tw/2;
            int d = tw - c;
            if( tw < 0) continue;
            if( c + 2 > p)
            {
                ct++; continue;
            }
            else if( (c + 2) == p)
            {
                if( s > 0)
                {
                    ct++;
                    s--;
                }
            }
            if( s != 0)
            {
                int h =0 ;
            }
        }
        printf("Case #%d: %d\n",++t,ct);
    }
    return 0;
}