#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 200, INF = 1000000000;
int kase, kases, n, m, t;
int dp[MAXN][MAXN];
vector<int> a;

void f(int x, int y)
{
    int t;
    if (y - x == 1)
    {
        dp[x][y] = 0;
        return;
    }
    dp[x][y] = INF;
    for (int i = x + 1; i <= y - 1; ++i)
    {
        if (dp[x][i] == -1) f(x, i);
        if (dp[i][y] == -1) f(i, y);
        t = dp[x][i] + dp[i][y] + a[y] - a[x] - 2;
        if (dp[x][y] > t) dp[x][y] = t;
    }
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    cin >> kases;
    for (kase = 1; kase <= kases; ++kase)
    {
        cin >> n >> m;
        a.clear();
        a.push_back(0);
        for (int i = 1; i <= m; ++i)
        {
            cin >> t;
            a.push_back(t);
        }
        a.push_back(n + 1);
        sort(a.begin(), a.end());
        memset(dp, 0xff, sizeof(dp));
        f(0, m + 1);
        cout << "Case #" << kase << ": " << dp[0][m + 1] << endl;
    }
    return 0;
}
