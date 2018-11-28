
#include <stdio.h>

#define Nmax  1000

unsigned long values[Nmax];

int main()
{
    unsigned char T, N, x, n;
    unsigned long xum, sum, min;

    scanf("%u ", &T);
    for (x = 0; x < T; x ++)
    {
        scanf("%u ", &N);
        xum = sum = 0;
        min = 0xffffffff;
        for (n = 0; n < N; n ++)
        {
            scanf("%lu ", &values[n]);
            xum ^= values[n];
            sum += values[n];
            if (min > values[n]) min = values[n];
        }

        if (xum)
            printf("Case #%u: NO\n", x + 1);

        else
            printf("Case #%u: %lu\n", x + 1, sum - min);
    }
}
