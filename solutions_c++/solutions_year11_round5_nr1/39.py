#include <cstdio>
#include <cstring>
#include <cmath>

#define EPS 1e-10

int     W, L, U, G;
int     n;

struct Point
{
    double x, y;
};
Point   low[120];
Point   upp[120];
Point   list[240];

void init()
{
    scanf("%d%d%d%d", &W, &L, &U, &G);
    for (int i = 0; i < L; i ++)
        scanf("%lf%lf", &low[i].x, &low[i].y);
    
    for (int i = 0; i < U; i ++)
        scanf("%lf%lf", &upp[i].x, &upp[i].y);

    n = 0;
    for (int i = 0; i < L; i ++)
        list[n ++] = low[i];
    for (int i = U - 1; i >= 0; i --)
        list[n ++] = upp[i];
    list[n] = list[0];
}

double getArea(double v)
{
    double area = 0;
    for (int i = 0; i + 1 <= n; i ++)
    {
        if (list[i + 1].x + EPS >= v)
        {
            double y1 = list[i].y + (v - list[i].x) / (list[i+1].x - list[i].x) * (list[i+1].y - list[i].y);
            for (int j = L; j < n; j ++)
            {
                if (list[j + 1].x <= v)
                {
                    double y2 = list[j].y + (v - list[j].x) / (list[j+1].x - list[j].x) * (list[j+1].y - list[j].y);
                    area += list[i].x * y1 - list[i].y * v;
                    area += v * y2 - y1 * v;
                    area += v * list[j+1].y - y2 * list[j+1].x;
                    i = j;
                    break;
                }
            }
        }
        else
        {
            area += list[i].x * list[i + 1].y - list[i].y * list[i + 1].x;
        }
    }
    return area;
}

void solve()
{
    double prev = 0;

    double area = getArea(W);

    for (int part = 1; part < G; part ++)
    {
        double low = prev;
        double upp = W;
        double mid;
        double target = area / G * part;
        
        while ( (upp - low) >= 1e-10 )
        {
            mid = (low + upp) / 2.0;
            double tmp = getArea(mid);
            if (tmp < target) low = mid;
            else upp = mid;
        }
        prev = (low + upp) / 2.0;
        printf("%.10lf\n", prev);
    }
}

int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small.out", "w", stdout);

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t ++)
    {
        printf("Case #%d:\n", t);

        init();
        solve();
    }

    return 0;
}