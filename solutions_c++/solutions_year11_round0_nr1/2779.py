
#include <stdio.h>

#define Nmax  100

#define ORANGE  0
#define BLUE    1

unsigned char which[2][Nmax + 1];
unsigned char who[Nmax];

int main()
{
    unsigned char T, N, x, n, w, r, nn;
    unsigned char where[2], next[2];
    unsigned long int y;

    scanf("%u ", &T);
    for (x = 0; x < T; x ++)
    {
        scanf("%u ", &N);
        next[0] = next[1] = 0;
        for (n = 0; n < N; n ++)
        {
            scanf("%c ", &w);
            who[n] = w == 'O' ? ORANGE : BLUE;
            scanf("%u ", &which[who[n]][next[who[n]]++]);
        }
        which[0][next[0]] = which[1][next[1]] = 0;

        next[0] = next[1] = 0;
        where[0] = where[1] = 1;
        for (n = nn = 0, y = 0; n < N; n = nn, y ++)
            for (r = 0; r < 2; r ++)
                if (which[r][next[r]])
                {
                    if (where[r] < which[r][next[r]])
                        where[r] ++;

                    else
                    if (where[r] > which[r][next[r]])
                        where[r] --;

                    else
                    if (who[n] == r)
                    {
                        next[r] ++;
                        nn ++;
                    }
                }

        printf("Case #%u: %lu\n", x + 1, y);
    }
}
