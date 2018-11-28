#include <cstdio>
#include <cstdlib>
#include <cstring>

int n, comb[1005][1005], oppo[1005][1005], invo[1005];
char s[1005];

int main()
{
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);

    int Test; scanf("%d", &Test);
    for (int tts = 1; tts <= Test; ++tts) {
        scanf("%d", &n);
        memset(comb, 0, sizeof(comb));
        for (int i = 1; i <= n; ++i) {
            scanf("%s", s);
            comb[s[0]][s[1]] = s[2];
            comb[s[1]][s[0]] = s[2];
        }

        scanf("%d", &n);
        memset(oppo, 0, sizeof(oppo));
        for (int i = 1; i <= n; ++i) {
            scanf("%s", s);
            oppo[s[0]][s[1]] = 1;
            oppo[s[1]][s[0]] = 1;
        }

        scanf("%d", &n);
        scanf("%s", s + 1);
        invo[0] = 0;
        for (int i = 1; i <= n; ++i) {
            invo[++invo[0]] = s[i];
            if (invo[0] > 1 && comb[s[i]][invo[invo[0]-1]]) {
                --invo[0];
                invo[invo[0]] = comb[s[i]][invo[invo[0]]];
            }
            for (int j = 1; j < invo[0]; ++j)
            if (oppo[invo[j]][invo[invo[0]]]) { invo[0] = 0; break; }
        }
        printf("Case #%d: [", tts);
        for (int i = 1; i <= invo[0]; ++i) {
            putchar(invo[i]);
            if (i < invo[0]) printf(", ");
        }
        printf("]\n");
    }
    return 0;
}
