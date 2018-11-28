#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int aa[110];
int dex1[110];
int bb[110];
int dex2[110];

int main()
{
    int cn, cns;

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    scanf("%d", &cns);
    for (cn = 0; cn < cns; cn++) {
        int n;
        scanf("%d", &n);
        int id;
        char ss[10];
        int cc1 = 0, cc2 = 0;
        for (int i = 0; i < n; i++) {
            scanf("%s%d", ss, &id);
            if (ss[0] == 'B') {
                aa[cc1] = id;
                dex1[cc1++] = i;
            } else if (ss[0] == 'O') {
                bb[cc2] = id;
                dex2[cc2++] = i;
            }
        }

        int a1 = 1, a2 = 1;
        int id1 = 0, id2 = 0;
        int cc = 0;
        int ans;
        for (int i = 0; ; i++) {
            int la = id1;
            int lb = id2;
            if (la < cc1) {
                if (a1 < aa[la]) {
                    a1++;
                } else if (a1 > aa[la]) {
                    a1--;
                } else {
                    if (lb >= cc2 || dex1[la] < dex2[lb]) {
                        id1++;
                        cc++;
                    }
                }
            }
            if (lb < cc2) {
                if (a2 < bb[lb]) {
                    a2++;
                } else if (a2 > bb[lb]) {
                    a2--;
                } else {
                    if (la >= cc1 || dex1[la] > dex2[lb]) {
                        id2++;
                        cc++;
                    }
                }
            }
            if (cc >= n) {
                ans = i + 1;
                break;
            }
        }

        printf("Case #%d: %d\n", cn + 1, ans);
    }
    return 0;
}
