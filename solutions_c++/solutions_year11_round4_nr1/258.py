#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

struct node
{
       double s, w;
} a[1100];
double t, tt, ans, x;
int T, s, r, n;
double b, e, tmp;

bool cmp(node a, node b)
{
     return a.w < b.w;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        scanf("%lf%d%d%lf%d", &x, &s, &r, &t, &n);
        tmp = ans = 0;
        for (int i = 0; i < n; i++)
        {
            scanf("%lf%lf%lf", &b, &e, &a[i].w);
            a[i].s = e - b;
            tmp += a[i].s;
        }
        a[n].s = x - tmp;
        a[n].w = 0;
        n++;
        sort(a, a + n, cmp);
             
        for (int i = 0; i < n; i++)
        {
            tt = 1.0 * a[i].s / (a[i].w + r);
            x -= a[i].s;
            if (tt <= t)
            {
                   ans += tt;
                   t -= tt;
            }
            else
            {
                a[i].s -= (a[i].w + r) * t;
                ans += t;
                ans += 1.0 * a[i].s / (a[i].w + s);
                t = 0;
            }
        }
        printf("Case #%d: %lf\n", cas, ans);
    }
    return 0;
}
        
                
            
            
