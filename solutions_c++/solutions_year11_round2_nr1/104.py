#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

char g[200][200];
double WP[200][200], OWP[200], OOWP[200], RPI[200];
int won[200], tot[200];

int main() {
    int tot_t, n;
    scanf("%d", &tot_t);
    for (int cur_t = 0; cur_t < tot_t; ++cur_t) {
        scanf("%d", &n);

        memset(won, 0, sizeof won);
        memset(tot, 0, sizeof tot);
        memset(WP, 0, sizeof WP);
        memset(OWP, 0, sizeof OWP);
        memset(OOWP, 0, sizeof OOWP);
        memset(RPI, 0, sizeof RPI);

        for (int i = 0; i < n; ++i) {
            scanf("%s", g[i]);
            for (int j = 0; j < n; ++j) {
                if (j != i) {
                    if (g[i][j] != '.') {
                        ++tot[i];
                    }
                    if (g[i][j] == '1') {
                        ++won[i];
                    }
                }
            }
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (j == i) {
                    continue;
                }
                int tot = 0, won = 0;
                for (int k = 0; k < n; ++k) {
                    if (k != i && k != j) {
                        if (g[i][k] != '.') {
                            ++tot;
                        }
                        if (g[i][k] == '1') {
                            ++won;
                        }
                    }
                }
                WP[i][j] = (double)won / tot;
            }
        }


        for (int i = 0; i < n ; ++i) {
            double sum = 0;
            int tot_op = 0;
            for (int j = 0; j < n; ++j) {
                if (j != i && g[i][j] != '.') {
                    ++tot_op;
                    sum += WP[j][i];
                }
            }
            OWP[i] = sum / tot_op;
        }

        for (int i = 0; i < n; ++i) {
            double sum = 0;
            int tot_op = 0;
            for (int j = 0; j < n; ++j) {
                if (j != i && g[i][j] != '.') {
                    ++tot_op;
                    sum += OWP[j];
                }
            }
            OOWP[i] = sum / tot_op;
        }

        for (int i = 0; i < n; ++i) {
            RPI[i] = 0.25 * (double)won[i] / tot[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
        }

        printf("Case #%d:\n", cur_t + 1);
        for (int i = 0; i < n; ++i) {
            printf("%.10f\n", RPI[i]);
        }
    }
    return 0;
}

