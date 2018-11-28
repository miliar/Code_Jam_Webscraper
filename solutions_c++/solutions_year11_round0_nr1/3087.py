#include <stdio.h>
#include <string.h>

int verbose = 0;

int goal[100];
int orange[100];
int goal_count = 0;
int next_goal;

void update_position(int *pos, int i_am_orange)
{
    int i;

    for (i = next_goal; i < goal_count; i++)
    {
        if (orange[i] != i_am_orange)
            continue;

        if (goal[i] < *pos)
            (*pos)--;

        else if (goal[i] > *pos)
            (*pos)++;

        break;
    }
}

void do_game(int game)
{
    int N, i;
    int pos_o, pos_b;
    int tick;

    scanf("%d", &N);

    goal_count = 0;

    for (i = 0; i < N; i++)
    {
        char buf[2];

        scanf("%s", buf);
        scanf("%d", &goal[goal_count++]);

        if (buf[0] == 'O')
            orange[goal_count - 1] = 1;
        else
            orange[goal_count - 1] = 0;
    }

    if (verbose)
    {
        for (i = 0; i < goal_count; i++)
            printf("%c %d ", orange[i] ? 'O' : 'B', goal[i]);

        printf("\n");
    }

    pos_o = 1;
    pos_b = 1;
    next_goal = 0;
    tick = 0;
    while (next_goal < goal_count)
    {
        int orange_did_button = 0, blue_did_button = 0;

        tick++;

        if (verbose)
            printf("tick %d\n", tick);

        if (orange[next_goal] && (pos_o == goal[next_goal]))
        {
            if (verbose)
                printf("orange pressed button %d\n", pos_o);

            next_goal++;

            if (next_goal == goal_count)
                break;

            orange_did_button = 1;
        }

        if (!orange_did_button && !orange[next_goal]
            && (pos_b == goal[next_goal]))
        {
            if (verbose)
                printf("blue pressed button %d\n", pos_b);

            next_goal++;

            if (next_goal == goal_count)
                break;

            blue_did_button = 1;
        }

        if (!orange_did_button)
        {
            update_position(&pos_o, 1 /* orange */);
        }

        if (!blue_did_button)
        {
            update_position(&pos_b, 0 /* not orange */);
        }

        if (verbose)
            printf("orange position %d, blue position %d\n", pos_o, pos_b);
    }

    printf("Case #%d:  ", game + 1);

    printf("%d", tick);

    printf("\n");
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
