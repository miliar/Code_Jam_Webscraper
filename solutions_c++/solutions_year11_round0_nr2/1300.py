#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char comb[40][5];
char delt[40][4];
char str[110];
char que[110];
int head, tail;

int main() {
    int t, c, d, n, clk = 0;
    freopen("B-large.in", "r", stdin);
    freopen("outB.txt", "w", stdout);
    scanf("%d", &t);
    while (t--) {
        int i;
        scanf("%d", &c);
        for (i = 0; i < c; ++i) {
            scanf("%s", comb[i]);
        }
        scanf("%d", &d);
        for (i = 0; i < d; ++i) {
            scanf("%s", delt[i]);
        }
        scanf("%d%s", &n, str);

        head = tail = 0;
        int k = 0;
        while (k < n) {
            que[head++] = str[k++];
            //printf("%c", que[head-1]);
            for (i = 0; i < c; ++i) {
                if(head < 2) break;
                if (comb[i][0] == que[head-1] && comb[i][1] == que[head-2]) {
                    head -= 2;
                    que[head++] = comb[i][2];
                    break;
                }
                else if (comb[i][1] == que[head-1] && comb[i][0] == que[head-2]) {
                    head -= 2;
                    que[head++] = comb[i][2];
                    break;
                }
            }
            for (i = 0; i < head-1; ++i) { 
                for (int j = 0; j < d; ++j) {
                    if(delt[j][0] == que[i] && delt[j][1] == que[head-1]) {
                        head = 0;
                        break;
                    }
                    else if (delt[j][1] == que[i] && delt[j][0] == que[head-1]) {
                        head = 0;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: [", ++clk);
        for (i = 0; i < head-1; ++i)
            printf("%c, ", que[i]);
        if(head > 0)printf("%c", que[i]);
        puts("]");
    }
//   system("pause");
    return 0;
}
