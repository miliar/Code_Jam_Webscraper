#include<stdio.h>

int main()
{
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);
    
    int T, tt, n, m, x, i;
    scanf("%d", &T);
    for(tt = 1; tt <= T; tt++)
    {
        m = 0;
        scanf("%d", &n);
        for(i = 1; i <= n; i++)
        {
            scanf("%d", &x);
            if(i != x) m++;
        }
        printf("Case #%d: %.6lf\n", tt, (double)m);
    }
    
    return 0;
}
