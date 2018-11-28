#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAX = 52, INF = 1000000005;

int TC, R, C, F, dp [MAX][MAX][MAX][MAX];
char grid [MAX][MAX];

inline int fall (int r, int c, int b, int e)
{
    if (grid [r][c] == '#' && (c < b || c > e))
        return INF;

    int f = 0;

    while (r < R - 1 && grid [r + 1][c] == '.')
    {
        r++;
        f++;
    }

    return f;
}

int solve (int r, int c, int b, int e)
{
    if (r == R - 1)
        return 0;

    if (dp [r][c][b][e] != -1)
        return dp [r][c][b][e];

    int &sol = dp [r][c][b][e] = INF;
    int begin = c, end = c;

    while (begin - 1 >= 0 && ((begin - 1 >= b && begin - 1 <= e) || grid [r][begin - 1] == '.') && grid [r + 1][begin - 1] == '#')
        begin--;

    while (end + 1 < C && ((end + 1 >= b && end + 1 <= e) || grid [r][end + 1] == '.') && grid [r + 1][end + 1] == '#')
        end++;

    if (begin - 1 >= 0)
    {
        int f = fall (r, begin - 1, b, e);

        if (f <= F)
            sol = min (sol, solve (r + f, begin - 1, begin - 1, begin - 1));
    }

    if (end + 1 < C)
    {
        int f = fall (r, end + 1, b, e);

        if (f <= F)
            sol = min (sol, solve (r + f, end + 1, end + 1, end + 1));
    }

    for (int i = begin; i <= end; i++)
        for (int j = i; j <= end; j++)
        {
            if (i > begin)
            {
                grid [r + 1][i] = '.';
                int f = fall (r, i, b, e);

                if (f <= F)
                    sol = min (sol, solve (r + f, i, i, f == 1 ? j : i) + j - i + 1);

                grid [r + 1][i] = '#';
            }

            if (j < end)
            {
                grid [r + 1][j] = '.';
                int f = fall (r, j, b, e);

                if (f <= F)
                    sol = min (sol, solve (r + f, j, f == 1 ? i : j, j) + j - i + 1);

                grid [r + 1][j] = '#';
            }
        }

    return sol;
}

int main ()
{
    scanf ("%d", &TC);

    for (int tc = 1; tc <= TC; tc++)
    {
        scanf ("%d %d %d", &R, &C, &F);

        for (int i = 0; i < R; i++)
            scanf ("%s", grid [i]);

        memset (dp, -1, sizeof (dp));

        if (solve (0, 0, 0, 0) < INF)
            printf ("Case #%d: Yes %d\n", tc, solve (0, 0, 0, 0));
        else
            printf ("Case #%d: No\n", tc);

        fprintf (stderr, "Finished %d\n", tc);
    }

    return 0;
}
