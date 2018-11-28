#include <iostream>
#include <string>

using namespace std;

int kases, kase, n, m, res;
int dp[1000][100];
string a, b;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    cin >> kases;
    b = "welcome to code jam";
    m = b.size();
    for (int kase = 0; kase != kases; ++kase)
    {
        getline(cin, a);
        if (a == "") getline(cin, a);
        n = a.size();

        memset(dp, 0, sizeof(dp));
        if (a[0] == b[0]) dp[0][0] = 1;
        for (int i = 1; i != n; ++i)
            dp[i][0] = (dp[i - 1][0] + (a[i] == b[0])) % 10000;

        for (int j = 1; j != m; ++j)
            for (int i = j; i < n; ++i)
            {
                dp[i][j] = dp[i - 1][j];
                if (a[i] == b[j]) dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % 10000;
            }

        cout << "Case #" << kase + 1 << ": ";
        res = dp[n - 1][m - 1];
        if (res < 1000) cout << 0;
        if (res < 100) cout << 0;
        if (res < 10) cout << 0;
        cout << res << endl;
    }
    return 0;
}
