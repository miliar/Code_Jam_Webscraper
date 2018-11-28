#include <cstdio>
#include <cstring>

const char pattern[] = "welcome to code jam";
const int PAT_LEN = sizeof(pattern) - 1;
const int MAX_N = 600;
const int MODS = 10000;

int best[MAX_N][PAT_LEN];
char str[MAX_N];
int T, t, len, i, j, k, ans;

int main() {
    scanf("%d ", &T);
    for (t = 1; t <= T; t++) {
        fgets(str, sizeof(str), stdin);
        len = strlen(str) - 1;
        for (i = 0; i < len; i++) {
            best[i][0] = (str[i] == pattern[0]) ? 1 : 0;
            for (j = 1; j < PAT_LEN; j++) {
                best[i][j] = 0;
                if (str[i] != pattern[j])
                    continue;
                for (k = 0; k < i; k++)
                    if (pattern[j - 1] == str[k])
                        best[i][j] += best[k][j - 1];
                best[i][j] %= MODS;
            }
        }
        ans = 0;
        for (i = 0; i < len; i++)
            ans += best[i][PAT_LEN - 1];
        ans %= 10000;
        printf("Case #%d: %04d\n", t, ans);
    }

    return 0;
}

