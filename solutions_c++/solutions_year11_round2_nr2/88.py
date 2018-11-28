#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 1111111;

int d, c;
int a[MAXN];
int n, m, x;
long double ll, rr, cc;

int main()
{
    freopen("in", "rt", stdin);
    freopen("out", "wt", stdout);

    int ctest = 0;
    scanf("%d", &ctest);
    for (int itest = 1; itest <= ctest; itest++)
    {

        scanf("%d %d", &c, &d);
        n = 0;

        for (int i = 0; i < c; i++)
        {
            scanf("%d %d", &x, &m);
            for (int j = 0; j < m; j++)
                a[n++] = x;
        }
//        printf("%d %d\n", c, d);

        ll = 0;
        rr = (long double)d * (long double)n;
        while (ll + 1e-7 < rr)
        {
            cc = (ll + rr) / 2;
            long double x = -1e+30;
            bool f = true;

            for (int i = 0; i < n && f; i++)
            {
                x = max(x + d, a[i] - cc);
                f &= x <= a[i] + cc;
            }

            if (f)
                rr = cc;
            else
                ll = cc;

//            printf("%.10lf %.10lf\n", (double)ll, (double)rr);
        }         
        printf("Case #%d: ", itest);
        printf("%.10lf\n", (double)rr);
        fflush(stdout);
    }


    return 0;
}