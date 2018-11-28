#include <stdio.h>
#define MaxN 110

int win[MaxN], cnt[MaxN];
double wp[MaxN], owp[MaxN], oowp[MaxN], rpi[MaxN];
char s[MaxN][MaxN];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, n;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) cnt[i] = win[i] = 0;
        for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) {
            scanf(" %c", &s[i][j]);
            if (s[i][j] != '.') {
                ++cnt[i];
                if (s[i][j] == '1') ++win[i];
            }
        }
        for (int i = 0; i < n; ++i) {
            wp[i] = (double)win[i] / cnt[i];
        }
        for (int i = 0; i < n; ++i) {
            owp[i] = 0.0;
            for (int j = 0; j < n; ++j) if (s[i][j] != '.') {
                owp[i] += (double)(s[j][i] == '1' ? win[j] - 1 : win[j]) / (cnt[j] - 1);
            }
            owp[i] /= cnt[i];
        }
        for (int i = 0; i < n; ++i) {
            oowp[i] = 0.0;
            for (int j = 0; j < n; ++j) if (s[i][j] != '.') {
                oowp[i] += owp[j];
            }
            oowp[i] /= cnt[i];
        }
        for (int i = 0; i < n; ++i) {
            rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
        }
        printf("Case #%d:\n", cas);
        for (int i = 0; i < n; ++i) {
            printf("%.12f\n", rpi[i]);
        }

//        for (int i = 0; i < n; ++i) {
//            printf("%.3f ", wp[i]);
//        }
//        puts("");
//
//        for (int i = 0; i < n; ++i) {
//            printf("%.3f ", owp[i]);
//        }
//        puts("");
//
//        for (int i = 0; i < n; ++i) {
//            printf("%.3f ", oowp[i]);
//        }
//        puts("");
//
//        for (int i = 0; i < n; ++i) {
//            printf("%.3f ", rpi[i]);
//        }
//        puts("");
    }
    return 0;
}
