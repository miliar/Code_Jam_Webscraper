#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

struct wl {
    int b, e, w;
    double x;
    bool operator <(const wl it) const {
        return x < it.x;
    }
}wll[2000];

void solve()
{
    int x, s2, r, t2, n;
    scanf("%d %d %d %d %d", &x, &s2, &r, &t2, &n);
    double ans = 0.0;
    
    int sum = 0;
    int b, e, w;
    double t = (double)t2;
    double s = (double)s2;
    
    for (int i = 0; i < n; i++) {
        scanf("%d %d %d", &wll[i].b, &wll[i].e, &wll[i].w);
        wll[i].x = wll[i].w;
        sum += wll[i].e - wll[i].b;
    }
    
    if (t > 0.0) {
        double t1 = (double)(x - sum) / r;
        if (t1 < t) {
            ans += t1;
            t -= t1;
        } else {
            double len = (double)x - sum - r * t;
            ans = ans + t + (double)len / s;
            t = 0.0;
        }
    } else {
        ans = ans + x - sum;
    }
    
    sort(wll, wll + n);
    
    for (int i = 0; i < n; i++) {
        sum = sum + wll[i].e - wll[i].b;
        if (t > 0.0) {
            double t1 = double(wll[i].e - wll[i].b) / (r + wll[i].w);
            if (t1 <= t) {
                ans += t1;
                t -= t1;
            } else {
                double len = wll[i].e - wll[i].b - (r + wll[i].w) * t;
                ans = ans + (double)t + (double)len / (s + wll[i].w);
                t = 0;
            }
        } else {
            ans = ans + (double)(wll[i].e - wll[i].b) / (s + wll[i].w);
        }
    }
   
    printf("%.10lf\n", ans);
}
 
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A.out2", "w", stdout);
    
    int T;
    scanf("%d", &T);
    
    for (int i = 1; i <= T; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
