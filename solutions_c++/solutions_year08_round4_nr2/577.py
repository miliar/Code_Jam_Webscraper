#include <stdio.h>

int main(void)
{
    int test, tests;
    
    freopen("b1.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &tests);
    for (test = 1; test <= tests; test++)
    {
        long long n, m, a, i, s, y1, x2, x3;

        scanf("%lld%lld%lld", &n, &m, &a);
        for (y1 = 0; y1 <= m; y1++)
            for (x2 = 0; x2 <= n; x2++)
                for (x3 = 0; x3 <= n; x3++)
                {
                    s = a - (x3 - x2) * y1;
                    if (x2 && (s % x2) == 0 && (s / x2) <= m)
                       goto sol;
                }
                
        printf("Case #%d: IMPOSSIBLE\n", test);
        continue;
        
        sol: printf("Case #%d: 0 %lld %lld 0 %lld %lld\n", test, y1, x2, x3, s / x2);
    }
    
    return 0;
}
