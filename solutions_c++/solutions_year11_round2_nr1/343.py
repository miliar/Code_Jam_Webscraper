#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define N 105

int n;
char s[N][N];
double wp[N], owp[N], oowp[N];

double cal_wp(int i, int k) {
    double p = 0, q = 0;
    for (int j = 0; j < n; ++j) if (j != k) {
        p += s[i][j] == '1';
        q += s[i][j] != '.';
    }
    return p / q;
}

void solve() {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
        scanf("%s", s[i]);
    for (int i = 0; i < n; ++i)
        wp[i] = cal_wp(i, -1);
    for (int i = 0; i < n; ++i) {
        int cnt = 0;
        double ss = 0;
        for (int j = 0; j < n; ++j) if (s[i][j] != '.') {
            ++cnt;
            ss += cal_wp(j, i);
        }
        owp[i] = ss/cnt;
    }
    for (int i = 0; i < n; ++i) {
        int cnt = 0;
        double ss = 0;
        for (int j = 0; j < n; ++j) if (s[i][j] != '.') {
            ++cnt;
            ss += owp[j];
        }
        oowp[i] = ss/cnt;
    }
    for (int i = 0; i < n; ++i)
        printf("%.8lf\n", 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d:\n", ++cas);
        solve();
    }
    return 0;
}
