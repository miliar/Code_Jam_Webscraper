#include <cstdio>
#include <string>
#include <cmath>
using namespace std;

const double eps = 1e-9;
const int MAXN = 218;
struct Pt {double x, y;} pt[2][MAXN];
int L, U, W, G;
int len[2];

double findy(double x, int idx) {
    if (fabs(x - W) < eps) return pt[idx][len[idx]-1].y;
    int i;
    for (i = 0 ; i < len[idx] - 1 ; ++i) {
        if (x >= pt[idx][i].x && x < pt[idx][i+1].x)
            break;
    }
    return pt[idx][i].y + (x - pt[idx][i].x) * (pt[idx][i+1].y - pt[idx][i].y) / (pt[idx][i+1].x - pt[idx][i].x);
}

double calc_s(double x, int idx) {
    double ans = .0;
    int i;
    for (i = 0 ; i < len[idx] - 1 ; i++) {
        if (x >= pt[idx][i+1].x) {
            ans += (pt[idx][i].y + pt[idx][i+1].y) * (pt[idx][i+1].x - pt[idx][i].x) / 2.0;
        } else break;
    }
    double dy = findy(x, idx);
    ans += (pt[idx][i].y + dy) * (x - pt[idx][i].x) / 2.0;
    return ans;
}

double calc_x(double area) {
    double lo, hi, mid;
    int cnt = 0;
    lo = 0; hi = W;
    while (hi - lo > eps && cnt < 100) {
        ++cnt;
        mid = (hi + lo) / 2;
        double s = calc_s(mid, 1) - calc_s(mid, 0);
        if (s <= area) lo = mid;
        else hi = mid;
    }
    return (hi + lo) / 2;
}

int main() {
    // freopen("a-small-attempt0.in","r",stdin);
    // freopen("a-small-attempt0.out","w",stdout);
        freopen("a-large.in","r",stdin);
    freopen("a-large.out","w",stdout);

    int T, ca, i;
    scanf("%d",&T);
    for (ca = 1 ; ca <= T ; ++ca) {
        scanf("%d%d%d%d",&W,&L,&U,&G);
        len[0] = L; len[1] = U;
        for (i = 0 ; i < L ; i++)
            scanf("%lf%lf",&pt[0][i].x,&pt[0][i].y);
        for (i = 0 ; i < U ; i++)
            scanf("%lf%lf",&pt[1][i].x,&pt[1][i].y);
        double tot = calc_s(W, 1) - calc_s(W, 0);
        //printf("tot:%f (%f-%f)\n",tot,calc_s(W,1),calc_s(W,0));
        printf("Case #%d:\n",ca);
        for (i = 1 ; i < G ; i++) {
            double ans = calc_x(tot / G * i);
            printf("%.10lf\n", ans);
            //printf("rea: %lf - %lf = %lf\n", calc_s(ans,1), calc_s(ans, 0), calc_s(ans,1)-calc_s(ans,0));
        }
    }
    return 0;
}
/*
2
15 3 3 3
0 6
10 8
15 9
0 10
5 11
15 13
8 3 4 2
0 2
5 4
8 3
0 5
3 4
4 7
8 5
*/
