#include <stdio.h>
#include <math.h>

#define eps 1e-8

const int maxn = 10;

double x[maxn], y[maxn], r[maxn];
int b[maxn], C, N;
double r_r;

double sqr(double x)
{
    return x * x;
}

double dis(int a, int b)
{
    return sqrt(sqr(x[a]-x[b]) + sqr(y[a]-y[b]));
}

double max(double x, double y)
{
    return x > y ? x : y;
}

int main(void)
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    
    scanf("%d", &C);
    for (int cas = 1; cas <= C; ++cas) {
        scanf("%d", &N);
        for (int i = 0; i < N; ++i) {
            scanf("%lf %lf %lf", &x[i], &y[i], &r[i]);
            b[i] = 0;
        }
        
        for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j) if (i != j) {
            double d = dis(i, j);
            if (d+r[j]<r[i] || fabs(d+r[j]-r[i])<eps) b[j] = 1;
        }
        
        int n = 0;
        for (int i = 0; i < N; ++i)
            if (!b[i]) {
                x[n] = x[i];
                y[n] = y[i];
                r[n] = r[i];
                ++n;
            }

        if (n == 1) r_r = 2*r[0];
        else if (n == 2) r_r = max(2*r[0], 2*r[1]);
        else {
            r_r = r[2];
            r_r = max(r_r, dis(0, 1)+r[0]+r[1]);
            
            double r_;
            r_ = r[1];
            r_ = max(r_, dis(0, 2)+r[0]+r[2]);
            
            if (r_ < r_r) r_r = r_;
            
            r_ = r[0];
            r_ = max(r_, dis(1, 2)+r[1]+r[2]);
            
            if (r_ < r_r) r_r = r_;
        }
        printf("Case #%d: %.6lf\n", cas, r_r/2);
    }
    return 0;
}
