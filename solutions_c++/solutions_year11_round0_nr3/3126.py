#include <stdio.h>
#include <string.h>

int verbose = 0;

char combine[26][26];
char oppose[26][26];

int sum(int *set, int len)
{
    int result = 0, i;

    for (i = 0; i < len; i++)
    {
        result ^= set[i];
    }

    return result;
}

void do_game(int game)
{
    int N_candies, i, j;
    int candies[10000];
    int two_tothe_n;
    int set1[10000], set2[10000];
    int set1_next, set2_next;
    int total, max = -1;

    scanf("%d", &N_candies);

    for (i = 0; i < N_candies; i++)
        scanf("%d", &candies[i]);

    two_tothe_n = 1;
    for (i = 0; i < N_candies; i++)
        two_tothe_n *= 2;

    for (i = 0; i < two_tothe_n; i++)
    {
        int bits = i;
        set1_next = 0;
        set2_next = 0;
        for (j = 0; j < N_candies; j++)
        {
            if (bits & 1)
                set1[set1_next++] = candies[j];
            else
                set2[set2_next++] = candies[j];

            bits >>= 1;
        }

        if (set1_next == 0 || set2_next == 0)
            continue;

        if (verbose) {

            for (j = 0; j < set1_next; j++)
                printf("%d ", set1[j]);

            printf("|");

            for (j = 0; j < set2_next; j++)
                printf("%d ", set2[j]);

            printf("|");

            int s1 = sum(set1, set1_next);
            int s2 = sum(set2, set2_next);

            printf ("%d %d\n", s1, s2);
            printf("\n");
        }

        if (sum(set1, set1_next) != sum(set2, set2_next))
            continue;

        total = 0;
        for (j = 0; j < set1_next; j++)
            total += set1[j];

        if (total > max)
            max = total;
    }
    printf("Case #%d:  ", game + 1);

    if (max == -1)
        printf("NO");
    else
        printf("%d", max);

    printf("\n");
}

int main(int argc, char **argv)
{
    int games, game;
    scanf("%d", &games);

    #if 0
    while (1) {
        int test[10], len, i;
        scanf("%d", &len);
        for (i = 0; i < len; i++)
            scanf("%d", &test[i]);
        printf("%d\n", sum(test, len));
    }
    #endif

    for (game = 0; game < games; game++)
    {
        do_game(game);
    }
}
