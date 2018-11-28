#include <stdio.h>

int main()
{
    int ca, tc;
    scanf("%d", &ca);
    for (int tc = 1; tc <= ca; tc++)
    {
        int n;
        scanf("%d", &n);

        int sum = 0;
        int magic = 0;
        int min = 10000000;
        for (int i = 0; i < n; i++)
        {
            int a;
            scanf("%d", &a);
            sum += a;
            magic ^= a;
            if (a < min) min = a;
        }

        if (magic == 0)
        {
            printf("Case #%d: %d\n", tc, sum - min);
        }
        else
        {
            printf("Case #%d: NO\n", tc);
        }
    }
    return 0;
}
