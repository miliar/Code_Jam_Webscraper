#include <cstdio>
#include <memory>

int f[600][20];

char e[100] = "welcome to code jam";
char s[600];

void solve() {
    memset(f, 0, sizeof f);
    f[0][0] = 1;
    gets(s);
    int len = strlen(s);
    int lene = strlen(e);
    for (int i = 0; i < len; i++) {
        for (int j = 0; j <= lene; j++) {
            f[i + 1][j] = f[i][j];
        }
        for (int j = 0; j < lene; j++)
            if (s[i] == e[j]) {
                f[i + 1][j + 1] += f[i][j];
                f[i + 1][j + 1] %= 1000;
            }
    }
    printf("%04d\n", f[len][lene]);
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int N;
    scanf("%d", &N);
    gets(s);
    for (int i = 0; i < N; i++) {
        printf("Case #%d: ", i + 1);
        solve();
    }
    return 0;
}
