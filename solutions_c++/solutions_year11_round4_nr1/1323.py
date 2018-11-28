#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <functional>
#include <utility>

using namespace std;

int dir4[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
int dir8[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}};

struct NN {
    int b, e, w;
};

NN ss[1010];
int X, S, R, t, n;

bool cmp(const NN &cmp1, const NN &cmp2)
{
    return cmp1.w > cmp2.w;
}

const double E = 1e-12;

int dblcmp(double x)
{
    if (x > -E && x < E)
        return 0;
    return x > 0 ? 1 :-1;
}

bool solve(double t1, double t2)
{
    double l1 = t1 * R, l2 = t2 * S;
    if (dblcmp(X - l1 - l2) <= 0)
        return true;
    double ans = 0;
    for (int i = 1; i <= n; i++) {
        if (dblcmp(t2) > 0) {
            double tmp = (double)(ss[i].e - ss[i].b) / (S + ss[i].w);
            if (dblcmp(tmp - t2) <= 0) {
                t2 -= tmp;
                ans += (double)(ss[i].e - ss[i].b);
            } else {
                double di = ((double)ss[i].e - ss[i].b) - (double)(S + ss[i].w) * t2;
                ans += (double)(S + ss[i].w) * t2;
                t2 = 0;
                tmp = di / (R + ss[i].w);

                if (dblcmp(tmp - t1) <= 0) {
                    t1 -= tmp;
                    ans += di;
                } else {
                    ans += (double)(R + ss[i].w) * t1;
                    t1 = 0;
                }
            }
        } else if (dblcmp(t1) > 0) {
            double tmp = (double)(ss[i].e - ss[i].b) / (R + ss[i].w);
            if (dblcmp(tmp - t1) <= 0) {
                t1 -= tmp;
                ans += (ss[i].e - ss[i].b);
            } else {
                ans += (double)(R + ss[i].w) * t1;
                t1 = 0;
            }
        }
    }
    ans += (t1 * R + t2 * S);
    if (dblcmp(X - ans) <= 0)
        return true;
    else
        return false;
}

int main()
{
    int cn, cns;

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    scanf("%d", &cns);
    for (cn = 0; cn < cns; cn++) {
        scanf("%d%d%d%d%d", &X, &S, &R, &t, &n);
        for (int i = 1; i <= n; i++) {
            scanf("%d%d%d", &ss[i].b, &ss[i].e, &ss[i].w);
        }
        sort(ss + 1, ss + n + 1, cmp);
        double l = 0, r = 1e7;
        while (r - l > 1e-8) {
            double m = (l + r) / 2;
            double t1 = min((double)t, m);
            double t2 = m - t1;
           /* if (dblcmp(m - 3) <= 0) {
                m = m;
            }*/
            if (solve(t1, t2)) {
                r = m;
            } else {
                l = m;
            }
        }
        printf("Case #%d: %.10lf\n", cn + 1, r);
    }
    return 0;
}
