#include <string>
#include <cstdio>

using namespace std;

const string s = "welcome to code jam";

int N, dp[500][30];
char in[512];

int main()
{
    scanf("%d", &N);
    gets(in);
    int len2 = s.length();
    int cas = 1;
    while (N--) {
        gets(in);
        int len1 = strlen(in);
        memset(dp, 0, sizeof(dp));
        for (int i = 0; i < len1; ++i) 
            if (in[i] == 'w')
                dp[i][0] = 1;
        for (int i = 1; i < len1; ++i) {
            for (int j = 1; j < len2; ++j) {
                if (in[i] == s[j]) {
                    for (int k = 0; k < i; ++k) {
                        dp[i][j] += dp[k][j-1];
                        if (dp[i][j] >= 1000)
                            dp[i][j] -= 1000;
                    }
                }
                else dp[i][j] = 0;
            }
        }
        int ans = 0;
        for (int i = len2-1; i < len1; ++i) {
            ans += dp[i][len2-1];
            if (ans >= 1000)
                ans -= 1000;
        }
        printf("Case #%d: %04d\n", cas++, ans);
    } 
}
