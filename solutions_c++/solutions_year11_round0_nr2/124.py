#include <stdio.h>
#include <string.h>

int T, C, D, N, t[110];
char a, b, c, s[110];
int com[30][30];
bool opp[30][30];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        memset(com, -1, sizeof(com));
        memset(opp, 0, sizeof(opp));
        scanf("%d", &C);
        while (C--) {
            scanf(" %c %c %c", &a, &b, &c);
            a -= 'A', b -= 'A', c -= 'A';
            com[a][b] = com[b][a] = c;
        }
        scanf("%d", &D);
        while (D--) {
            scanf(" %c %c", &a, &b);
            a -= 'A', b -= 'A';
            opp[a][b] = opp[b][a] = 1;
        }
        scanf("%d%s", &N, s);
        int n = 0;
        for (int i = 0; i < N; ++i) {
            t[n++] = s[i] - 'A';
            while (n > 1 && com[t[n-1]][t[n-2]] != -1) {
                t[n-2] = com[t[n-1]][t[n-2]];
                --n;
            }
            for (int j = 0; j < n-1; ++j) if (opp[t[n-1]][t[j]]) {
                n = 0;
                break;
            }
        }
        printf("Case #%d: [", cas);
        for (int i = 0; i < n; ++i) {
            if (i) printf(", ");
            putchar(t[i] + 'A');
        }
        puts("]");
    }
    return 0;
}
