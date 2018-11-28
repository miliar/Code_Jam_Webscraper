#include <cstdio>
#include <cstring>

const char *str = "welcome to code jam";

int dp[20][501];
bool used[20][501];
char line[501];

int main() {
    int caseSize;
    scanf("%d\n", &caseSize);
    for (int i = 0; i < caseSize; i++) {
        gets(line);
        int len = strlen(line);
        memset(dp, 0, sizeof(dp));
        memset(used, false, sizeof(used));
        dp[0][0] = 1;
        used[0][0] = true;
        for (int j = 0; j < 19; j++) {
            for (int k = 0; k < len; k++)
                if (used[j][k]) {
                    for (int l = k + 1; l <= len; l++)
                        if (line[l - 1] == str[j]) {
                            dp[j + 1][l] = (dp[j + 1][l] + dp[j][k]) % 10000;
                            used[j + 1][l] = true;
                        }
                }
        }
        int result = 0;
        for (int j = 0; j <= len; j++)
            if (used[19][j]) result = (result + dp[19][j]) % 10000;
        printf("Case #%d: %04d\n", i + 1, result);
    }
}
