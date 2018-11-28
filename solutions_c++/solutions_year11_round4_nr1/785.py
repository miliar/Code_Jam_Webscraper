#include <stdio.h>
#include <algorithm>
using namespace std;

struct Node {
    int b, e, w;
    Node(){}
    Node(int b, int e, int w):b(b), e(e), w(w){}
    bool operator < (const Node& a) const {
        return b < a.b;
    }
}a[5020];

const double eps = 1e-10;

int sgn(double x) {return (x > eps) - (x < -eps);}

bool cmp(const Node a, const Node b)
{
    if (a.w == b.w) return a.e - a.b > b.e - b.b;
    return a.w < b.w;
}

int main()
{
    int T, x, s, r, n;
    double t;

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%d%d%d%lf%d", &x, &s, &r, &t, &n);
        r -= s;
        for (int i = 0; i < n; ++i) {
            scanf("%d%d%d", &a[i].b, &a[i].e, &a[i].w);
            a[i].w += s;
        }
        sort(a, a + n);

//        for (int i = 0; i < n; ++i) printf("%d %d %d\n", a[i].b, a[i].e, a[i].w);

        int tn = n, pre = 0;
        for (int i = 0; i < n; ++i) {
            if (a[i].b > pre) {
                a[tn++] = Node(pre, a[i].b, s);
            }
            pre = a[i].e;
        }
        if (a[n-1].e < x) a[tn++] = Node(a[n-1].e, x, s);
        n = tn;
        sort(a, a + n, cmp);

//        for (int i = 0; i < n; ++i) printf("%d %d %d\n", a[i].b, a[i].e, a[i].w);

        double ans = 0.0;
        for (int i = 0; i < n; ++i) {
            if (sgn(t) > 0) {
                double tt = (double)(a[i].e - a[i].b) / (a[i].w + r);
                if (tt > t) {
                    ans += t + (a[i].e - a[i].b - t * (a[i].w + r)) / a[i].w;
                    t = 0.0;
                }
                else {
                    t -= tt;
                    ans += tt;
                }
            }
            else ans += (double)(a[i].e - a[i].b) / a[i].w;
        }
        printf("Case #%d: %.9f\n", cas, ans);
    }
    return 0;
}
