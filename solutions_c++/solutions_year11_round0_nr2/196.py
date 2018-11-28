#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
using namespace std;
int t,N,len,cas;
char str[1100];
char ans[1100];
char u[310][310], d[310][310];
int main() {
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    int i, j, a;
    int un,dn;
    scanf("%d", &t);
    for(cas=1;cas<=t;cas++){
        memset(u, 0, sizeof (u));
        memset(d, 0, sizeof (d));
        scanf("%d", &un);
        for (i = 0; i < un; i++) {
            scanf("%s", str);
            u[str[0]][str[1]] =u[str[1]][str[0]]= str[2];
        }
        scanf("%d", &dn);
        for (i = 0; i < dn; i++) {
            scanf("%s", str);
            d[str[0]][str[1]] = d[str[1]][str[0]] = 1;
        }
        scanf("%d%s", &N, str);
        len = -1;
        for (i = 0; i < N; i++) {
            ans[++len] = str[i];
            while (len - 1 >= 0) {
                if (u[ans[len]][ans[len - 1]] != 0) {
                    ans[len - 1] = u[ans[len]][ans[len - 1]];
                    len--;
                }else break;
            }
            for (j = 0; j < len; j++)
                if (d[ans[len]][ans[j]] == 1) {
                    len = -1;
                }
        }
        printf("Case #%d: [", cas);
        for (i = 0; i <= len; i++)
            if (i != len) printf("%c, ", ans[i]);
            else printf("%c", ans[i]);
        printf("]\n");
    }
    return 0;
}


