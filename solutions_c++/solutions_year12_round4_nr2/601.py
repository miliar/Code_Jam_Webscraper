#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>

#define inf 0x3f3f3f3f
#define Inf 0x3FFFFFFFFFFFFFFFLL
#define maxn 1111
using namespace std;
double const pi = atan2(0, -1.0);
double const eps = 1e-7;
struct node {
    double r;
    int id;
    friend bool operator<(node a, node b) {
        return a.r > b.r;
    }
}p[maxn];

double res[maxn][2];
double ret[maxn][2];

struct lim {
    double h, wl, wr;
    lim(double _h, double _wl, double _wr) { h = _h, wl = _wl, wr = _wr; }
    lim() {}
}ob[maxn][maxn];

struct cir {
    double x, y, r;
} c[maxn];

double sqr(double x1, double x2, double y1, double y2) {
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
}
bool check(int n) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == j) continue;
           // cout << c[i].x << " , " << c[i].y << endl;
           // cout << c[j].x << " , " << c[j].y << endl;
           // cout << sqr(c[i].x, c[j].x, c[i].y, c[j].y) << " : " << c[i].r + c[j].r << endl;
            if (sqr(c[i].x, c[j].x, c[i].y, c[j].y) < c[i].r + c[j].r ) return false;
        }
    }
    return true;
}

int main(){
  //  freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-ans.txt", "w", stdout);
    freopen("B-large.in", "r", stdin);  freopen("B-large-ans.txt", "w", stdout);
    int test_case;
    scanf("%d", &test_case);

    int n; double w, l;
    for(int _t = 1; _t <= test_case; _t++){
        scanf("%d %lf %lf", &n, &w, &l);

double sum = 0;
        for (int i = 0; i < n; ++i) {
            scanf(" %lf", &p[i].r);
            p[i].id = i;

            sum += pi * p[i].r * p[i].r;
        }

        sort(p, p + n);
        int ip = 0, jp = 0;
        double tw, tl;
        double now = 0.0, nl;
        int pc = 0;
        for (int k = 0; k < n; ) {
            tw = tl = p[k].r * 2.0;
         //   printf("k = %d, now = %.2lf\n", k, now);
            if (ip == 0) tl *= 0.5;
            if (jp == 0) tw *= 0.5;

            if (ip == 0) {
                if (tw <= w - now) {
                    res[k][0] = 0;
                    if (jp == 0) {
                        res[k][1] = 0;
                        ob[ip][jp] = lim(tl, 0, tw);
                    }
                    else {
                        res[k][1] = now + tw * 0.5;
                        ob[ip][jp] = lim(tl, now, now + tw);
                    }
                    ++k;
                    ++jp;
                    now += tw;

                }
                else if (tw * 0.5 <= w - now) {
                    res[k][0] = 0;
                    res[k][1] = w;
                    ++k;
                    ob[ip][jp] = lim(tl, now, w);

                    ++ip;
                    jp = 0;
                    pc = 0;
                    now = 0;
                }
                else {
                    ++ip;
                    jp = 0;
                    pc = 0;
                    now = 0;
                }
            }
            else {
                while (now > ob[ip - 1][pc].wr) ++pc;
                nl = ob[ip - 1][pc].h + eps;
                if (tw <= w - now) {
                    res[k][0] = nl + tl * 0.5;
                    if (jp == 0) {
                        res[k][1] = 0;
                        ob[ip][jp] = lim(nl + tl, 0, tw);
                    }
                    else {
                        res[k][1] = now + tw * 0.5;
                        ob[ip][jp] = lim(nl + tl, now, now + tw);
                    }
                    ++k;
                    ++jp;
                    now += tw;
                }
                else if (tw * 0.5 <= w - now) {
                    res[k][0] = nl + tl * 0.5;
                    res[k][1] = w;
                    ++k;
                    ob[ip][jp] = lim(nl + tl, now, w);

                    ++ip;
                    jp = 0;
                    pc = 0;
                    now = 0;
                }
                else {
                    ++ip;
                    jp = 0;
                    pc = 0;
                    now = 0;
                }
            }
        }
        for (int i = 0; i < n; ++i) {
            ret[ p[i].id ][0] = res[i][0];
            ret[ p[i].id ][1] = res[i][1];
        }
        for (int i = 0; i < n; ++i) {
            c[i].x = res[i][0];
            c[i].y = res[i][1];
            c[i].r = p[i].r;
        }
     //   cout << check(n) << endl;
     //   cout << sum * 5  << " < " << w * l << endl;
        printf("Case #%d:", _t);
        for (int i = 0; i < n; ++i) {
            printf(" %.2lf %.2lf", ret[i][1], ret[i][0]);
        }
        puts("");
    }
    return 0;
}
