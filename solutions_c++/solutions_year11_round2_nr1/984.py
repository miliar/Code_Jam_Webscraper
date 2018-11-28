#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

int n_teams;
char match[1 << 7][1 << 7];
double wp[1 << 7];
double owp[1 << 7];
double oowp[1 << 7];

int main() {
    int kases;

    scanf("%d", &kases);
    for (int kase = 1; kase <= kases; ++kase) {
        scanf("%d", &n_teams);
        for (int i = 0; i < n_teams; ++i) scanf("%s", match[i]);

        for (int i = 0; i < n_teams; ++i) {
            int played = 0;

            wp[i] = 0.0;
            for (int j = 0; j < n_teams; ++j) {
                if (match[i][j] != '.') {
                    ++played;
                    if (match[i][j] == '1') wp[i] += 1.0;
                }
            }
            wp[i] /= played;
        }

        for (int i = 0; i < n_teams; ++i) {
            int n_opp = 0;
            double total_wp = 0.0;

            for (int j = 0; j < n_teams; ++j) {
                if (match[i][j] != '.') {
                    int played = 0;
                    double wp = 0.0;

                    for (int k = 0; k < n_teams; ++k) {
                        if (k == i) continue;
                        if (match[j][k] != '.') {
                            ++played;
                            wp += match[j][k] - '0';
                        }
                    }
                    wp /= played;

                    total_wp += wp;
                    ++n_opp;
                }
            }

            total_wp /= n_opp;
            owp[i] = total_wp;
        }

        for (int i = 0; i < n_teams; ++i) {
            int n = 0;
            oowp[i] = 0.0;

            for (int j = 0; j < n_teams; ++j) if (match[i][j] != '.') {
                oowp[i] += owp[j];
                ++n;
            }

            oowp[i] /= n;
        }





        printf("Case #%d:\n", kase);
        for (int i = 0; i < n_teams; ++i) {
            printf("%.12lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
            //printf("%.6lf %.6lf %.6lf %.12lf\n", wp[i], owp[i], oowp[i], 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
        }
    }

    return 0;
}
