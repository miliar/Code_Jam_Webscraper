#include<stdio.h>
#include<string.h>

int main()
{
    int i, j, k;
    char oppose[100][100];
    char combine[100][100];
    int noppose, ncombine;
    int t, nowt;
    int n;
    char ele[1000];
    char finaln, finalele[1000];

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    nowt = 0;
    scanf("%d", &t);
    while (t--) {
        nowt ++;
        scanf("%d", &ncombine);
        for (i = 0; i < ncombine; i ++) {
            scanf("%s", combine[i]);
        }
        scanf("%d", &noppose);
        for (i = 0; i < noppose; i ++) {
            scanf("%s", oppose[i]);
        }
        scanf("%d%s", &n, ele);

        finaln = 0;
        for (i = 0; i < n; i ++) {
            finalele[finaln] = ele[i];
            finaln ++;
            if (finaln <= 1)
                continue;

            for (j = 0; j < ncombine; j ++) {
                if ((finalele[finaln-1] == combine[j][0] && finalele[finaln-2] == combine[j][1]) ||
                    (finalele[finaln-2] == combine[j][0] && finalele[finaln-1] == combine[j][1])) {
                        finaln --;
                        finalele[finaln-1] = combine[j][2];
                        break;
                }
            }

            if (j < ncombine)
                continue;

            for (j = 0; j < noppose; j ++) {
                for (k = 0; k < finaln; k ++) {
                    if ((finalele[finaln-1] == oppose[j][0] && finalele[k] == oppose[j][1]) ||
                        (finalele[finaln-1] == oppose[j][1] && finalele[k] == oppose[j][0])) {
                            finaln = 0;
                            break;
                    }
                }
            }
        }

        finalele[finaln] = '\0';

        printf("Case #%d: ", nowt);
        printf("[");
        if (finaln > 0)
            printf("%c", finalele[0]);
        for (i = 1; i < finaln; i ++) {
            printf(", %c", finalele[i]);
        }
        printf("]\n");
    }
    return 0;
}