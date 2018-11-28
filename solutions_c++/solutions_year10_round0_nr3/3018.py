#include <stdio.h>
#include <stdlib.h>

const int MAX_N = 10;

int
main()
{
    int t = 0;
    int n = 0;
    int r = 0;
    int k = 0;
    scanf("%d", &t);
    int g[MAX_N];
    int value = 0;

    for (int i = 0; i < t; i++)
    {
        scanf("%d %d %d", &r, &k, &n);
        for (int p = 0; p < n; p++)
        {
            scanf("%d", &value);
            g[p] = value;
        }

        int amount = 0;
        int cursor = 0;
        for (int m = 0; m < r; m++)
        {
            
            int sum = 0;
            int count = 0;
            while (count  < n && sum + g[cursor] <= k)
            {
                sum += g[cursor];
                cursor++;
                count++;
                if (cursor == n)
                {
                    cursor = 0;
                }
            }
            amount += sum;
        }

        printf("Case #%d: %d\n", i + 1, amount);

    }
    return 0;


}
