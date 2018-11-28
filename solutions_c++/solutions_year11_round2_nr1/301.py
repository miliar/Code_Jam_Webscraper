#include <cstdio>
#include <string>
#include <vector>
#include <memory.h>
#include <cstring>
#include <cmath>

using namespace std;

char mapp[300][300];

double WP[300];
double OWP[300];
double OOWP[300];

int main() {

    int t;
    int n;

    scanf("%d", &t);

    for (int test = 1;test <= t;++test) {

        scanf("%d", &n);
        for (int i = 0;i < n;++i)
            scanf("%s", mapp[i]);

        for (int i = 0;i < n;++i) {
            int a = 0;
            int b = 0;
            for (int j = 0;j < n;++j) {
                if (mapp[i][j] == '.') continue;
                if (mapp[i][j] == '1') ++a;
                ++b;
            }
            WP[i] = (0.0 + a) / b;
        }

        for (int i = 0;i < n;++i) {
            double a = 0;
            int b = 0;
            for (int j = 0;j < n;++j) {
                if (mapp[i][j] == '.') continue;
                int aa = 0;
                int bb = 0;
                for (int k = 0;k < n;++k) {
                    if (mapp[j][k] == '.' || k == i) continue;
                    if (mapp[j][k] == '1') ++aa;
                    ++bb;
                }
                a += (0.0 + aa) / bb;
                ++b;
            }
            if (b)
                OWP[i] = a / b;
            else
                OWP[i] = 0.0;
        }

        for (int i = 0;i < n;++i) {
            double a = 0;
            int b = 0;
            for (int j = 0;j < n;++j) {
                if (mapp[i][j] == '.') continue;
//                for (int k = 0;k < n;++k) {

                //              }
                a += OWP[j];
                ++b;
            }
            if (b)
                OOWP[i] = a / b;
            else
                OOWP[i] = 0.0;
        }

        printf("Case #%d:\n", test);
        for (int i = 0;i < n;++i)
            printf("%.8lf\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
    }

    return 0;
}
