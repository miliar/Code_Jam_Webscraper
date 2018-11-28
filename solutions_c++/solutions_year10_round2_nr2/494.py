#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

int main()
{
    int c;
    int n, k, b, t;
    long long xi[50];
    long long vi[50];

    scanf("%d", &c);
    
    for(int j = 1; j <= c; j++)
    {
        scanf("%d %d %d %d", &n, &k, &b, &t);
        for(int i = 0; i < n; i++)
        {
            scanf("%lld", &xi[i]);
        }
        for(int i = 0; i < n; i++)
        {
            scanf("%lld", &vi[i]);
        }
        for(int i = 0; i < n; i++)
        {
            xi[i] += vi[i]*t;
        }
        int successCount = 0;
        int swapCount = 0;
        for(int i = n-1; i >= 0; i--)
        {
            if(xi[i] >= b)
            {
                successCount++;
                for(int k = i+1; k < n; k++)
                {
                    if(xi[k] < b)
                    {
                        int t = xi[k];
                        xi[k] = xi[i];
                        xi[i] = t;
                        swapCount++;
                    }
                }
                if(successCount >= k) break;
            }
        }
        if(successCount < k)
        {
            printf("Case #%d: IMPOSSIBLE\n", j);
        }
        else
        {
            printf("Case #%d: %d\n", j, swapCount);
        }
    }
}
