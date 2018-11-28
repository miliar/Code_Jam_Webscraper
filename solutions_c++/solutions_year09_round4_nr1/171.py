#include <iostream>
#include <cmath>
#include <cstring>
#include <cstdio>

using namespace std;

const int MAXN = 100, INF = 100000000;
int a[MAXN][MAXN], b[MAXN];
int n, kase, kases, res, tot;
char ch;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> kases;
    for (int kase = 1; kase <= kases; ++kase)
    {
        cin >> n;
        memset(b, 0, sizeof(b));
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= n; ++j)
            {
                cin >> ch;
                a[i][j] = (ch == '1');
                if (a[i][j]) b[i] = j;
            }
        res = 0;
        for (int i = 1; i <= n; ++i)
            for (int j = i; j <= n; ++j)
                if (b[j] <= i)
                {
                    res += j - i;
                    for (int k = j - 1; k >= i; --k)
                        swap(b[k], b[k + 1]);
                    break;
                }
        cout << "Case #" << kase << ": " << res << endl;
    }
    return 0;
}
