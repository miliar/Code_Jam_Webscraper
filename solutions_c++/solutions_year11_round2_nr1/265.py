#include <cstdio>

char d[110][110];
int win[110], lose[110];
double wp[110];
double owp[110];
double oowp[110];

int main() {
    int T, n, winw, losel;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%s", d[i]);
        for (int i = 0; i < n; i++) {
            winw = losel = 0;
            for (int j = 0; j < n; j++) {
                if (d[i][j] == '1')
                    winw++;
                else if (d[i][j] == '0')
                    losel++;
            }
            win[i] = winw; lose[i] = losel;
            wp[i] = winw * 1.0 / (winw + losel);
        }
        for (int i = 0; i < n; i++) {
            double s = 0;
            int cnt = 0;
            for (int j = 0; j < n; j++) {
                if (d[i][j] == '0') {
                    s += 1.0 * (win[j] - 1) / (win[j] + lose[j] - 1);
                    cnt ++;
                } else if (d[i][j] == '1') {
                    s += 1.0 * win[j] / (win[j] + lose[j] - 1);
                    cnt ++;
                }
            }
            owp[i] = s / cnt;
        }
        for (int i = 0; i < n; i++) {
            double s = 0;
            int cnt = 0;
            for (int j = 0; j < n; j++) {
                if (d[i][j] == '0' || d[i][j] == '1') {
                    s += owp[j];
                    cnt++;
                }
            }
            oowp[i] = s / cnt;
        }
        printf("Case #%d:\n", t);
        for (int i = 0; i < n; i++) {
            //printf("wp = %f, owp = %f, oowp = %f\n", wp[i], owp[i], oowp[i]);
            double x = wp[i] * 0.25 + owp[i] * 0.5 + 0.25 * oowp[i];
            printf("%.20lf\n", x);
        }
    }
}
