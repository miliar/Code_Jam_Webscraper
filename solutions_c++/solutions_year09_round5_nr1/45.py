#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
using namespace std;

const int MAX = 12, dr [] = {-1, 0, 1, 0}, dc [] = {0, 1, 0, -1};

struct state
{
    vector <pair <int, int> > box;

    inline long long hash ()
    {
        sort (box.begin (), box.end ());
        long long h = 0;

        for (int i = 0; i < (int) box.size (); i++)
        {
            h = h * MAX + box [i].first;
            h = h * MAX + box [i].second;
        }

        return h;
    }
};

int TC, R, C, B;
char grid [MAX + 5][MAX + 5];
state S, E;
queue <state> q;
map <long long, int> dist;

inline bool contain (state s, int r, int c)
{
    for (int i = 0; i < B; i++)
        if (s.box [i] == make_pair (r, c))
            return true;

    return false;
}

inline bool empty (state s, int r, int c)
{
    if (r < 0 || r >= R || c < 0 || c >= C || grid [r][c] == '#')
        return false;

    return !contain (s, r, c);    
}

inline bool danger (state s)
{
    queue <pair <int, int> > pq;
    pq.push (s.box [0]);
    bool done [5];
    memset (done, false, sizeof (done));
    done [0] = true;

    while (!pq.empty ())
    {
        pair <int, int> top = pq.front (); pq.pop ();

        for (int i = 0; i < B; i++)
            if (!done [i] && abs (s.box [i].first - top.first) + abs (s.box [i].second - top.second) == 1)
            {
                done [i] = true;
                pq.push (s.box [i]);
            }
    }

    for (int i = 0; i < B; i++)
        if (!done [i])
            return true;

    return false;
}

void bfs ()
{
    dist.clear ();
    q = queue <state> ();
    q.push (S);
    dist [S.hash ()] = 0;

    while (!q.empty ())
    {
        state top = q.front (); q.pop ();

        for (int i = 0; i < B; i++)
            for (int d = 0; d < 4; d++)
                if (empty (top, top.box [i].first + dr [d], top.box [i].second + dc [d]) && empty (top, top.box [i].first - dr [d], top.box [i].second - dc [d]))
                {
                    state next = top;
                    next.box [i].first += dr [d];
                    next.box [i].second += dc [d];

                    if (!danger (top) || !danger (next))
                        if (dist.find (next.hash ()) == dist.end () || dist [top.hash ()] + 1 < dist [next.hash ()])
                        {
                            dist [next.hash ()] = dist [top.hash ()] + 1;
                            q.push (next);
                        }
                }
    }
}

int main ()
{
    scanf ("%d", &TC);

    for (int tc = 1; tc <= TC; tc++)
    {
        S.box.clear ();
        E.box.clear ();
        B = 0;
        scanf ("%d %d", &R, &C);

        for (int i = 0; i < R; i++)
        {
            scanf ("%s", grid [i]);

            for (int j = 0; j < C; j++)
            {
                if (grid [i][j] == 'o' || grid [i][j] == 'w')
                {
                    S.box.push_back (make_pair (i, j));
                    B++;
                }

                if (grid [i][j] == 'x' || grid [i][j] == 'w')
                    E.box.push_back (make_pair (i, j));

                if (grid [i][j] != '.' && grid [i][j] != '#')
                    grid [i][j] = '.';
            }
        }

        bfs ();
        printf ("Case #%d: %d\n", tc, dist.find (E.hash ()) == dist.end () ? -1 : dist [E.hash ()]);
        fflush (stdout);
    }

    return 0;
}
