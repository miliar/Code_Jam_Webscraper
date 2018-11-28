#include <stdio.h>

char combine[100][10];
char oppose[100][10];
char basic[1000];
int c, d, n;

int main()
{
    int tc, ca;
    scanf("%d", &ca);
    for (tc = 1; tc <= ca; tc++)
    {
        scanf("%d", &c);
        for (int i = 0; i < c; i++)
        {
            scanf("%s", combine[i]);
        }

        scanf("%d", &d);
        for (int i = 0; i < d; i++)
        {
            scanf("%s", oppose[i]);
        }

        scanf("%d", &n);
        scanf("%s", basic);

        char result[1000];
        int p = 0;
        for (int i = 0; i < n; i++)
        {
            // invoke
            result[p++] = basic[i];

            // combine
            bool go = true;
            while (go && p >= 2)
            {
                go = false;
                for (int j = 0; j < c; j++)
                {
                    if (combine[j][0] == result[p - 1] && combine[j][1] == result[p - 2] ||
                        combine[j][0] == result[p - 2] && combine[j][1] == result[p - 1])
                    {
                        result[p - 2] = combine[j][2];
                        p --;
                        go = true;
                        break;
                    }
                }
            }

            // oppose
            bool clear = false;
            for (int j = 0; j < d && !clear; j++)
            {
                if (p > 0 && result[p - 1] == oppose[j][0])
                {
                    for (int k = 0; k < p - 1 && !clear; k++)
                    {
                        if (result[k] == oppose[j][1])
                        {
                            clear = true;
                        }
                    }
                }

                if (p > 0 && result[p - 1] == oppose[j][1])
                {
                    for (int k = 0; k < p - 1 && !clear; k++)
                    {
                        if (result[k] == oppose[j][0])
                        {
                            clear = true;
                        }
                    }
                }
            }
            if (clear) p = 0;
        }
        result[p] = 0;

        printf("Case #%d: [", tc);
        for (int i = 0; i < p; i++)
        {
            if (i == 0) printf("%c", result[i]);
            else printf(", %c", result[i]);
        }
        printf("]\n", tc, result);
    }
}
