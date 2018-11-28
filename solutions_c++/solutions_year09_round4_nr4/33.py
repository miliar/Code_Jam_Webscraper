#include <stdio.h>
#include <math.h>

int n;
int x[100], y[100], r[100];

double cover (int i, int j)
{
    return (r[i] + r[j] + sqrt((x[i] - x[j]) * (double)(x[i] - x[j]) + (y[i] - y[j]) * (double)(y[i] - y[j]))) / 2;
}

double max (double x, double y)
{
    return x > y ? x : y;
}

double min3 (double x, double y, double z)
{
    return -max(max(-x, -y), -z);
}

int main ()
{
    int t, ct = 0;
    
    for (scanf("%d", &t); t > 0; t --)
    {
        scanf("%d", &n);
        for (int i = 0; i < n; i ++)
            scanf("%d%d%d", x + i, y + i, r + i);
        double ans;
        if (n == 1)
            ans = r[0];
        if (n == 2)
            ans = max (r[0], r[1]);
        if (n == 3)
            ans = min3 ( max(cover(0, 1) , r[2]), max(cover(0, 2) , r[1]), max(cover(1, 2) , r[0]));
        printf("Case #%d: %.10lf\n",++ct, ans);
    }
    
    return 0;
}
