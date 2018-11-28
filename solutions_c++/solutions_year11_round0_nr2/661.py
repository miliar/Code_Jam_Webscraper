#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

const int MAXN = 1024;
char buf[MAXN];
char comb[300][300], op[300][300];
char res[MAXN];

int main() {
    //freopen("B-small.in","r",stdin);
    //freopen("B-small.out","w",stdout);
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T, ca, C, D, i;
    scanf("%d",&T);
    for (ca = 1 ; ca <= T ; ++ca) {
        memset(comb, 0, sizeof(comb));
        memset(op, 0, sizeof(op));
        scanf("%d",&C);
        while (C--) {
            scanf("%s",buf);
            comb[buf[0]][buf[1]] = buf[2];
            comb[buf[1]][buf[0]] = buf[2];
        }
        scanf("%d",&D);
        while (D--) {
            scanf("%s",buf);
            op[buf[0]][buf[1]] = 1;
            op[buf[1]][buf[0]] = 1;
        }
        int len;
        scanf("%d",&len);
        scanf("%s",buf);
        int pres = 0;
        for (i = 0 ; i < len ; ++i) {
            res[pres++] = buf[i];
            if (pres <= 1) continue;
            char ch;
            if (ch = comb[res[pres-2]][res[pres-1]]) {
                pres -= 2;
                res[pres++] = ch;
            } else {
                int j;
                for (j = 0 ; j < pres - 1 ; ++j)
                    if (op[res[j]][res[pres-1]]) break;
                if (j< pres - 1) pres = 0;
            }
        }
        printf("Case #%d: [", ca);
        for (int i = 0 ; i < pres ; ++i) {
            if (i) printf(", ");
            printf("%c", res[i]);
        }
        printf("]\n");
    }
    return 0;
}
