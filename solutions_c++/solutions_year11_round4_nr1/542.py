#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 3000;
const double eps = 1e-8;

int T, b, e, w;
double S, R, X, t;
int N;

struct TData {
   int l, w;
   int b, e;
};

TData seg[MAXN];
int tot;

int cmp (const TData a, const TData b)
{
    return a.w < b.w;
}

int main ()
{
    //freopen ("in.txt", "r", stdin);

    scanf ("%d", &T);

    for (int i = 1; i <= T; i++) {
        scanf ("%lf%lf%lf%lf%d", &X, &S, &R, &t, &N);

        int last = 0;

        tot = 0;

        for (int j = 0; j < N; j++) {
            scanf ("%d%d%d", &b, &e, &w);

            seg[tot].b = last;
            seg[tot].e = b;
            seg[tot].l = b - last;
            seg[tot].w = 0;
            tot ++;

            seg[tot].b = b;
            seg[tot].e = e;
            seg[tot].l = e - b;
            seg[tot].w = w;
            tot ++;

            last = e;
        }

        seg[tot].b = last;
        seg[tot].e = X;
        seg[tot].l = X - last;
        seg[tot].w = 0;
        tot ++;

        sort (seg, seg + tot, cmp);

        double ans = 0, tmp;
        for (int j = 0; j < tot; j++)
        {
            if (seg[j].l == 0) continue;

            //printf ("%d %d %d     ", seg[j].b, seg[j].e, seg[j].l);
            tmp = seg[j].l * 1.0 / (seg[j].w + R);

            //printf ("%.2f\n", tmp);
            if (tmp - eps > t) {
                ans += t + (seg[j].l - (seg[j].w + R) * t) / (seg[j].w + S);
                t = 0;
            } else {
                ans += tmp;
                t -= tmp;
            }
        }

        printf ("Case #%d: %.9f\n", i, ans);
    }
}

