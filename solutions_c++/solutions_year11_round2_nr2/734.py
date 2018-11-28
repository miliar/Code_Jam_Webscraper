#include <iostream>
#include <cmath>
using namespace std;
const int N = 1000;
const double MAXN = 1e8;
const double EPS = 1e-8;
double x[N], tmp[N];
int main()
{
    int n, t;
    int c, v;
    double d, p;
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("ronaflx", "w", stdout);
    scanf("%d", &t);
    for(int k = 1;k <= t;k++)
    {
        scanf("%d%lf", &c, &d);
        n = 0;
        while(c--)
        {
            scanf("%lf%d", &p, &v);
            for(int i = n;i < n + v;i++)
                x[i] = p;
            n += v;
        }
        double low = 0, high = MAXN, reach;
        while(fabs(low - high) > EPS)
        {
            double mid = (low + high) / 2;
            tmp[0] = x[0] - mid;
            bool flag = true;
            for(int i = 1;i < n;i++)
            {
                if(tmp[i - 1] + d <= x[i])
                    tmp[i] = max(x[i] - mid, tmp[i - 1] + d);
                else if(tmp[i - 1] + d <= x[i] + mid)
                    tmp[i] = min(tmp[i - 1] + d, x[i] + mid);
                else
                {
                    flag = false;
                    break;
                }
            }
            if(flag) high = mid, reach = mid;
            else low = mid;
        }
        printf("Case #%d: %lf\n", k, reach);
    }
    return 0;
}
