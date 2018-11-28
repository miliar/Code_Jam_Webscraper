#include <iostream>
#include <algorithm>

using namespace std;

const int mod = 100003;

long long c[512][512];
long long d[512][512];

int solve(int n, int m)
{
    if (d[n][m])
        return d[n][m];

    int res = !(m-1);
    for (int x = 1; x < m; x++)
        res += solve(m, x) * c[n-m-1][m-x-1] % mod;
    return d[n][m] = res % mod;
}

int main()
{
    for (int i=0; i<512; i++)
    {
        c[i][0] = 1;
        for (int j=1; j<=i; j++)
            c[i][j] = (c[i-1][j] + c[i-1][j-1]) % mod;
    }

    int t;
    cin >> t;
    for (int tt = 1; tt<=t; tt++)
    {
        int n;
        cin >> n;

        int ans = 0;
        for (int k = 1; k < n; k++)
            ans += solve(n, k);
            
        cout << "Case #" << tt << ": " << ans%mod << endl;
    }
    return 0;
}
