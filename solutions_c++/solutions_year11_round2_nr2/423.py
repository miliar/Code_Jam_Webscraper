#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <map>
#include <string>

using namespace std;

const int MAXN = 1000100;

double aa[MAXN];
int bb[MAXN];
int sum[MAXN];

int main()
{
    int cn, cns;

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    scanf("%d", &cns);
    for (cn = 0; cn < cns; cn++) {
        int n, m;
        scanf("%d%d", &n, &m);
        //int cc = 0;
        sum[0] = 0;
        for (int i = 1; i <= n; i++) {
            int x, y;
            scanf("%d%d", &x, &y);
            aa[i] = x;
            bb[i] = y;
            sum[i] = sum[i - 1] + bb[i];
        }
        //printf("%d\n", cc);

        double l = 0, r = 1e12 + 10;
        int cc = 0;
        while (r - l > 1e-8 && cc < 1000) {
            double mid = (l + r) / 2;
            cc++;
            //printf("%lf %lf\n", l, r);
            bool ok = true;
            for (int i = 1; i <= n; i++) {
                if (bb[i] > 1) {
                    if ((double)m * (bb[i] - 1) / 2 > mid) {
                        ok = false;
                        break;
                    }
                }
                for (int j = i + 1; j <= n; j++) {
                    if (fabs(aa[j] - aa[i]) < (double)m * (sum[j] - sum[i - 1] - 1)) {
                        if (((double)m * (sum[j] - sum[i - 1] - 1) - fabs(aa[j] - aa[i])) / 2 > mid) {
                            ok = false;
                            break;
                        }
                    }
                }
                if (!ok) {
                    break;
                }

            }
            if (ok) {
                r = mid;
            } else {
                l = mid;
            }
        }

        printf("Case #%d: %.10lf\n", cn + 1, r);
        /*
                while (r - l > 1e-9) {
                    double mid = (l + r) / 2;
                    bool ok = true;
                    for (int i = 0; i < n; i++) {
                        if ((double)m * (bb[i] - 1) / 2 > mid) {
                            ok = false;
                            break;
                        }
                        for (int j = i + 1; j < n; j++) {

                        }
                    }
                    for (int i = 0; i < cc; i++) {
                        for (int j = i + 1; j < cc; j++) {
                            if (fabs(aa[i] - aa[j]) < m * (j - i)) {
                                if ((m * (j - i) - fabs(aa[i] - aa[j])) / 2 > mid) {
                                    ok = false;
                                    break;
                                }
                            }
                        }
                        if (!ok) {
                            break;
                        }
                    }
                    if (ok) {
                        r = mid;
                    } else {
                        l = mid;
                    }
                }
        */
        //printf("Case #%d: %.10lf\n", cn + 1, r);
    }
    return 0;
}
