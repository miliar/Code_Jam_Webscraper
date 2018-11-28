#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

const int MAXN = 1024;
struct SS {int v, len;} a[MAXN];
int X, S, R, n;
double tim;

int cmp(SS a, SS b) {
    double t1 = 1.0 / (a.v + S) - 1.0 / (a.v + R);
    double t2 = 1.0 / (b.v + S) - 1.0 / (b.v + R);
    return t1 > t2;
}

int main() {
    //freopen("a-small-attempt0.in","r",stdin);
    //freopen("a-small-attempt0.out","w",stdout);
    freopen("a-large.in","r",stdin);
    freopen("a-large.out","w",stdout);
    int ca, T, i;
    scanf("%d",&T);
    for (ca = 1 ; ca <= T ; ++ca) {
        scanf("%d%d%d%lf%d",&X,&S,&R,&tim,&n);
        double ans = .0;
        for (i = 0 ; i < n ; i++) {
            int t1, t2;
            scanf("%d%d%d",&t1,&t2,&a[i].v);
            a[i].len = t2 - t1;
            X -= a[i].len;
        }
        if (X) {
            a[n].len = X; a[n].v = 0;
            ++n;
        }

        sort(a, a+n, cmp);
        for (i = 0 ; i < n ; i++) {
            ans += (double)a[i].len / (a[i].v + S);
            //printf("len:%d v:%d\n",a[i].len,a[i].v);
        }
        //printf("ans:%f\n",ans);
        int p = 0;
        while (tim > 0 && p < n) {
            double tmp_t = (double)a[p].len / (a[p].v + R);
            double real_t = min(tmp_t, tim);
            //printf("real_t:%f tmp_t:%f\n",real_t,tmp_t);
            ans -= (1.0 * a[p].len / (a[p].v + S) - 1.0 * a[p].len / (a[p].v + R)) * real_t / tmp_t;
            tim -= real_t;
            ++p;
        }
        printf("Case #%d: %.10lf\n", ca, ans);
    }
    return 0;
}
