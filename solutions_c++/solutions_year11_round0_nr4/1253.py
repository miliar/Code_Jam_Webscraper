/*
 * Author: Xay
 * Created Time:  2011/5/7 17:27:16
 * File Name: d.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
const int maxn = 10 + 4;

double f[maxn];
int n;
int p[maxn];
int rec[maxn];
int a[maxn];
bool used[maxn];
double jie[maxn];
double com[maxn][maxn];
double c[maxn];

void init() {
    jie[0] = 1;
    for (int i = 1; i < maxn; ++i) {
        jie[i] = jie[i - 1] * i;
    }
    com[0][0] = 1;
    for (int i = 1; i < maxn; ++i) {
        com[i][0] = 1;
        for (int j = 1; j < i; ++j) {
            com[i][j] = com[i - 1][j] + com[i - 1][j - 1];
            //printf("%d %d: %lf\n", i, j, com[i][j]);
        }
        com[i][i] = 1;
    }
    c[0] = 1;
    for (int i = 1; i < maxn; ++i) {
        c[i] = 0;
        for (int j = 0; j <= i; ++j) {
            if (j % 2 == 0) {
                c[i] += com[i][j] * jie[i - j];
            } else {
                c[i] -= com[i][j] * jie[i - j];
            }
        }
        //printf("%d: %lf\n", i, c[i]);
    }
    f[0] = 1;
    f[1] = 0;
    f[2] = 2;
    for (int i = 3; i < maxn; ++i) {
        f[i] = jie[i];
        for (int j = 2; j < i; ++j) {
            f[i] += com[i][j] * c[j] * f[j];
        }
        f[i] /= (jie[i] - c[i]);
        //printf("%d: %lf\n", i, f[i]);
    }
}

void dfs(int x, int &cnt) {
    if (used[x]) return;
    used[x] = true;
    ++cnt;
    dfs(p[x], cnt);
}

bool cmp(int x1, int x2) {
    return a[x1] < a[x2];
}

int main() {
    freopen("d.out", "w", stdout);
    init();
    int t, ca = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", ++ca);
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d", &a[i]);
            p[i] = i;
            used[i] = 0;
            rec[i] = 0;
        }
        rec[n] = 0;
        sort(p, p + n, cmp);
        for (int i = 0; i < n; ++i) {
            if (used[i]) continue;
            int cnt = 0;
            dfs(i, cnt);
            ++rec[cnt];
        }
        double ans = 0;
        for (int i = 2; i <= n; ++i) {
            ans += rec[i] * i;
        }
        printf("%.8lf\n", ans);
    }
    return 0;
}

