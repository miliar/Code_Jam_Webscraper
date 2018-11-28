#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main() {
    freopen("D:\\TopCoder\\gcj2011\\R1\\A.in", "r", stdin);
    freopen("D:\\TopCoder\\gcj2011\\R1\\A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ca++) {
        int n;
        scanf("%d", &n);
        char t[n+3][n+3];
        for (int i = 0; i < n; i++) {
            scanf("%s", t[i]);
        }
        
        double wp[n+3], owp[n+3], oowp[n+3], rpi[n+3];
        int w[n+3], a[n+3];
        for (int i = 0; i < n; i++) {
            int win = 0, all = 0;
            for (int j = 0; j < n; j++) {
                if (t[i][j] == '1') win++;
                else if (t[i][j] == '0') all++;
            }
            all += win;
            wp[i] = win * 1.0 / all;
            w[i] = win, a[i] = all;
        }
        for (int i = 0; i < n; i++) {
            owp[i] = 0;
            for (int j = 0; j < n; j++) {
                if (j == i) continue;
                if (t[i][j] != '.') {
                    int ww = 0, aa = 0;
                    for (int k = 0; k < n; k++) {
                        if (k == i) continue;
                        if (t[j][k] == '1') ++ww;
                        else if (t[j][k] == '0') ++aa;
                    }
                    aa += ww;
                    double twp = ww * 1.0 / aa;
                    owp[i] += twp;
                }
            }
            //cout << i << ": " << owp[i] << " " << a[i] << endl;//
            owp[i] /= a[i];
        }
        for (int i = 0; i < n; i++) {
            oowp[i] = 0;
            for (int j = 0; j < n; j++) {
                if (j == i) continue;
                if (t[i][j] != '.') {
                    oowp[i] += owp[j];
                }
            }
            oowp[i] /= a[i];
        }
        for (int i = 0; i < n; i++) {
            //cout << i << ": " << wp[i] << ", " << owp[i] << ", " << oowp[i] << endl;//
            rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
        }
        
        printf("Case #%d:\n", ca);
        for (int i = 0; i < n; i++) {
            printf("%.7lf\n", rpi[i]);
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}

