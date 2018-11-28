#include <cstdio>
#include <cstring>
#include <complex>
#include <cassert>
using namespace std;

const int MAXN = 45, ITER = 1000, BOUND = 2000;

int TC, N;
double prad [MAXN];
complex <double> plant [MAXN];

inline complex <double> rotate (complex <double> p)
{
    return complex <double> (p.imag (), -p.real ());
}

inline pair <complex <double>, complex <double> > center (int a, int b, double da, double db)
{
    double d = abs (plant [a] - plant [b]);
    assert (da + db >= d);

    double x = (d * d + da * da - db * db) / (2 * d);
    double y = sqrt (da * da - x * x);

    complex <double> ab = plant [b] - plant [a];
    ab /= d;

    return make_pair (plant [a] + x * ab + y * rotate (ab), plant [a] + x * ab - y * rotate (ab));
}

inline void modify (int a, int b, double R, complex <double> p, long long &tocov)
{
    for (int k = 0; k < N; k++)
        if (tocov & 1LL << k)
            if (k == a || k == b || (R - prad [k]) * (R - prad [k]) >= norm (p - plant [k]))
                tocov ^= 1LL << k;
}

bool cover (int depth, double R, long long tocov)
{
    if (depth >= 2)
        return tocov == 0;

    if (__builtin_popcountll (tocov) == 1)
    {
        for (int i = 0; i < N; i++)
            if (tocov & 1LL <<i)
                return R >= prad [i];
    }

    for (int i = 0; i < N; i++)
        if (tocov & 1LL << i)
            if (R >= prad [i])
            {
                tocov ^= 1LL << i;

                if (cover (depth + 1, R, tocov))
                    return true;

                tocov ^= 1LL << i;
            }

    for (int i = 0; i < N; i++)
        if (tocov & 1LL << i)
            for (int j = i + 1; j < N; j++)
                if (tocov & 1LL << j)
                {
                    double d = abs (plant [i] - plant [j]);

                    if (R - prad [i] + R - prad [j] < d)
                        continue;

                    pair <complex <double>, complex <double> > p = center (i, j, R - prad [i], R - prad [j]);
                    long long temp = tocov;
                    modify (i, j, R, p.first, tocov);

                    if (cover (depth + 1, R, tocov))
                        return true;

                    tocov = temp;
                    modify (i, j, R, p.second, tocov);

                    if (cover (depth + 1, R, tocov))
                        return true;
                }

    return false;
}

int main ()
{
    scanf ("%d", &TC);

    for (int tc = 1; tc <= TC; tc++)
    {
        scanf ("%d", &N);

        for (int i = 0; i < N; i++)
            scanf ("%lf %lf %lf", &plant [i].real (), &plant [i].imag (), prad + i);

        double lo = 0, hi = BOUND;

        for (int it = 0; it < ITER; it++)
        {
            double mid = (lo + hi) / 2;

            if (cover (0, mid, (1LL << N) - 1))
                hi = mid;
            else
                lo = mid;
        }

        printf ("Case #%d: %lf\n", tc, lo);
    }

    return 0;
}
