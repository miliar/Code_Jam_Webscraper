#include <cstdio>
#include <cstring>
#include <set>
#include <cstdlib>
#include <ctime>
using namespace std;

const int MAXN = 1005, MAXY = 35, INF = 1000000005;

int TC, N, eind, deg [MAXN], eadj [2 * MAXN], eprev [2 * MAXN], elast [MAXN];
int front, back, q [MAXN], color [MAXN], can [MAXN][3];
set <pair <int, int> > players [MAXY];

inline void addedge (int a, int b)
{
    deg [a]++; eadj [eind] = b; eprev [eind] = elast [a]; elast [a] = eind++;
}

inline void neighbor (int ind, int x, int ny)
{
    if (players [ny].upper_bound (make_pair (x, MAXN)) != players [ny].end ())
    {
        addedge (ind, players [ny].upper_bound (make_pair (x, MAXN))->second);
        addedge (players [ny].upper_bound (make_pair (x, MAXN))->second, ind);
    }
}

void bfs (int start)
{
    front = back = 0;
    q [back++] = start;

    while (front < back)
    {
        int top = q [front++];

        for (int i = elast [top]; i != -1; i = eprev [i])
            if (color [eadj [i]] == -1)
            {
                color [eadj [i]] = color [top] ^ 1;
                q [back++] = eadj [i];
            }
    }
}

bool bipartite ()
{
    memset (color, -1, sizeof (color));

    for (int i = 0; i < N; i++)
        if (color [i] == -1)
            bfs (i);

    for (int i = 0; i < N; i++)
        for (int j = elast [i]; j != -1; j = eprev [j])
            if (color [i] == color [eadj [j]])
                return false;

    return true;
}

inline int good (int num)
{
    return (can [num][0] == 0 ? 1 : 0) + (can [num][1] == 0 ? 1 : 0) + (can [num][2] == 0 ? 1 : 0);
}

inline bool add (int num, int col)
{
    color [num] = col;

    for (int i = elast [num]; i != -1; i = eprev [i])
        can [eadj [i]][col]++;

    for (int i = elast [num]; i != -1; i = eprev [i])
        if (good (eadj [i]) == 0)
            return false;

    return true;
}

inline void remove (int num, int col)
{
    color [num] = -1;

    for (int i = elast [num]; i != -1; i = eprev [i])
        can [eadj [i]][col]--;
}

bool three (int num, bool start = false)
{
    int ind = -1;
    pair <int, int> best (INF, INF);

    for (int i = elast [num]; i != -1; i = eprev [i])
        if (color [eadj [i]] == -1)
            if (make_pair (good (eadj [i]), -deg [eadj [i]]) < best)
            {
                ind = eadj [i];
                best = make_pair (good (eadj [i]), -deg [eadj [i]]);
            }

    if (ind == -1)
        return true;

    if (best.first == 0)
        return false;

    for (int c = 0; c < 3; c++)
        if (can [ind][c] == 0)
        {
            if (add (ind, c) && three (ind))
            {
                if (three (num))
                    return true;
                else if (start)
                    break;
            }

            remove (ind, c);
        }

    return false;
}

bool tripartite ()
{
    memset (color, -1, sizeof (color));
    memset (can, 0, sizeof (can));

    for (int i = 0; i < N; i++)
        if (color [i] == -1)
        {
            add (i, 0);

            if (!three (i, true))
                return false;
        }

    return true;
}

int main ()
{
    srand (time (NULL));
    scanf ("%d", &TC);

    for (int tc = 1; tc <= TC; tc++)
    {
        scanf ("%d", &N);
        memset (elast, -1, sizeof (elast));
        memset (deg, 0, sizeof (deg));
        eind = 0;

        for (int y = 0; y < MAXY; y++)
            players [y].clear ();

        for (int i = 0, x, y; i < N; i++)
        {
            scanf ("%d %d", &x, &y);
            players [y].insert (make_pair (x, i));
        }

        for (int y = 0; y < MAXY; y++)
            for (set <pair <int, int> > :: iterator it = players [y].begin (); it != players [y].end (); it++)
            {
                neighbor (it->second, it->first, y - 1);
                neighbor (it->second, it->first, y);
                neighbor (it->second, it->first, y + 1);
            }

        if (eind == 0)
            printf ("Case #%d: 1\n", tc);
        else if (bipartite ())
            printf ("Case #%d: 2\n", tc);
        else if (tripartite ())
            printf ("Case #%d: 3\n", tc);
        else
            printf ("Case #%d: 4\n", tc);

        fflush (stdout);
    }

    return 0;
}
