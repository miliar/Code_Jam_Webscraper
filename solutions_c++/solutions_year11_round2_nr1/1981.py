#include <stdio.h>
#include <string.h>

int s[100][100];
double WP[100];
double OWP[100];
double OOWP[100];

int win[100];
int all[100];

int main() {
    int T;
    scanf("%d", &T);
    for(int num = 1; num <= T; ++num) {
        int N;
        scanf("%d", &N);
        memset(s, 0, sizeof(s));
        memset(WP, 0, sizeof(WP));
        memset(OWP, 0, sizeof(OWP));
        memset(OOWP, 0, sizeof(OOWP));
        memset(win, 0, sizeof(win));
        memset(all, 0, sizeof(all));
        for (int i = 0; i < N; ++i) {
            char tmp[100];
            scanf("%s", tmp);
            for (int j = 0; j < N; ++j) {
                if (tmp[j] == '1')
                    s[i][j] = 1;
                else if (tmp[j] == '0')
                    s[i][j] = 0;
                else
                    s[i][j] = -1;
            }
        }
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (s[i][j] != -1) {
                    ++all[i];
                    if (s[i][j] == 1) ++win[i];
                }
            }
            WP[i] = (double)win[i] / all[i];
        }
        for (int i = 0; i < N; ++i) {
            double t1 = 0, t2 = 0;
            for (int j = 0; j < N; ++j) {
                if (s[i][j] != -1) {
                    ++t1;
                    if (s[i][j] == 1) {
                        t2 += (double)win[j] / (all[j] - 1);
                    } else {
                        t2 += (double)(win[j] - 1) / (all[j] - 1);
                    }
                }
            }
            OWP[i] = t2 / t1;

        }
        for (int i = 0; i < N; ++i) {
            double t1 = 0, t2 = 0;
            for (int j = 0; j < N; ++j) {
                if (s[i][j] != -1) {
                    ++t1;
                    t2 += OWP[j];
                }
            }
            OOWP[i] = t2 / t1;
        }
        printf("Case #%d:\n", num);
        for (int i = 0; i < N; ++i) {
            printf("%lf\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
        }
    }
    return 0;
}
