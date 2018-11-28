#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXV = 10000005, ITER = 150;

int C, D, V, vendor [MAXV];

bool works (double time)
{
    double lo = -1e100;

    for (int i = 0; i < V; i++)
    {
        double ilo = vendor [i] - (double) i * D - time, ihi = ilo + 2 * time;
        lo = max (lo, ilo);

        if (lo > ihi)
            return false;
    }

    return true;
}

double solve_case ()
{
    scanf ("%d %d", &C, &D);
    V = 0;

    for (int p, v, i = 0; i < C; i++)
    {
        scanf ("%d %d", &p, &v);

        while (v-- > 0)
            vendor [V++] = p;
    }

    double lo = 0, hi = 1e16;

    for (int it = 0; it < ITER; it++)
    {
        double mid = (lo + hi) / 2;

        if (works (mid))
            hi = mid;
        else
            lo = mid;
    }

    return lo;
}

int main ()
{
    int T; scanf ("%d", &T);

    for (int tc = 1; tc <= T; tc++)
        printf ("Case #%d: %.9lf\n", tc, solve_case ());

    return 0;
}
