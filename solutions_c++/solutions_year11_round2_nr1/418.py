#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <map>
#include <string>

using namespace std;

char g[110][110];
double wp[110];
double wp1[110][110];
//double wp2[110][110][110];
double owp[110];
//double owp2[110][110];
double oowp[110];

int main()
{
    int cn, cns;

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    scanf("%d", &cns);
    for (cn = 0; cn < cns; cn++) {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%s", g[i]);
        }
        for (int i = 0; i < n; i++) {
            int cc1 = 0, cc2 = 0;
            for (int j = 0; j < n; j++) {
                if (g[i][j] == '1' || g[i][j] == '0') {
                    cc2++;
                    if (g[i][j] == '1')
                        cc1++;
                }
            }
            wp[i] = (double)cc1 / cc2;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int cc1 = 0, cc2 = 0;
                for (int k = 0; k < n; k++) {
                    if (k != j) {
                        if (g[i][k] == '1' || g[i][k] == '0') {
                            cc2++;
                            if (g[i][k] == '1')
                                cc1++;
                        }
                    }
                }
                wp1[i][j] = (double)cc1 / cc2;
            }
        }

        for (int i = 0; i < n; i++) {
            owp[i] = 0;
            int cc = 0;
            for (int j = 0; j < n; j++) {
                if (g[i][j] != '.') {
                    owp[i] += wp1[j][i];
                    cc++;
                }
            }
            owp[i] /= cc;
        }

        for (int i = 0; i < n; i++) {
            oowp[i] = 0;
            int cc = 0;
            for (int j = 0; j < n; j++) {
                if (g[i][j] != '.') {
                    oowp[i] += owp[j];
                    cc++;
                }
            }
            oowp[i] /= cc;
        }
        printf("Case #%d:\n", cn + 1);
        for (int i = 0; i < n; i++) {
            printf("%.10lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
        }
    }
    return 0;
}
