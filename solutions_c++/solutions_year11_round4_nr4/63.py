#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

const int MAXP = 405;

int P, W, dist [MAXP][MAXP];
bool edge [MAXP][MAXP];
vector <int> adj [MAXP];
bool chosen [MAXP];

inline int threaten ()
{
    int count = 0;

    for (int i = 0; i < P; i++)
    {
        bool neighbor = false;

        for (int j = 0; j < (int) adj [i].size (); j++)
            if (chosen [adj [i][j]])
                neighbor = true;

        if (!chosen [i] && neighbor)
            count++;
    }

    return count;
}

int solve (int num)
{
    if (num == 1)
        return threaten ();

    chosen [num] = true;
    int most = 0;

    for (int i = 0; i < (int) adj [num].size (); i++)
        if (dist [0][adj [num][i]] == dist [0][num] + 1 && dist [adj [num][i]][1] + 1 == dist [num][1])
            most = max (most, solve (adj [num][i]));

    chosen [num] = false;
    return most;
}

void solve_case ()
{
    scanf ("%d %d", &P, &W);

    for (int i = 0; i < MAXP; i++)
        adj [i].clear ();

    memset (dist, 63, sizeof (dist));
    memset (edge, false, sizeof (edge));

    for (int a, b, i = 0; i < W; i++)
    {
        scanf ("%d,%d", &a, &b);
        adj [a].push_back (b);
        adj [b].push_back (a);
        edge [a][b] = edge [b][a] = true;
        dist [a][b] = dist [b][a] = 1;
    }

    for (int i = 0; i < P; i++)
        dist [i][i] = 0;

    for (int k = 0; k < P; k++)
        for (int i = 0; i < P; i++)
            for (int j = 0; j < P; j++)
                dist [i][j] = min (dist [i][j], dist [i][k] + dist [k][j]);

    printf ("%d %d\n", dist [0][1] - 1, solve (0));
}

int main ()
{
    int T; scanf ("%d", &T);

    for (int tc = 1; tc <= T; tc++)
    {
        printf ("Case #%d: ", tc);
        solve_case ();
    }

    return 0;
}
