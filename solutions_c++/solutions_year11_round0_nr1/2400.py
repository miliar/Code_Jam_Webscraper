#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

pair<int, int> va[150];
pair<int, int> vb[150];

int main() {
    int t;
    scanf("%d ", &t);
    for (int k = 0; k < t; k++) {
        int n;
        scanf("%d ", &n);
        int na = 0, nb = 0, pa = 1, pb = 1;
        int senha = 0;
        char c;
        int x;
        for (int i = 0; i < n; i++) {
            scanf("%c %d ", &c, &x);
            if (c == 'O') {
                va[na].first = x;
                va[na].second = i;
                na++;
            }
            if (c == 'B') {
                vb[nb].first = x;
                vb[nb].second = i;
                nb++;
            }
            //printf("%c %d\n", c, x);
        }
        int res = 0;
        int iA = 0, iB = 0;
        bool apertou;
        while (1) {
            //printf("%d %d %d %d\n", pa, pb, senha, res);
            if (senha == n) break;
            if (iA < na) {
                if (pa < va[iA].first) {
                    pa++;
                }
                else if (pa > va[iA].first) {
                    pa--;
                }
                else {
                    if (senha == va[iA].second) {
                        iA++;
                        senha++;
                        res++;
                        if (iB < nb) {
                            if (pb < vb[iB].first) {
                                pb++;
                            }
                            else if (pb > vb[iB].first) {
                                pb--;
                            }
                        }
                        continue;
                    }
                }
            }
            if (iB < nb) {
                if (pb < vb[iB].first) {
                    pb++;
                }
                else if (pb > vb[iB].first) {
                    pb--;
                }
                else {
                    if (senha == vb[iB].second) {
                        iB++;
                        senha++;
                        res++;
                        continue;
                    }
                }
            }
            res++;
        }
        printf("Case #%d: %d\n", k+1, res);
    }
    return 0;
}
