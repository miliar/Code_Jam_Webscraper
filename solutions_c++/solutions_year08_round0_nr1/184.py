#include <cstdio>

int T, z[1000], s, q, dp[1001][100], a;
char t[256], e[100][256];

bool eq(char *s, char *t) {
        while (*s && *s == *t) {
                ++s;
                ++t;
        }
        return *s == *t;
}

int find(char *z) {
        for (int i = 0; i < s; ++i)
                if (eq(z, e[i]))
                        return i;
        return -1;
}

int main() {
        scanf("%d", &T);
        for (int r = 1; r <= T; ++r) {
                printf("Case #%d: ", r);
                scanf("%d", &s);
                gets(t);
                for (int i = 0; i < s; ++i)
                        gets(e[i]);
                scanf("%d", &q);
                gets(t);
                for (int i = 0; i < q; ++i) {
                        gets(t);
                        if ((z[i] = find(t)) == -1) {
                                --i;
                                --q;
                        }
                }
                for (int j = 0; j < s; ++j)
                        dp[0][j] = 0;
                for (int i = 0; i < q; ++i)
                        for (int j = 0; j < s; ++j)
                                if (z[i] == j)
                                        dp[i + 1][j] = 1 << 30;
                                else {
                                        dp[i + 1][j] = dp[i][j];
                                        for (int k = 0; k < s; ++k)
                                                if (dp[i][k] + 1 < dp[i + 1][j])
                                                        dp[i + 1][j] = dp[i][k] + 1;
                                }
                a = 1 << 30;
                for (int j = 0; j < s; ++j)
                        if (dp[q][j] < a)
                                a = dp[q][j];
/*
                for (int i = 0; i <= q; ++i) {
                        for (int j = 0; j < s; ++j)
                                printf("%d ", dp[i][j]);
                        puts("");
                }
*/
                printf("%d\n", a);
        }
        return 0;
}
