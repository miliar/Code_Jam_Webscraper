#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
const int MAXN = 101;
char mat[MAXN][MAXN];
double win[MAXN], sum[MAXN];
double wp[MAXN], owp[MAXN], oowp[MAXN];
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int cas, n;
    scanf("%d", &cas);
    for (int T = 1; T <= cas; T++) {
        scanf("%d", &n);
        memset(win, 0, sizeof(win));
        memset(sum, 0, sizeof(sum));
        memset(wp, 0, sizeof(wp));
        memset(owp, 0, sizeof(owp));
        memset(oowp, 0, sizeof(oowp));
        for (int i = 0; i < n; i++) {
            getchar();
            wp[i] = 0;
            for (int j = 0; j < n; j++) {
                scanf("%c", &mat[i][j]);
                if (mat[i][j] == '0') {
                    sum[i]++;
                } else if (mat[i][j] == '1') {
                    sum[i]++;
                    wp[i]++;
                }
            }
            wp[i] /= sum[i];
        }
        for (int i = 0; i < n; i++) {
            owp[i] = 0;
            for (int j = 0; j < n; j++) {
                if (mat[i][j] != '.') {
                    double tmp = (wp[j] * sum[j] - (mat[j][i] - '0')) / (sum[j] - 1);
                    owp[i] += tmp;
                }
            }
            owp[i] /= sum[i];
        }
        for (int i = 0; i < n; i++) {
            oowp[i] = 0;
            for (int j = 0; j < n; j++) {
                if (mat[i][j] != '.') {
                    oowp[i] += owp[j];
                }
            }
            oowp[i] /= sum[i];
        }
        printf("Case #%d:\n", T);
        for (int i = 0; i < n; i++) {
            //cout << wp[i] << ' ' << owp[i] << ' ' << oowp[i] << endl;
            printf("%.10lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
        }
    }
}
