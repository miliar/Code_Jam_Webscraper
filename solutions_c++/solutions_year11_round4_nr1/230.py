#include <algorithm>
#include <stdio.h>

#define MAX 1024
#define mp make_pair
#define f first
#define s second

using namespace std;

int testCases;
double x, s, r, t, n;
pair <double, double> lr[MAX];

int main()
{
    freopen("a-small.in", "r", stdin);
    freopen("a-small.out", "w", stdout);

    int test = 0;
    for (scanf("%d", &testCases); testCases; testCases--)
    {
        test++;
        printf("Case #%d: ", test);

        scanf("%lf %lf %lf %lf %lf", &x, &s, &r, &t, &n);

        ++n;
        lr[(int) n] = mp((double) 0, x);
        for (int i = 1; i < n; i++)
        {
            double st, fn;
            scanf("%lf %lf %lf", &st, &fn, &lr[i].f);
            lr[i].s = fn - st;

            lr[(int) n].s -= fn - st;
        }

        sort(lr + 1, lr + 1 + (int) n);

        double solT = 0;
        for (int i = 1; i <= n; i++)
            if (t * (r + lr[i].f) >= lr[i].s)
            {
                t -= lr[i].s / (r + lr[i].f);
                solT += lr[i].s / (r + lr[i].f);
            }
            else
            {
                double d = lr[i].s - t * (r + lr[i].f);
                solT += t;
                t = 0;
                solT += d / (s + lr[i].f);
            }

        printf("%lf\n", solT);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
