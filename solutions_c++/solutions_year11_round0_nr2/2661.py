
#include <stdio.h>

#define Nmax  100

char combine[26][26];
unsigned long oppose[26];

int main()
{
    char T, N, I, x, n, i;
    char y0[Nmax * 3 - 2 + 1];
    char *y;
    unsigned long trigger;
    char s0[Nmax + 1];
    char last;

    scanf("%d ", &T);
    for (x = 0; x < T; x ++)
    {
        for (i = 0; i < 26; i ++)
        {
            oppose[i] = 0;
            for (n = 0; n < 26; n ++)
                combine[i][n] = 0;
        }

        scanf("%d ", &I);
        for (i = 0; i < I; i ++)
        {
            scanf("%s ", s0);
            combine[s0[0] - 'A'][s0[1] - 'A'] = combine[s0[1] - 'A'][s0[0] - 'A'] = s0[2];
        }

        scanf("%d ", &I);
        for (i = 0; i < I; i ++)
        {
            scanf("%s ", s0);
            oppose[s0[0] - 'A'] |= 1 << (s0[1] - 'A');
            oppose[s0[1] - 'A'] |= 1 << (s0[0] - 'A');
        }

        scanf("%d ", &N);
        scanf("%s ", s0);

        y = y0;
        last = 0;
        trigger = 0;
        for (n = 0; n < N; n ++)
        {
            if (last)
            {
                if (combine[last - 'A'][s0[n] - 'A'])
                {
                    last = combine[last - 'A'][s0[n] - 'A'];
                    continue;
                }

                if (y != y0)
                {
                    *y++ = ',';
                    *y++ = ' ';
                }
                *y++ = last;
                trigger |= oppose[last - 'A'];
            }
            last = s0[n];

            if (trigger & (1 << (last - 'A')))
            {
                y = y0;
                last = 0;
                trigger = 0;
            }
        }

        if (last)
        {
            if (y != y0)
            {
                *y++ = ',';
                *y++ = ' ';
            }
            *y++ = last;
        }
        *y = 0;
        printf("Case #%d: [%s]\n", x + 1, y0);
    }
}
