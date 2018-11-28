#include <cstdio>
#include <cstdlib>
#include <cstring>

int n, m, len[10005], Q[10005], P[10005];
char a[10005][105], s[50];
bool us[10005];

    inline int Guess(int u)
    {
        memset(us, 0, sizeof(us));
        int tot = n;
        for (int i = 1; i <= n; ++i)
        if (len[i] != len[u]) { us[i] = 1; --tot; }
        if (tot == 1) return 0;
        int ll = strlen(s + 1), wa = 0, wh;
        for (int k = 1; k <= ll; ++k) {
            Q[0] = 0;
            for (int i = 1; i <= len[u]; ++i)
            if (a[u][i] == s[k]) Q[++Q[0]] = i;
            bool ff = 0;
            for (int i = 1; i <= n; ++i)
            if (!us[i]) {
                P[0] = 0;
                for (int j = 1; j <= len[i]; ++j)
                if (a[i][j] == s[k]) P[++P[0]] = j;
                if (P[0] > 0 && Q[0] == 0) {
                    ff = 1; --tot; us[i] = 1;
                    continue;
                }
                if (Q[0] != P[0]) {
                    --tot; us[i] = 1;
                    continue;
                }
                for (int j = 1; j <= Q[0]; ++j)
                if (Q[j] != P[j]) {
                    --tot; us[i] = 1;
                    break;
                }
            }
            if (ff) ++wa;
            if (tot == 1) return wa;
        }
        return wa;
    }

int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);
    int Test, tts = 0;
    for (scanf("%d", &Test); Test--; ) {
        printf("Case #%d:", ++tts);
        scanf("%d%d", &n, &m);
        for (int i = 1; i <= n; ++i) {
            scanf("%s", a[i] + 1);
            len[i] = strlen(a[i] + 1);
        }
        for (int o = 1; o <= m; ++o) {
            scanf("%s", s + 1);
            int id = 0, mx = -1;
            for (int i = 1; i <= n; ++i) {
                int tmp = Guess(i);
                if (tmp > mx) {
                    mx = tmp;
                    id = i;
                }
            }
            printf(" %s", a[id] + 1);
        }
        puts("");
    }
    return 0;
}
