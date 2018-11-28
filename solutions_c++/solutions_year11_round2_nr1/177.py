#include <cstdio>
using namespace std;

const int MAXN = 105;

int N;
char plays [MAXN][MAXN];
double wp [MAXN], owp [MAXN], oowp [MAXN];

double percentage (int num, int exclude)
{
    double win = 0, played = 0;

    for (int i = 0; i < N; i++)
        if (i != exclude)
            if (plays [num][i] == '0' || plays [num][i] == '1')
            {
                played++;

                if (plays [num][i] == '1')
                    win++;
            }

    return win / played;
}

void solve_case ()
{
    scanf ("%d", &N);

    for (int i = 0; i < N; i++)
        scanf ("%s", plays [i]);

    for (int i = 0; i < N; i++)
        wp [i] = percentage (i, -1);

    for (int i = 0; i < N; i++)
    {
        double sum = 0, opp = 0;

        for (int j = 0; j < N; j++)
            if (plays [i][j] != '.')
            {
                sum += percentage (j, i);
                opp++;
            }

        owp [i] = sum / opp;
    }

    for (int i = 0; i < N; i++)
    {
        double sum = 0, opp = 0;

        for (int j = 0; j < N; j++)
            if (plays [i][j] != '.')
            {
                sum += owp [j];
                opp++;
            }

        oowp [i] = sum / opp;
    }

    for (int i = 0; i < N; i++)
        printf ("%.9lf\n", 0.25 * wp [i] + 0.5 * owp [i] + 0.25 * oowp [i]);
}

int main ()
{
    int T; scanf ("%d", &T);

    for (int tc = 1; tc <= T; tc++)
    {
        printf ("Case #%d:\n", tc);
        solve_case ();
    }

    return 0;
}
