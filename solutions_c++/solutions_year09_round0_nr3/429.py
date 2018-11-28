#include <cstdio>
#include <cstring>

const char* S = "welcome to code jam";
const int LEN = strlen(S);

char s[505];
int dp[505][100];

int main()
{
    int T;
    scanf("%d", &T);
    getchar();
    for (int cas = 1; cas <= T; cas++)
    {
        gets(s);
        int n = strlen(s);
        memset(dp, 0, sizeof(dp));
        if (s[0] == S[0])
            dp[0][0] = 1;
        for (int i = 1; i < n; i++)
        {
            dp[i][0] = dp[i - 1][0];
            if (s[i] == S[0])
                dp[i][0]++;
            for (int j = 1; j < LEN; j++)
            {
                dp[i][j] = dp[i - 1][j];
                if (s[i] == S[j])
                    dp[i][j] += dp[i - 1][j - 1];
                dp[i][j] %= 10000;
            }
        }
        printf("Case #%d: %04d\n", cas, dp[n - 1][LEN - 1]);
    }
    return 0;
}
