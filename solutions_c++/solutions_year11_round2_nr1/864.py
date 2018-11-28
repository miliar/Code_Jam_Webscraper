#include <iostream>
#include <cstdio>
#include <cstring>

#define MAX 210

using namespace std;

const double p[] = {0.25, 0.5, 0.25};
char mat[MAX][MAX];
int w[MAX], s[MAX];
double wp[MAX], owp[MAX], oowp[MAX];

void solve(const int n) {
    int i, j, ts;
    double tmp;

    for (i = 0; i < n; i++) {
        s[i] = w[i] = 0;
        for (j = 0; j< n; j++) {
            if (mat[i][j] != '.') {
                s[i]++;
                if (mat[i][j] == '1') w[i]++;
            }
        }
        wp[i] = (double)w[i] / s[i];
    }
    for (i = 0; i < n; i++) {
        tmp = ts = 0;
        for (j = 0; j < n; j++) {
            if (mat[i][j] != '.') {
                ts++;
                if (mat[i][j] == '0') tmp += (double)(w[j] - 1) / (s[j] - 1);
                else tmp += (double)w[j] / (s[j] - 1);
            }
        }
        owp[i] = tmp / ts;
    }
    for (i = 0; i < n; i++) {
        tmp = ts = 0;
        for (j = 0; j < n; j++) {
            if (mat[i][j] != '.') {
                ts++;
                tmp += owp[j];
            }
        }
        oowp[i] = tmp / ts;
    }
}

int main() {
    int t, cnt = 1, n, i;

    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        for (i = 0; i < n; i++) scanf("%s", mat[i]);
        solve(n);
        printf("Case #%d:\n", cnt++);
        for (i = 0; i < n; i++) {
            printf("%.12lf\n", wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25);
        }
    }

    return 0;
}
