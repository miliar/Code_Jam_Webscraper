#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#define MAXN 2000100
using namespace std;
int t, n;
double delta;
int tt;
double start[MAXN];
double x[MAXN], y[MAXN];
bool okay(double time)
{

    for (int i = 1; i <= n; ++i)
    {
        x[i] = (double)start[i] - time;
        y[i] = (double)start[i] + time;
    }
    /*if (time)
    {
        printf("%.2f\n", time);
        for (int i = 1; i <= n; ++i)
            printf("%.2f %.2f\n", x[i], y[i]);
        system("pause");
    }*/
    double last = x[1];
    for (int i = 2; i <= n; ++i)
    {
        if (y[i] < last + (double)delta) { /*printf("%d\n", i);*/return false;}
        last = max(last + (double)delta, x[i]);
    }
    return true;
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &t);
    for (int ca = 1; ca <= t; ++ca)
    {
        double a, b;
        tt = 0;
        memset(x, 0, sizeof(x));
        memset(y, 0, sizeof(y));
        scanf("%d%lf", &n, &delta);
        for (int i = 1; i <= n; ++i)
        {
            scanf("%lf%lf", &a, &b);
            for (int j = 1; j <= b; ++j)
                start[++tt] = a;
        }
        n = tt;
        //printf("AAA\n");
        sort(start + 1, start + 1 + n);
        //printf("BBB\n");
        /*for (int i = 1; i <= n; ++i)
            printf("%.2f\n", start[i]);*/
        double l = 0, r = 1e12;
        while (fabs(r - l) > 1e-2)
        {
            if (okay((l + r) / 2.0)) r = (l + r) / 2.0;
            else l = (l + r) / 2.0;
        }
        printf("Case #%d: %.1f\n", ca, l);
    }
    return 0;
}
