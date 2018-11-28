


#include <set>
#include <cstdio>
using namespace std;

long long x [1 << 17];
long long y [1 << 17];

long long am [100005][4][3][3];

int main ()
{
    int N;
    scanf ("%d", &N);
    for (int t = 0; t < N; ++t)
    {
        long long n, A, B, C, D, x0, y0, M;
        scanf ("%lld %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, &x0, &y0, &M);
//        long long x = x0, y = y0;
        x [0] = x0;
        y [0] = y0;
//        printf ("%lld %lld\n", x, y);
        for (int i = 1; i < n; ++i)
        {
            x [i] = (A * x [i - 1] + B) % M;
            y [i] = (C * y [i - 1] + D) % M;
//            printf ("%lld %lld\n", x, y);
        }
//      puts ("");
        
        //for (int i = 0; i < n; ++i)
        //    printf ("%d %d\n", (int) x [i], (int) y [i]);
        
        /*
        set <pair <long long, long long> > got;
        for (int i = 0; i < n; ++i)
            got.insert (make_pair (x [i], y [i]));
        
        long long res = 0;
        for (int a = 0; a < n; ++a)
            for (int b = a + 1; b < n; ++b)
                for (int c = b + 1; c < n; ++c)
                {
                    long long mx = x [a] + x [b] + x [c];
                    long long my = y [a] + y [b] + y [c];
                    if (mx % 3 != 0 || my % 3 != 0)
                        continue;
                    //if (got.count (make_pair (mx / 3, my / 3)))
                        ++res;
                }
                printf ("Case #%d: %lld\n", t + 1, res);
        */
        
        memset (am, 0, sizeof (am));
        am [0][0][0][0] = 1;
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j <= 3; ++j)
                for (int mx = 0; mx < 3; ++mx)
                    for (int my = 0; my < 3; ++my)
                    {
                        am [i + 1][j][mx][my] += am [i][j][mx][my];
                        if (j + 1 <= 3)
                            am [i + 1][j + 1][(mx + x [i]) % 3][(my + y [i]) % 3] += am [i][j][mx][my];
                    }
        }
        printf ("Case #%d: %lld\n", t + 1, am [n][3][0][0]);
    }
    return 0;
}