#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
int n;
double h;
int w,l;
struct Cir
{
    double x,y,r;
    int num;
}c[1021];

int cmp(const struct Cir a,const struct Cir b)
{
    if (a.r < b.r)
        return 0;
    return 1;
}
int cmp2(const struct Cir a,const struct Cir b)
{
    if (a.num < b.num)
        return 1;
    return 0;
}

void putcir(int m)
{
    if (m == 1)
    {
        c[m].x = 0;
        c[m].y = 0;
        h = c[m].y + c[m].r;
        return;
    }
    bool ok = false;
    double x,y;
    x = c[m - 1].x + 2*c[m - 1].r;
    y = c[m - 1].y;
    if (x > w)
    {
        x = 0;
        y = h + c[m].r;
        h = y + c[m].r;
    }
    if (y > l)
        printf("TAT");
    c[m].x = x;
    c[m].y = y;
}

int main()
{
    int T;
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for (int CA = 1; CA <= T; ++CA)
    {
        scanf("%d%d%d",&n,&w,&l);
        for (int i = 1; i <= n; ++i)
            scanf("%lf",&c[i].r),c[i].num = i;
        sort(c + 1,c + n + 1,cmp);
        bool flag = true;
        for (int i = 1; i <= n; ++i)
        {
            putcir(i);
        }
        sort(c + 1,c + n + 1,cmp2);
        printf("Case #%d: ",CA);
        for (int i = 1; i <= n; ++i)
        {
            printf("%.1f %.1f",c[i].x,c[i].y);
            if (i != n)
                printf(" ");
        }

        puts("");
    }
    return 0;
}
