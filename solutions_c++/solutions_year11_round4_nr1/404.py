#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int maxn = 10000;

struct point{
    int l,r,v;
};

point a[maxn],b[maxn];

int m;

void add(int l,int r,int v){
    b[++m].l = l; b[m].r = r; b[m].v = v;
}

bool cmp1(point i,point j){
    return i.l < j.l;
}

bool cmp2(point i,point j){
    return i.v < j.v;
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int casenum=1; casenum<=T; ++casenum){
        int x,s,r,kk,n;
        scanf("%d %d %d %d %d",&x,&s,&r,&kk,&n);
        double t = kk;
        for (int i=1; i<=n; ++i)
            scanf("%d %d %d",&a[i].l,&a[i].r,&a[i].v);
        m = 0;
        int now = 0;
        sort(a+1,a+n+1,cmp1);
        for (int i=1; i<=n; ++i){
            if (a[i].l > now){
                add(now,a[i].l,s);
                add(a[i].l,a[i].r,a[i].v + s);
                now = a[i].r;
            }
            else {
                add(a[i].l,a[i].r,a[i].v + s);
                now = a[i].r;
            }
        }
        if (now != x)
            add(now,x,s);
        for (int i=1; i<=m; ++i)
            a[i] = b[i];
        sort(a+1,a+m+1,cmp2);
        double total = 0;
        for (int i=1; i<=m; ++i){
            double length = a[i].r - a[i].l,v = a[i].v + r - s;
            double tmp = length / v;
            if (tmp <= t){
                t -= tmp;
                total += tmp;
            } else {
                length = length - t * v;
                total += t;
                t = 0;
                total += length / (a[i].v + 0.0);
            }
        }
        printf("Case #%d: %.10lf\n",casenum,total);
    }
    return 0;
}
