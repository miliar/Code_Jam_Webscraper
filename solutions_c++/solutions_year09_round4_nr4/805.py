#include<stdio.h>
#include<math.h>

struct cir{ double x, y, r; }a[50];
int C, N, i, j, k, cas;
double t1, t2, ans;

inline double mymin(double v1, double v2){ return (v1)>(v2)?(v2):(v1); }
inline double mymax(double v1, double v2){ return (v1)>(v2)?(v1):(v2); }
double findr(cir c1, cir c2)
{
    double ret = sqrt((c1.x - c2.x)*(c1.x - c2.x)+(c1.y - c2.y)*(c1.y - c2.y));
    ret = ret + c1.r + c2.r;
    return ret/2.0;
}
int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    scanf("%d", &C);
    for (cas = 1; cas <= C; cas++){
        scanf("%d", &N);
        for (i=0;i<N;i++)
            scanf("%lf%lf%lf", &a[i].x, &a[i].y, &a[i].r);
        if (N == 1) ans = a[0].r;else
        if (N == 2) ans = mymax(a[0].r, a[1].r);else
        if (N == 3){
              ans = mymax(a[0].r, findr(a[1], a[2]));
              ans = mymin(ans, mymax(a[1].r, findr(a[0], a[2])));
              ans = mymin(ans, mymax(a[2].r, findr(a[0], a[1])));
        }
        printf("Case #%d: %.6lf\n", cas, ans);
    }
    return 0;
}
