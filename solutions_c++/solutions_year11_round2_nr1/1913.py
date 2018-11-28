#include <cstdio>
#include <cstring>

int tab[123][123];
double wp[123], owp[123], oowp[123];

int main() {
    int nt;
    int cases = 1;

    scanf(" %d", &nt);
    while (nt--) {
        int n;
        scanf(" %d", &n);
        memset(tab, -1, sizeof(tab));
        for (int i = 0; i < n; i++) {
            char line[123];
            scanf(" %s", line);
            for (int j = 0; j < n; j++)
                if (i != j)
                    tab[i][j] = line[j] == '.' ? -1 : line[j] - '0';
        }

        for (int i = 0; i < n; i++) {
            int win = 0, gam = 0;
            for (int j = 0; j < n; j++)
                if (i != j) {
                    win += tab[i][j] == 1 ? 1 : 0;
                    gam += tab[i][j] != -1 ? 1 : 0;
                }
            wp[i] = (double)win/gam;
            // printf("win: %d gam: %d %lf\n", win, gam, wp[i]);
        }
        // printf("---------\n");
        for (int k = 0; k < n; k++) {
            int cnt = 0;
            owp[k] = 0.0;
            for (int i = 0; i < n; i++) {
                int win = 0, gam = 0;
                if (tab[k][i] == -1) continue;
                for (int j = 0; j < n; j++)
                    if (i != j && j != k) {
                        win += tab[i][j] == 1 ? 1 : 0;
                        gam += tab[i][j] != -1 ? 1 : 0;
                    }
                // printf("win: %d gam: %d %lf\n", win, gam, (double)win/gam);
                owp[k] += (double)win/gam;
                ++cnt;
            }
            // printf("%d %d\n", k, cnt);
            owp[k] /= (double)cnt;
        }

        for (int i = 0; i < n; i++) {
            int cnt = 0;
            oowp[i] = 0.0;
            for (int j = 0; j < n; j++)
                if (i != j && tab[i][j] != -1) {
                    oowp[i] += owp[j];
                    ++cnt;
                }
            oowp[i] /= (double)cnt;
        }

        printf("Case #%d:\n", cases++);
        for (int i = 0; i < n; i++)
            printf("%lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
    }

    return 0;
}
