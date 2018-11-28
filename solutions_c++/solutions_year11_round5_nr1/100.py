#include <stdio.h>
struct abc{
    double x, y;
}l[110], u[110];
int ln, un;
double pd(abc c[], int n, double x){
    int i;
    double s = 0;
    for (i = 1; i < n - 1 && c[i].x < x - 1e-8; i++){
        s += (c[i].y + c[i - 1].y) * (c[i].x - c[i - 1].x) / 2;
    }
    double y = (c[i].y - c[i - 1].y) / (c[i].x - c[i - 1].x) * (x - c[i - 1].x) + c[i - 1].y;
    s += (y + c[i - 1].y) * (x - c[i - 1].x) / 2;
    return s;
}
double f(double x){
    return pd(u, un, x) - pd(l, ln, x);
}
double ef(double l, double r, double s){
    double z = (l + r) / 2;
    if (r - l < 1e-8){
        return l;
    }
    if (f(z) < s){
        return ef(z, r, s);
    }
    return ef(l, z, s);
}
int main(){
    int ri = 1, T, i, w, g;
    double s;
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d%d%d%d", &w, &ln, &un, &g);
        for (i = 0; i < ln; i++){
            scanf("%lf%lf", &l[i].x, &l[i].y);
        }
        for (i = 0; i < un; i++){
            scanf("%lf%lf", &u[i].x, &u[i].y);
        }
        s = f(w);
        printf("Case #%d:\n", ri++);
        for (i = 1; i < g; i++){
            printf("%.8f\n", ef(0, w, s / g * i));
        }
    }
    return 0;
}
