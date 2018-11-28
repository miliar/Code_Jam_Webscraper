#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>

using namespace std;

static const char needle[] = "welcome to code jam";
static const int MOD = 10000;

static int solve(const string &line)
{
    int L = line.size();
    const int LN = strlen(needle);
    int dp[L + 1][LN + 1];

    for (int i = 0; i < LN; i++)
        dp[L][i] = 0;
    dp[L][LN] = 1;

    for (int l = L - 1; l >= 0; l--)
    {
        dp[l][LN] = 1;
        for (int ln = LN - 1; ln >= 0; ln--)
        {
            dp[l][ln] = dp[l + 1][ln];
            if (line[l] == needle[ln])
            {
                dp[l][ln] += dp[l + 1][ln + 1];
                dp[l][ln] %= MOD;
            }
        }
    }

    return dp[0][0];
}

int main()
{
    int N;
    cin >> N >> ws;
    for (int cas = 1; cas <= N; cas++)
    {
        string line;
        getline(cin, line);
        printf("Case #%d: %.4d\n", cas, solve(line));
    }
    return 0;
}
