#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#define max(x,y) ((x)>(y)?(x):(y))
#define min(x,y) ((x)<(y)?(x):(y))

double x, s, r, t;int n;

struct Type {

    Type() {
    }

    void setType(double x, double y, double z) {
        b = x, e = y, w = z;
    }
    double b, e, w;
} con[3001];int N;

int cmp(const void *a, const void *b) {
    return ((Type*) a)->b < ((Type*) b)->b ? -1 : 1;
}

int wcmp(const void *a, const void *b) {
    return ((Type*) a)->w < ((Type*) b)->w ? -1 : 1;
}

int main() {
    freopen("D:\\A-large.in","r",stdin);
    freopen("D:\\A-large.out","w",stdout);
    int tt, c, i;
    scanf("%d", &tt);
    for (c = 1; c <= tt; c++) {
        scanf("%lf%lf%lf%lf%d", &x, &s, &r, &t, &n);
        for (i = 0; i < n; i++) {
            scanf("%lf%lf%lf", &con[i].b, &con[i].e, &con[i].w);
        }
        qsort(con, n, sizeof (Type), cmp);
        Type pre;
        pre.setType(0,0,0);
        N=n;
        for (i=0;i<n;i++) {
            if (pre.e<con[i].b) {
                con[N++].setType(pre.e,con[i].b,0);
            }
            pre=con[i];
        }
        if (pre.e<x)
            con[N++].setType(pre.e,x,0);
        qsort(con,N,sizeof(Type),wcmp);
        double ans=0;
        for (i=0;i<N;i++) {
            if (t>0) {
                if (t*(con[i].w+r)>=(con[i].e-con[i].b)) {
                    t-=(con[i].e-con[i].b)/(con[i].w+r);
                    ans+=(con[i].e-con[i].b)/(con[i].w+r);
                } else {
                    ans+=t;
                    ans+=((con[i].e-con[i].b)-(con[i].w+r)*t)/(con[i].w+s);
                    t=0;
                }
            } else {
                ans+=(con[i].e-con[i].b)/(con[i].w+s);
            }
        }
        printf("Case #%d: %.7lf\n",c,ans);
    }
    return 0;
}