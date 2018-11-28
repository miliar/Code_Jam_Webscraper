#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <string>

typedef long long int64;


int n;
double xs[1000], ys[1000], zs[1000], p[1000];

double calc(double x, double y, double z)
{
    double res = 0;
    for (int i = 0; i < n; i++)
        res = std::max(res, (std::fabs(x-xs[i]) + std::fabs(y-ys[i]) + std::fabs(z-zs[i])) / p[i]);
    return res;
}

double curr;

void improve(double &x, double &y, double &z, double scale)
{
    for (int i = 0; i < 10; i++) {
        for (double dx = -1; dx <= 1; dx++)
        for (double dy = -1; dy <= 1; dy++)
        for (double dz = -1; dz <= 1; dz++) {
            x += scale * dx;
            y += scale * dy;
            z += scale * dz;
            double next = calc(x, y, z);
            if (next < curr)
                curr = next;
            else {
                x -= scale * dx;
                y -= scale * dy;
                z -= scale * dz;
            }
        }
    }
}

void solve()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%lf%lf%lf%lf", &xs[i], &ys[i], &zs[i], &p[i]);

    double x = 500000;
    double y = 500000;
    double z = 500000;

    curr = calc(x, y, z);

    improve(x, y, z, 500000);
    improve(x, y, z, 100000);
    improve(x, y, z,  10000);
    improve(x, y, z,   1000);
    improve(x, y, z,    100);
    improve(x, y, z,     10);
    improve(x, y, z,      1);
    improve(x, y, z,      0.1);
    improve(x, y, z,      0.01);
    improve(x, y, z,      0.001);
    improve(x, y, z,      0.0001);
    improve(x, y, z,      0.00001);
    improve(x, y, z,      0.000001);
    improve(x, y, z,      0.0000001);
    improve(x, y, z,      0.00000001);

    printf("%lf", curr);
}

int main()
{
    int n_cases;
    scanf("%d", &n_cases);

    for (int i = 0; i < n_cases; i++) {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }
}

