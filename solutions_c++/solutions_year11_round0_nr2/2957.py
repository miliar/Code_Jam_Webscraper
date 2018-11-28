#include <stdio.h>
#include <string.h>

int verbose = 0;

char combine[26][26];
char oppose[26][26];

void do_game(int game)
{
    int C_combine, D_oppose, N, i, j;
    char buf[10];
    char list[10000];
    int next = 0;
    char input[200];
    int next_ipt = 0;

    memset(combine, 0, sizeof(combine));
    memset(oppose, 0, sizeof(oppose));

    scanf("%d", &C_combine);

    for (i = 0; i < C_combine; i++)
    {
        scanf("%s", buf);
        combine[(int)buf[0] - 'A'][(int)buf[1] - 'A'] = buf[2];
        combine[(int)buf[1] - 'A'][(int)buf[0] - 'A'] = buf[2];
    }

    scanf("%d", &D_oppose);

    for (i = 0; i < D_oppose; i++)
    {
        scanf("%s", buf);
        oppose[(int)buf[0] - 'A'][(int)buf[1] - 'A'] = 1;
        oppose[(int)buf[1] - 'A'][(int)buf[0] - 'A'] = 1;
    }

    scanf("%d", &N);

    scanf("%s", input);

    for (i = 0; i < N; i++)
    {
        char c;
        c = input[next_ipt++];

        if (next == 0)
        {
            list[next++] = c;
            if (verbose) fprintf(stderr, "push first char\n");
            continue;
        }

        if (combine[(int) list[next-1] - 'A'][(int) c - 'A'] != 0)
        {
            list[next-1] = combine[(int) list[next-1] - 'A'][(int) c - 'A'];
            if (verbose) fprintf(stderr, "do a combine..\n");
            continue;
        }

        for (j = 0; j < next; j++)
        {
            if (oppose[(int) list[j] - 'A'][(int) c - 'A'])
            {
                next = 0;
                if (verbose) fprintf(stderr, "do an oppose..\n");
                goto done;
            }
        }

        list[next++] = c;
        if (verbose) fprintf(stderr, "do a push..\n");
        done:;
    }

    printf("Case #%d:  [", game + 1);
    for (i = 0; i < next; i++)
    {
        if (i > 0) printf(", ");
        printf("%c", list[i]);
    }
    printf("]\n");
}

int main(int argc, char **argv)
{
    int games, game;
    scanf("%d", &games);

    for (game = 0; game < games; game++)
    {
        do_game(game);
    }
}
