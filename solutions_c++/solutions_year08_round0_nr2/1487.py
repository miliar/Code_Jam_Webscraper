#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;

const int MAXN = 205;

struct event
{
    int start, end, type;

    inline bool operator < (const event &o) const
    {
        return start < o.start;
    }
};

int C, N, A, B, ans [2], T;
priority_queue <int, vector <int>, greater <int> > trains [2];
event trips [MAXN];

inline int parse ()
{
    int h, m;
    scanf ("%d:%d", &h, &m);
    return h * 60 + m;
}

int main ()
{
    scanf ("%d", &C);

    for (int c = 0; c < C; c++)
    {
        scanf ("%d %d %d", &T, &A, &B);
        N = A + B; ans [0] = ans [1] = 0;

        for (int i = 0; i < N; i++)
            trips [i] = (event) {parse (), parse (), i < A ? 0 : 1};

        sort (trips, trips + N);

        while (!trains [0].empty ()) trains [0].pop ();
        while (!trains [1].empty ()) trains [1].pop ();

        for (int i = 0; i < N; i++)
        {
            if (trains [trips [i].type].empty () || trains [trips [i].type].top () > trips [i].start)
            {
                ans [trips [i].type]++;
                trains [trips [i].type].push (0);
            }

            trains [trips [i].type].pop ();
            trains [trips [i].type ^ 1].push (trips [i].end + T);
        }

        printf ("Case #%d: %d %d\n", c + 1, ans [0], ans [1]);
    }

    return 0;
}
