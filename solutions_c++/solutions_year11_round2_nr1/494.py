#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>

using namespace std;
int t, n;
char smap[105][105];
double wp[105], owp[105], oowp[105];
double ttmp[105][105];

int main(int argc, char** argv) {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &t);
    for (int v = 1; v <= t; ++v) {
        scanf("%d", &n);
        memset(wp, 0, sizeof (wp));
        memset(owp, 0, sizeof (owp));
        memset(oowp, 0, sizeof (oowp));
        for (int i = 0; i < n; ++i) {
            scanf("%s", smap[i]);
        }
        for (int i = 0; i < n; ++i) {
            int win = 0;
            int cnt = 0;
            for (int j = 0; j < n; ++j) {
                if (smap[i][j] != '.') cnt++;
                if (smap[i][j] == '1') win++;
            }
            wp[i] = 1.0 * win / cnt;
        }
        for (int i = 0; i < n; ++i) {
            int ccnt = 0;
            double tmp = 0.0;
            for (int j = 0; j < n; ++j) {
                if (i == j) continue;
                if (smap[i][j] != '.') {
                    int win = 0, cnt = 0;
                    for (int k = 0; k < n; ++k) {
                        if (k == i) continue;
                        if (smap[j][k] != '.') cnt++;
                        if (smap[j][k] == '1') win++;
                    }
                    tmp += 1.0 * win / cnt;
                    ccnt++;
                }
            }
            owp[i] = 1.0 * tmp / ccnt;
        }
        for (int i = 0; i < n; ++i) {
            int cnt = 0;
            double tmp = 0.0;
            for (int j = 0; j < n; ++j)
                if (smap[i][j] != '.')
                    tmp += owp[j], cnt++;
            oowp[i] = 1.0 * tmp / cnt;
        }
        printf("Case #%d:\n", v);
        for (int i = 0; i < n; ++i) {
            printf("%.12f\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
        }
    }
    return 0;
}

