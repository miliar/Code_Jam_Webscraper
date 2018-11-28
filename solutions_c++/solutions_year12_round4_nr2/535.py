#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <ctime>
#define eps 1e-10
using namespace std;
double fabs(double x)
{
    return (x > 0) ? x : -x;
}
int dblcmp(double d)
{
    if (fabs(d) < eps) return 0;
    else if (d > 0) return 1;
    else return -1;
    return (d > 0)?1:-1;
}
int n, m, T;
double r[2000];
struct point
{
    double x, y;
}p[2000];
double w, l;
double getR()
{
       double ret = 0;
       for (int i = 0; i < 10; ++i)
           ret = ret / 10.0 + double(rand() % 10);
       return ret / 10.0;
}
void shuffle()
{
     for (int i = 0; i < n; ++i)
     {
         p[i].x = getR() * w;
         p[i].y = getR() * l;
     }
}
double sqr(double x)
{
    return x * x;
}
bool check()
{
     for (int i = 0; i < n; ++i)
         for (int j = i + 1; j < n; ++j)
             if (dblcmp(sqr(p[i].x - p[j].x) + sqr(p[i].y - p[j].y) - sqr(r[i] + r[j])) <= 0) return false;
     return true;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    srand(time(0));
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca)
    {
        scanf("%d%lf%lf", &n, &w, &l);
        for (int i = 0; i < n; ++i)
            scanf("%lf", &r[i]);
        do
        {
            shuffle();
        }  while (!check());
        printf("Case #%d:", ca);
        for (int i = 0; i < n; ++i)
            printf(" %.5f %.5f", p[i].x, p[i].y);
        printf("\n");
    }
    return 0;
}

