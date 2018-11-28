/* template for programming contests */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int verbose = 0;
int win_lose[100][100];
int team_win_lose[100];
int n;

double wp[100];
double owp[100];
double rpi[100];

/* clear out and initialize data structures for next input problem */
void reset_input()
{
}

/* read in input for next problem */
void read_input()
{
    scanf("%d", &n);
    for (int i=0; i < n; i++)
    {
        char buf[110];
        scanf("%s", buf);
        for (int j = 0; j < n; j++)
            if (buf[j] == '1')
                win_lose[i][j] = 1;
            else if (buf[j] == '0')
                win_lose[i][j] = 0;
            else if (buf[j] == '.')
                win_lose[i][j] = -1;
    }
}

/* print input for the current problem */
void print_input()
{
    fprintf(stderr, "input:\n");
    for (int i=0;i <n;i++)
    {
        for (int j=0;j <n;j++)
        {
            printf("%4d", win_lose[i][j]);
        }
        printf("\n");
    }
}

double win_pct(int team)
{
    int win = 0, total = 0;
    double result;

    for (int oppo = 0; oppo < n; oppo++)
    {
        if (win_lose[team][oppo] != -1)
        {
            total++;
            if (win_lose[team][oppo] == 1)
                win++;
        }
    }
    if (total == 0) result = 0.;
    else            result = (double) win / (double) total;

    return result;
}

/* solve the current problem */
void solve_it()
{
    /* compute each team's winning percentage */
    for (int team = 0; team < n; team++)
    {
        wp[team] = win_pct(team);
        if (verbose) printf("team %d; wp %.12f\n", team, wp[team]);
    }

    /* compute each team's opponents' winning percentage */
    for (int team = 0; team < n; team++)
    {
        double oppo_wp = 0.;
        double oppo_wp_total = 0.;
        int oppo_count = 0;
        int i;

        for (i = 0; i < n; i++)
        {
            team_win_lose[i] = win_lose[i][team];
            win_lose[i][team] = -1;
        }

        if (verbose > 1)
        {
            printf("team %d owp matrix:\n", team);
            print_input();
        }

        for (int oppo = 0; oppo < n; oppo++)
        {
            if (team_win_lose[oppo] == -1)
                continue;

            oppo_wp = win_pct(oppo);
            oppo_wp_total += oppo_wp;
            oppo_count++;
            if (verbose) printf("team %d, oppo %d, oppo_wp %.12f\n",
                    team, oppo, oppo_wp);

        }

        for (i = 0; i < n; i++)
            win_lose[i][team] = team_win_lose[i];

        if (oppo_count == 0) owp[team] = 0.;
        else owp[team] = oppo_wp_total / (double) oppo_count;

        if (verbose)
            printf("team %d owp %.12f\n", team, owp[team]);
    }

    /* compute each team's RPI */
    for (int team = 0; team < n; team++)
    {
        double total = 0, oowp = 0.;
        int oppo_count = 0;
        rpi[team] = 0.25 * wp[team];

        rpi[team] += 0.5 * owp[team];

        for (int oppo = 0; oppo < n; oppo++)
        {
            if (win_lose[team][oppo] == -1)
                continue;

            total += owp[oppo];
            oppo_count++;
        }

        if (oppo_count > 0)
            oowp += total / (double) oppo_count;

        if (verbose)
            printf("avg oppo owp %.12f\n", oowp);

        rpi[team] += 0.25 * oowp;
    }
}

/* print the solution for the current problem */
void print_soln()
{
    for (int team = 0; team < n; team++)
        printf("\n%.12f", rpi[team]);
}

/* read in, solve, and print solution to one problem in the input */
void do_game(int game)
{
    reset_input();

    read_input();

    if (verbose)
        print_input();

    solve_it();

    printf("Case #%d:  ", game + 1);

    print_soln();

    printf("\n");
}

/* process a file containing a sequence of problems */
int main(int argc, char **argv)
{
    int games, game, just_game = -1;

    if (argc > 1)
    {
        for (int i = 1; i < argc; i++)
        {
            if (strcmp("-v", argv[i]) == 0)
                verbose++;
            else if (strcmp("-g", argv[i]) == 0)
            {
                if (++i >= argc || sscanf(argv[i], "%d", &just_game) != 1)
                {
                    fprintf(stderr, "bad arg line\n");
                    exit(1);
                }
                just_game--;
            }
            else
            {
                fprintf(stderr, "bad arg line\n");
                exit(1);
            }
        }
    }

    scanf("%d", &games);

    for (game = 0; game < games; game++)
    {
        if (just_game != -1 && game != just_game)
            read_input();
        else
            do_game(game);
    }
}
