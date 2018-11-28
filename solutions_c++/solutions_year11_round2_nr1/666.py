#include <cstdio>
#include <cstring>
#include <algorithm>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#define sys system("pause")
using namespace std;
char maz[300][300];
int n;
// RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
double wp[300];
double owp[300];
double oowp[300];

int main() {
   // freopen("a.in", "r", stdin);
  //  freopen("a.txt", "w", stdout);
    int T, cas = 1;
    scanf("%d", &T);
    while (T--) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%s", maz[i]);
        }
        for (int i = 0; i < n; ++i) {
            double a = 0;
            int b = 0;
            for (int j = 0; j < n; ++j) {
                if (maz[i][j] == '1') {
                    ++a;
                }
                if (maz[i][j] != '.') {
                    ++b;
                }
            }
            if (b != 0) {
                wp[i] = a / (1.0 * b);
            } else {
                wp[i] = 0;
            }
        }
        for (int i = 0; i < n; ++i) {
            owp[i] = 0.0;
            int cnt = 0;
            for (int j = 0; j < n; ++j) {
                if (maz[i][j] != '.') {
                    ++cnt;
                    double a = 0;
                    int b = 0;
                    for (int k = 0; k < n; ++k) {
                        if (k != i) {
                            if (maz[j][k] == '1') {
                                ++a;
                            }
                            if (maz[j][k] != '.') {
                                ++b;
                            }
                        }
                    }
                    if (b != 0) {
                        owp[i] += (a / (1.0 * b));
                    }
                }
            }
            if (cnt != 0) {
                owp[i] /= cnt;
            }
        }
        for (int i = 0; i < n; ++i) {
            oowp[i] = 0.0;
            int cnt = 0;
            for (int j = 0; j < n; ++j) {
                if (maz[i][j] != '.') {
                    ++cnt;
                    oowp[i] += owp[j];
                }
            }
            if (cnt != 0) {
                oowp[i] /= cnt;
            }
        }
        printf("Case #%d:\n", cas++);
        for (int i = 0; i < n; ++i) {
            printf("%.10lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
        }
    }
   // sys;
    return 0;
}
// RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
