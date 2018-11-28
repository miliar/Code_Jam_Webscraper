/**********************************************************************
Author: WHU_GCC
Created Time: 2008年08月03日 星期日 01时29分41秒
File Name: gcj_c.cpp
Description: 
**********************************************************************/
#include <iostream>
#include <cmath>
using namespace std;
#define out(x) (cout << #x << ": " << x << endl)
const int maxint = 0x7FFFFFFF;
template <class T> void get_max(T &a, const T &b) {b > a ? a = b : 1;}
template <class T> void get_min(T &a, const T &b) {b < a ? a = b : 1;}

int n;
double x[1000], y[1000], z[1000];
int p[1000];

const int rand_times = 10000;

const int dx[] = {-1, 0, 1, 0, 0, 0};
const int dy[] = {0, 1, 0, -1, 0, 0};
const int dz[] = {0, 0, 0, 0, 1, -1};

int main() {
    int ca;
    int T = 1;
    freopen("gcj_c.out", "w", stdout);
    for (scanf("%d", &ca); ca--;) {
        printf("Case #%d: ", T++);
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%lf%lf%lf%d", &x[i], &y[i], &z[i], &p[i]);
        
        double tx, ty, tz;
        double step = 100000;
        double ans = 1e100;
        for (int i = 0; i < rand_times; i++) {
            tx = rand() % 1000000;
            ty = rand() % 1000000;
            tz = rand() % 1000000;
            double cost = 0;
            for (int j = 0; j < n; j++) {
                get_max(cost, (abs(x[j] - tx) + abs(y[j] - ty) + abs(z[j] - tz))/ p[j]);
            }

            while (step > 1e-7) {
//                printf("%lf\n", step);
//                printf("%.2lf %.2lf %.2lf\n", tx, ty, tz);
                int flag = 1;
                for (int k = 0; k < 6 && flag; k++) {
                    double nx = tx + dx[k] * step;
                    double ny = ty + dy[k] * step;
                    double nz = tz + dz[k] * step;
                    double tcost = 0.0;
                    for (int j = 0; j < n; j++) {
                        get_max(tcost, (abs(x[j] - nx) + abs(y[j] - ny) + abs(z[j] - nz))/ p[j]);
                    }
                    if (tcost < cost) {
                        cost = tcost;
                        tx = nx;
                        ty = ny;
                        tz = nz;
                        flag = 0;
                    }
                }
                if (flag)
                    step *= 0.8;
            }
            get_min(ans, cost);
        }
        printf("%.6lf\n", ans);
    }
    return 0;
}

