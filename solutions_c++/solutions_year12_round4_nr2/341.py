#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

double x[1024], y[1024];
double r[1024];

int w,l,n;


__always_inline double dist(int i, int j) {
    return sqrt(
            (x[i]-x[j])*(x[i]-x[j])+
            (y[i]-y[j])*(y[i]-y[j]));

}

void random_put(int i) {
    x[i] = w * (double)(random()) / RAND_MAX;
    y[i] = l * (double)(random()) / RAND_MAX;

    // if (x[i] > w || x[i] < 0 || y[i] > l || y[i] < 0) {
    //     printf("\nERR1: %g %g\n", x[i], y[i]);
    //     exit(2);
    // }

}

int gao() {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (j == i) continue;
            // move j from i
            double d=dist(i,j);
            double rr=r[i]+r[j];
            if (d < rr+1e-4) {
                // move (i, j)
                double dx = x[j] - x[i];
                double dy = y[j] - y[i];
                double dr = sqrt(dx * dx + dy * dy);
                if (dr < 1e-4) {
                    random_put(j);
                    break;
                }
                // norm
                dx/=dr;
                dy/=dr;
                double nx = x[j] + dx * (rr+1e-5);
                double ny = y[j] + dy * (rr+1e-5);

                if (nx <= 0 || nx > w || ny <= 0 || ny > l) {
                    random_put(j);
                } else {
                    x[j] = nx;
                    y[j] = ny;
                    // if (x[j] > w || x[j] < 0 || y[j] > l || y[j] < 0) {
                    //     printf("\nERR2: %g %g\n", x[j], y[j]);
                    //     exit(2);
                    // }
                }
            }
        }
    }

    // check
    for (int i = 0; i < n; ++i) {
        // if (x[i] > w || x[i] < 0 || y[i] > l || y[i] < 0) {
        //     printf("\nERR: %g %g\n", x[i], y[i]);
        //     exit(2);
        //     return 0;
        // }
        for (int j = i+1; j < n; ++j) {
            double d=dist(i,j);
            double rr=r[i]+r[j];
            if (d < rr+1e-4) {
                return 0;
            }
        }
    }
    return 1;
}

int main(int argc, char const *argv[]) {
    int T;
    scanf("%d", &T);
    for (int ti = 0; ti < T; ++ti) {
        printf("Case #%d:", ti+1 );
        scanf("%d%d%d", &n, &w, &l);

        memset(x, 0, sizeof(x));
        memset(y, 0, sizeof(y));

        for (int i=0;i<n;i++) {
            scanf("%lf", r+i);
        }

        // gao
        while(gao()==0);
        for (int i = 0; i <n;i++) {
            printf(" %.12g %.12g", x[i], y[i]);
        }
        printf("\n");
    }
    return 0;
}
