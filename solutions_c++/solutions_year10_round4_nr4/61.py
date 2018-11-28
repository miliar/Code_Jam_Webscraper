#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

const double Eps = 1E-8;
const double Pi = acos(-1.0);
const int maxn = 30;
const int maxr = 100;

#define sqr(a) ((a) * (a))
#define dist(a, b) (sqrt(sqr((a)[0] - (b)[0]) + sqr((a)[1] - (b)[1])))
#define Equal(a, b) (fabs((a) - (b)) < Eps)

struct Tcir {
    double x, y, r;

    Tcir() {}
    Tcir(double x, double y, double r): x(x), y(y), r(r) {}
} allcir[maxn];
struct Tinterval {
    double y1, y2, Height, Area;
    int flag;

    Tinterval() {}
    Tinterval(double y1, double y2, double Height, double Area, int flag): y1(y1), y2(y2), Height(Height), Area(Area), flag(flag) {}
    bool operator< (const Tinterval& a) const {
        return Height > a.Height;
    }
} allseg[maxn];
double allcut[maxr];
double allpoints[maxn][2];
int N, n;
double ret;

void addcir(double* pa, double* pb) {
    double lenres = dist(pa, pb);
    allcir[N ++] = Tcir(pa[0], pa[1], lenres);
}
void addpoints(double x) {
    allcut[n ++] = x;
}
void cross_circle(const Tcir& a, const Tcir& b) {
    double lenres = sqr(a.x - b.x) + sqr(a.y - b.y);
    if(lenres > sqr(a.r + b.r) - Eps || lenres < sqr(a.r - b.r) + Eps)
        return;
    double u = ((sqr(a.r) - sqr(b.r)) / lenres + 1) / 2;
    double v = sqrt((sqr(a.r) - sqr(u) * lenres) / lenres);
    double x = b.x - a.x;
    double y = b.y - a.y;
    double x1 = a.x + x * u - y * v, y1 = a.y + y * u + x * v;
    double x2 = a.x + x * u + y * v, y2 = a.y + y * u - x * v;
    addpoints(x1);
    addpoints(x2);
}
void Check(double f, double r) {
    double a1, a2, a3, y1, y2, y3, D, lenres, theta, cnt;
    int i, t, Count;

    for(i = t = 0; i < N; i ++)
        if(allcir[i].x - allcir[i].r - Eps < f && allcir[i].x + allcir[i].r + Eps > r) {
            a1 = sqrt(fabs(sqr(allcir[i].r) - sqr(f - allcir[i].x)));
            a2 = sqrt(fabs(sqr(allcir[i].r) - sqr(r - allcir[i].x)));
            a3 = sqrt(fabs(sqr(allcir[i].r) - sqr((f + r) / 2 - allcir[i].x)));
            y1 = allcir[i].y - a1;
            y2 = allcir[i].y - a2;
            y3 = allcir[i].y - a3;
            D = sqr(f - r) + sqr(y1 - y2);
            lenres = sqr(allcir[i].r) - D / 4;
            theta = atan(sqrt(D / lenres) / 2) * 2;
            cnt = sqr(allcir[i].r) * theta / 2 - sqr(allcir[i].r) * sin(theta) / 2;
            allseg[t ++] = Tinterval(y1, y2, y3, cnt, -1);
            y1 = allcir[i].y + a1;
            y2 = allcir[i].y + a2;
            y3 = allcir[i].y + a3;
            allseg[t ++] = Tinterval(y1, y2, y3, cnt, 1);
        }
    sort(allseg, allseg + t);
    for(i = Count = 0; i + 1 < t; i ++) {
        Count += allseg[i].flag;
        if(Count == N)
            ret += allseg[i].flag * allseg[i].Area - allseg[i + 1].flag * allseg[i + 1].Area + (r - f) * (allseg[i].y1 - allseg[i + 1].y1 + allseg[i].y2 - allseg[i + 1].y2) / 2;
    }
}
int main() {
    freopen("D-small-attempt0.in", "r", stdin);
//    freopen("input.txt", "r", stdin);
    int i, j, nn, m, nc, T;
    int test = 1;

    for(scanf("%d", &T); T; T --) {
        scanf("%d%d", &nn, &m);
        for(i = 0; i < nn + m; i ++)
            scanf("%lf%lf", &allpoints[i][0], &allpoints[i][1]);
        printf("Case #%d:", test ++);
        for(int K = 0; K < m; K ++) {
            N = 0;
            n = 0;
            for(i = 0; i < nn; i ++) addcir(allpoints[i], allpoints[nn + K]);
            for(i = 0; i < N; i ++) {
                for(j = i + 1; j < N; j ++)
                    cross_circle(allcir[i], allcir[j]);
                addpoints(allcir[i].x - allcir[i].r);
                addpoints(allcir[i].x);
                addpoints(allcir[i].x + allcir[i].r);
            }
            sort(allcut, allcut + n);
            nc = unique(allcut, allcut + n) - allcut;
            ret = 0;
            for(i = 0; i + 1 < nc; i ++)
                Check(allcut[i], allcut[i + 1]);
            printf(" %.7f", ret);
        }
        printf("\n");
    }
    return 0;
}

