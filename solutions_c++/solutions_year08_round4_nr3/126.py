#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>

using namespace std;

const double lmd = 0.618;
const double eps = 1e-8;
const double inf = 1e100;
const int maxn = 10000;
const int dire[6][3] = {
    {1, 0, 0}, {-1, 0, 0},
    {0, 1, 0}, {0, -1, 0},
    {0, 0, 1}, {0, 0, -1}
};
const int limit = 1000;

double x[maxn], y[maxn], z[maxn], p[maxn];
int n;
double ans;

void Init() {
    int i;
    scanf("%d", &n);
    for (i = 0; i < n; i++)
        scanf("%lf %lf %lf %lf", &x[i], &y[i], &z[i], &p[i]);
}

double Calc(double sx, double sy, double sz, double rr) {
    int i;
    double res = 0;
    for (i = 0; i < n; i++) {
        res = max(res, (fabs(x[i] - sx) + fabs(y[i] - sy) + fabs(z[i] - sz)) / p[i]);
        if (res >= rr) return res + 10;
    }
    return res;
}

void Solve(double sx, double sy, double sz) {
    double delta = 1e6, _x, _y, _z;
    int t, i;
    double res = Calc(sx, sy, sz, inf), temp, xx, yy, zz;
    //printf("res = %lf\n", res);
    for (t = 0; t < limit; t++, delta *= lmd) {
        xx = sx;
        yy = sy;
        zz = sz;
        for (i = 0; i < 6; i++) {
            _x = sx + dire[i][0] * delta;
            _y = sy + dire[i][1] * delta;
            _z = sz + dire[i][2] * delta;
            temp = Calc(_x, _y, _z, res);
            if (temp <= res) {
                res = temp;
                xx = _x;
                yy = _y;
                zz = _z;
            }
        }
        sx = xx;
        sy = yy;
        sz = zz;
    }
    if (res < ans) ans = res;
    //printf("delta = %lf\n", delta);
}

void Work() {
    ans = inf;
    int i;
    double xx, yy, zz;
    for (i = 0; i < limit; i++) {
        xx = rand();
        yy = rand();
        zz = rand();
        Solve(xx, yy, zz);
    }
    printf("%.6lf\n", ans + eps);
}

int main() {
    srand(time(0));
    int t, i;
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
        printf("Case #%d: ", i + 1);
        Init();
        Work();
    }
    return 0;
}
