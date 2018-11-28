#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 1005, ITER = 100;
const double BOUND = 5000000, DINF = 1e10;

int T, N, x [MAXN], y [MAXN], z [MAXN], p [MAXN];

inline pair <double, double> inter (pair <double, double> a, pair <double, double> b)
{
    return make_pair (max (a.first, b.first), min (a.second, b.second));
}

bool works (double cp)
{
    pair <double, double> reg1, reg2, reg3, reg4;
    reg1 = reg2 = reg3 = reg4 = make_pair (-DINF, DINF);

    for (int i = 0; i < N; i++)
    {
        reg1 = inter (reg1, make_pair (x [i] + y [i] + z [i] - p [i] * cp, x [i] + y [i] + z [i] + p [i] * cp));
        reg2 = inter (reg2, make_pair (x [i] + y [i] - z [i] - p [i] * cp, x [i] + y [i] - z [i] + p [i] * cp));
        reg3 = inter (reg3, make_pair (x [i] - y [i] + z [i] - p [i] * cp, x [i] - y [i] + z [i] + p [i] * cp));
        reg4 = inter (reg4, make_pair (x [i] - y [i] - z [i] - p [i] * cp, x [i] - y [i] - z [i] + p [i] * cp));
    }

    if (reg1.first > reg1.second) return false;
    if (reg2.first > reg2.second) return false;
    if (reg3.first > reg3.second) return false;
    if (reg4.first > reg4.second) return false;

    pair <double, double> x1 = make_pair (reg1.first + reg4.first, reg1.second + reg4.second);
    pair <double, double> x2 = make_pair (reg2.first + reg3.first, reg2.second + reg3.second);

    pair <double, double> check = inter (x1, x2);

    return check.first < check.second;
}

int main ()
{
    scanf ("%d", &T);

    for (int t = 1; t <= T; t++)
    {
        scanf ("%d", &N);

        for (int i = 0; i < N; i++)
            scanf ("%d %d %d %d", x + i, y + i, z + i, p + i);

        double lo = 0, hi = BOUND, mid;

        for (int i = 0; i < ITER; i++)
        {
            mid = (lo + hi) / 2;

            if (works (mid))
                hi = mid;
            else
                lo = mid;
        }

        printf ("Case #%d: %lf\n", t, (lo + hi) / 2);
    }

    return 0;
}
