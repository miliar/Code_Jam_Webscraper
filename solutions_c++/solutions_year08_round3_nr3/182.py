#include <stdio.h>

#define MOD 1000000007
#define MAX_N 1024

long long W[MAX_N], A[MAX_N], C[MAX_N];

int main(void)
{
    int T, tests;

    freopen("c0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &tests);
    for (T = 1; T <= tests; T++)
    {
        long long n, m, x, y, z, sum = 0LL;
        int i, j;
        
        scanf("%lld%lld%lld%lld%lld", &n, &m, &x, &y, &z);
        for (i = 0; i < m; i++)
            scanf("%lld", A + i);
        for (i = 0; i < n; i++)
        {
            W[i] = A[i % m];
            A[i % m] = (x * A[i % m] + y * (i + 1)) % z;
        }
        
        for (i = 0; i < n; i++)
        {
            long long sols = 1LL;
            
            for (j = 0; j < i; j++)
                if (W[j] < W[i])
                   sols = (sols + C[j]) % MOD;
            C[i] = sols;
            sum = (sum + sols) % MOD;
        }
        
        printf("Case #%d: %lld\n", T, sum);
    }
    
    return 0;
}
