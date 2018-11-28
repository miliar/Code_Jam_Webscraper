#include <cstdio>
#include <iostream>
#define inf 123456789098765432

using namespace std;

const int MAXN = 40000;
long long f[MAXN], n, tc, d[MAXN], x[MAXN];

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> tc;
    for (int tci = 1; tci <= tc; tci++)
    {
        cin >> n;
        for (int i = 0; i <= n; i++) f[i] = -1;
        for (int i = 0; i < n; i++)
            cin >> x[i] >> d[i];
        cin >> x[n];
        f[0] = x[0];
        for (int i = 0; i < n; i++)
        {
            if (f[i] < 0) break;
            for (int j = i + 1; j <= n; j++)
            {
                if (x[j] > x[i] + f[i]) break;
                f[j] = max(f[j], min(x[j] - x[i], d[j]));
            }
        }
        printf("Case #%d: ", tci);
        if (f[n] >= 0) printf("YES\n"); else printf("NO\n");
    }
    return 0;
}
