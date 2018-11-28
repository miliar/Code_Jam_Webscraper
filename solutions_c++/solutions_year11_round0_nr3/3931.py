#include <iostream>

using namespace std;
char comb[200][3];
char oppo[200][3];
int tc;
char result[200];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("gcj.out","w",stdout);
    scanf("%d",&tc);
    int b;
    b = tc;
    while(tc) {
        char t[105];
        int n,m;
        int d;
        scanf("%d ",&n);
        for(int i = 1; i<= n; i++)
         scanf("%s",&comb[i]);
        scanf("%d ",&m);
        for(int i = 1; i<= m; i++)
         scanf("%s",&oppo[i]);
        scanf("%d",&d);
        scanf("%s",&t);
        int fin = 0;
        for(int i = 0; i < strlen(t); i++) {
          if (fin == 0) {
              result[fin] = t[i];
              fin++;
          }
          else {
              int ok = 1;
              for(int j = 1; j <= n; j++)
                 if (t[i] == comb[j][0]) {
                    if (result[fin-1] == comb[j][1]) {
                        result[fin-1] = comb[j][2];
                        ok = 0;
                    }
                  }
                  else
                    if (t[i] == comb[j][1]) {
                        if (result[fin-1] == comb[j][0]) {
                            result[fin-1] = comb[j][2];
                            ok = 0;
                        }
                    }
            if (ok != 0) {
                for(int k = 1; k <= m; k++)
                 if ((t[i] == oppo[k][0])) {
                   for(int j = 0; j < fin; j++)
                    if (result[j] == oppo[k][1]) {
                     fin = 0;
                     ok = 0;
                     k = m + 1;
                     break;
                    }

                }
                else
                 if (t[i] == oppo[k][1]) {
                   for(int j = 0; j < fin; j++)
                    if (result[j] == oppo[k][0]) {
                     fin = 0;
                     k = m + 1;
                     ok = 0;
                     break;
                    }
                }
          }
          if (ok != 0) {
              result[fin++] = t[i];
          }
          }
          }
        printf("Case #%d: ",b - tc + 1);
        printf("[");
        for(int u = 0; u < fin - 1; u++) {
         printf("%c, ",result[u]);
         result[u] = '\0';
        }
        if (fin != 0)
        printf("%c",result[fin-1]);
        printf("]");
        printf("\n");
        tc--;
    }
    return 0;
}
