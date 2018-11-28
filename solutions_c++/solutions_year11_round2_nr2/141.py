#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <string.h>
#include <vector>

using namespace std;

const double eps = 1e-9;
const double inf = 1e18;
const int maxop = 300;

double x[2000000], l[2000000], r[2000000];

inline bool ls(double a, double b){
    return (b - a >= eps);
}

inline void solve(int t){
    int n;
    double d;
    scanf("%d %lf", &n, &d);
    int m = 0;
    for(int i = 0; i < n; i++){
        double cx;
        int sz;
        scanf("%lf %d", &cx, &sz);
        for(int j = 0; j < sz; j++){
            x[m++] = cx;
        }
    }
    sort(x, x + m);
    double ans = inf;
    double ll = 0;
    double rr = inf;
    for(int op = 0; op < maxop; op++){
        double mid = (ll + rr) / 2;
        for(int i = 0; i < m; i++){
            l[i] = x[i] - mid;
            r[i] = x[i] + mid;
        }
        double g = -2 * inf;
        bool fl = true;
        for(int i = 0; i < m; i++){
            double pos = max(g, l[i]);
            if(ls(r[i], pos)){
                fl = false;
                break;
            }
            g = pos + d;
        }
        if(fl){
            ans = mid;
            rr = mid;
        }
        else{
            ll = mid;
        }
    }
    printf("Case #%d: %.18lf\n", t, ans);
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++){
        solve(i);
    }
    return 0;
}
