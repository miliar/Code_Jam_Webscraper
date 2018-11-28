#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXA = 1005, MAXB = 1005, MAXE = 100005, INF = 1000000005;

struct DfsMatch
{
    int A, B, eind, eadj [MAXE], eprev [MAXE], elast [MAXA];
    int start, vis [MAXA], prev [MAXB];

    inline DfsMatch ()
    {
        A = B = -1;
    }

    inline void init (int a, int b)
    {
        A = a; B = b; eind = 0;
        memset (elast, -1, A * sizeof (int));
    }

    inline void addedge (int a, int b)
    {
        eadj [eind] = b; eprev [eind] = elast [a]; elast [a] = eind++;
    }

    bool dfs (int num)
    {
        if (vis [num] == start)
            return false;

        vis [num] = start;

        for (int i = elast [num]; i != -1; i = eprev [i])
            if (prev [eadj [i]] == -1)
            {
                prev [eadj [i]] = num;
                return true;
            }

        for (int i = elast [num]; i != -1; i = eprev [i])
            if (dfs (prev [eadj [i]]))
            {
                prev [eadj [i]] = num;
                return true;
            }

        return false;
    }

    int match ()
    {
        if (A == -1 && B == -1)
            return -INF;

        memset (prev, -1, B * sizeof (int));
        memset (vis, -1, A * sizeof (int));
        int total = 0;

        for (int i = 0; i < A; i++)
        {
            start = i;

            if (dfs (i))
                total++;
        }

        return total;
    }
};

const int MAXN = 1005, MAXK = 300;

struct klist
{
    int price [MAXK];

    inline bool operator < (const klist &o) const
    {
        return price [0] > o.price [0];
    }
};

int TC, N, K;
klist stock [MAXN];
DfsMatch graph;

int main ()
{
    scanf ("%d", &TC);

    for (int tc = 1; tc <= TC; tc++)
    {
        scanf ("%d %d", &N, &K);
        graph.init (N, N);

        for (int i = 0; i < N; i++)
            for (int j = 0; j < K; j++)
                scanf ("%d", &stock [i].price [j]);

        sort (stock, stock + N);

        for (int i = 0; i < N; i++)
            for (int j = i + 1; j < N; j++)
            {
                bool more = true;

                for (int k = 0; k < K; k++)
                    if (stock [i].price [k] <= stock [j].price [k])
                        more = false;

                if (more)
                    graph.addedge (i, j);
            }

        printf ("Case #%d: %d\n", tc, N - graph.match ());
    }

    return 0;
}
