#include <cstdio>
#include <algorithm>
using namespace std;


struct L {
    long long b, e, l, w;
};

bool cmp1(const L& a, const L& b) {
    return a.b < b.b;
}

bool cmp2(const L& a, const L& b) {
    return a.w < b.w;
}

int te, Te;
long long x, s, r, t, n, last, walklen, thisl;
long double total, thisT, leftT;
L l[2000];

int main() {
    scanf("%d", &Te);
    for (int te = 1; te <= Te; te++) {
        scanf("%lld%lld%lld%lld%lld", &x, &s, &r, &t, &n);
        for (int i = 0; i < n; i++) {
            scanf("%lld%lld%lld", &l[i].b, &l[i].e, &l[i].w);
            l[i].l = l[i].e - l[i].b;
        }
        sort(l, l + n, cmp1);
        total = 0;
        last = 0;
        walklen = 0;
        for (int i = 0; i < n; i++) {
            thisl = l[i].b - last;
            if (thisl != 0) {
                walklen += thisl;
                total += thisl * 1.0 / s;
            }
            total += l[i].l * 1.0 / (s + l[i].w);
            last = l[i].e;
            //printf(" +%d: %Lf\n", i, total);
        }
        thisl = x - last;
        walklen += thisl;
        if (thisl != 0)
            total += thisl * 1.0 / s;

        //printf("%Lf\n", total);
        if (walklen != 0) {
            l[n].w = 0;
            l[n].l = walklen;
            n++;
        }
        sort(l, l + n, cmp2);
        leftT = t;
        for (int i = 0; i < n; i++) {
            if (leftT <= 0)
                break;
            thisT = l[i].l * 1.0 / (r + l[i].w);
            //printf("%Lf\n", thisT);
            if (thisT > leftT)
                thisT = leftT;
            total -= thisT * 1.0 * (r + l[i].w) / (s + l[i].w) - thisT;
            leftT -= thisT;
            //printf(" -%d: %Lf\n", i, total);
        }
        printf("Case #%d: %.20Lf\n", te, total);
    }
}
