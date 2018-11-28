#include <iostream>
#include <cmath>
using namespace std;

double x[4], y[4], r[4];
int n, task, tt;

inline double sqr(double x)
{
       return x * x;
}

inline double dis(int i, int j)
{
       return sqrt(sqr(x[i] - x[j]) + sqr(y[i] - y[j]));
}

int main()
{
    freopen("d1.in", "r", stdin);
    freopen("d1.out", "w", stdout);
    scanf("%d", &task); int i, j, k, t;
    double ans, tmp;
    for (tt = 1; tt <= task; ++tt) {
        scanf("%d", &n);
        for (i = 0; i < n; ++i) {
            scanf("%lf%lf%lf", &x[i], &y[i], &r[i]);
        }
        ans = 1e10; printf("Case #%d: ", tt);
        if (n == 1) {printf("%.5lf\n", r[0]);}
        if (n == 2) {
           if (r[0] > r[1]) printf("%.5lf\n", r[0]);
           else printf("%.5lf\n", r[1]);
        }
        if (n == 3) {
           for (i = 0; i < n; ++i) {
               k = (i + 1) % 3; t = (i + 2) % 3;
               tmp = (dis(k, t) + r[k] + r[t]) / 2;
               if (r[i] > tmp) tmp = r[i];
               if (ans > tmp) ans = tmp;
           }
           printf("%.5lf\n", ans);
        }
    }
    return 0;
}
