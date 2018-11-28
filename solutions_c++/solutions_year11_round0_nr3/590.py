#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    int tc;
    scanf("%d", &tc);
    for (int ncase = 1; ncase <= tc; ++ncase)
    {
        int min = 0;
        int sum = 0;
        int xor_sum = 0;
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
        {
            int v;
            scanf("%d", &v);
            sum += v;
            xor_sum ^= v;
            if (i == 0 || min > v)
            {
                min = v;
            }
        }
        if (xor_sum != 0)
        {
            printf("Case #%d: NO\n", ncase);
        }
        else
        {
            printf("Case #%d: %d\n", ncase, sum - min);
        }
    }
    return 0;
}
