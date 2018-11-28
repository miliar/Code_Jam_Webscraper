#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

int sign(double x)
{
    if (fabs(x) < 1e-8) return 0;
    if (x < 0) return -1;
    return 1;
}
struct node {
    double x, y;
    node() {}
    node(double a, double b) : x(a), y(b) {}
};
node aa[105], bb[105];
int W, L, U, G;
double getyy(node a, node b, double x)
{
    double k = (b.y - a.y) / (b.x - a.x);
    return k * (x - a.x) + a.y;
}
double getit(double x)
{
    int a = 0, b = 0;
    double len = bb[0].y - aa[0].y;
    double res = 0;
    double xx = 0;
    double pre = 0;
    while (sign(xx - x) < 0) {
        pre = xx;
        xx = x;
        if (a < L - 1) xx = min(xx, aa[a + 1].x);
        if (b < U - 1) xx = min(xx, bb[b + 1].x);
        if (a < L - 1 && sign(xx - aa[a + 1].x) >= 0) a++;
        if (b < U - 1 && sign(xx - bb[b + 1].x) >= 0) b++;
        double now = 0;
        if (sign(xx - aa[L - 1].x) == 0) {
            now = bb[U - 1].y - aa[L - 1].y;
        } else {
            now = getyy(bb[b], bb[b + 1], xx) - getyy(aa[a], aa[a + 1], xx);
        }
        res += (len + now) * (xx - pre) / 2.0;
        len = now;
    }
    return res;
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%d%d%d%d", &W, &L, &U, &G);
        for (int i = 0; i < L; ++i)
            scanf("%lf%lf", &aa[i].x, &aa[i].y);
        for (int i = 0; i < U; ++i)
            scanf("%lf%lf", &bb[i].x, &bb[i].y);
        printf("Case #%d:\n", ca);
        double tt = getit(aa[L - 1].x);
        for (int i = 1; i < G; ++i) {
            double l = aa[0].x, r = aa[L - 1].x;
            double now = i * tt / G;
            while (r - l > 1e-8) {
                double mid = (l + r) / 2.0;
                double t = getit(mid);
                if (t > now) r = mid;
                else l = mid;
            }
            printf("%lf\n", l);
        }
    }
    return 0;
}
