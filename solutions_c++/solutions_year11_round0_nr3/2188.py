#include <cstdio>

int main()
{
    int t;
    scanf("%d", &t);
    for (int ca = 1; ca <= t; ++ca)
    {
        int n;
        scanf("%d", &n);
        int ans, min, sum;
        scanf("%d", &ans);
        min = sum = ans;
        for (int i = 2; i <= n; ++i)
        {
            int t;
            scanf("%d", &t);
            ans ^= t;
            sum += t;
            if ( t < min )
                min = t;
        }
        if ( ans != 0 )
            printf("Case #%d: NO\n", ca);
        else
            printf("Case #%d: %d\n", ca, sum-min);
    }
    return 0;
}
