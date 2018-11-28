#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

struct Point
{
    double x, y;
};

Point p[3];
double R[3];

double dis(double x, double y)
{
    return sqrt(x * x + y * y);
}

double gao(int a, int b)
{
    return (dis(p[a].x - p[b].x, p[a].y - p[b].y) + R[a] + R[b]) / 2;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%lf%lf%lf", &p[i].x, &p[i].y, &R[i]);
        double res = 1e10;
        if (n == 1)
        {
            res = R[0];
        } else if (n == 2)
        {
            res = min(R[0], R[1]);
        } else
        {
            double curr = max(gao(0, 1), R[2]);
            if (curr < res)
                res = curr;
            curr = max(gao(0, 2), R[1]);
            if (curr < res)
                res = curr;
            curr = max(gao(1, 2), R[0]);
            if (curr < res)
                res = curr;
        }
        printf("Case #%d: %.13lf\n", cas, res);
    }
    return 0;
}
