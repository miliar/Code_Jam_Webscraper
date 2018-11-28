#include <cstdio>
#include <cstring>

const int MAX_LEN = 1000;
const char STR[] = " welcome to code jam";
const char LEN = strlen(STR);

int main() {
    int N, c = 0;
    char line[MAX_LEN];
    int dp[MAX_LEN][LEN];

    for (scanf("%d", &N); N--;) {
        scanf(" %[^\n]", line + 1);

        int len = strlen(line + 1);

        memset(dp, 0, sizeof dp);
        dp[0][0] = 1;

        
        int res = 0;
        for (int i = 1; i <= len; ++i) {
            for (int j = 1; j < LEN; ++j) {
                if (STR[j] == line[i]) {
                    for (int k = 0; k < i; ++k) {
                        dp[i][j] += dp[k][j-1];
                    }
                }
                dp[i][j] %= 10000;
            }
            res = (res + dp[i][LEN-1]) % 10000;
        }

        printf("Case #%d: %04d\n", ++c, res);
    }

    return 0;
}
