#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
    int T;
    int n, s, p, x[110];
    int qnt;
    int q, r;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        qnt = 0;
        scanf("%d %d %d", &n, &s, &p);
        for (int i = 0; i < n; i++) {
            scanf("%d", &x[i]);
        }
        for (int i = 0; i < n; i++) {
            if (x[i] == 0) {
                if (p == 0) {
                    qnt++;
                }
                continue;
            }
            if (x[i] == 1) {
                if (1 >= p) {
                    qnt++;
                }
                continue;
            }
            q = x[i] / 3;
            r = x[i] % 3;
            if (r == 0) {
                if (q >= p) {
                    qnt++;
                }
                else if (s > 0 && q+1 >= p) {
                    qnt++;
                    s--;
                }
            }
            else if (r == 1) {
                if (q+1 >= p) {
                    qnt++;
                }
            }
            else {
                if (q+1 >= p) {
                    qnt++;
                }
                else if (s > 0 && q+2 >= p) {
                    qnt++;
                    s--;
                }
            }
        }
        printf("Case #%d: %d\n", t, qnt);
    }
}
