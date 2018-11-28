#include <iostream>
using namespace std;

int R, K, n;
int g[1005];
long long CY, TI;
long long ans;

int main(void)
{
    int i, j, k, t;
    int ca;
    int c = 0;
    bool vi[1005];
    bool is[1005];
    cin >> ca;
    while (ca--)
    {
        cin >> R >> K >> n;
        for (i = 0; i < n; i++) cin >> g[i];
        memset(is, 0, sizeof(is));
        is[0] = 1;
        ans = 0;
        i = 0;
        while (R)
        {
            memset(vi, 0, sizeof(vi));
            k = K;
            while (1)
            {
                if (vi[i] || k - g[i] < 0) break;
                ans += g[i], k -= g[i], vi[i] = 1, i = (i + 1) % n;
            }
            R--;
            if (is[i]) break;
            else is[i] = 1;
        }
        t = i;
        CY = TI = 0;
        memset(is, 0, sizeof(is));
        is[t] = 1;
        i = t;
        while (1)
        {
            memset(vi, 0, sizeof(vi));
            k = K;
            while (1)
            {
                if (vi[i] || k - g[i] < 0) break;
                CY += g[i], k -= g[i], vi[i] = 1, i = (i + 1) % n;
            }
            TI++;
            if (is[i]) break;
            else is[i] = 1;
        }
        ans += (R / TI) * CY;
        R %= TI;
        i = t;
        while (R)
        {
            memset(vi, 0, sizeof(vi));
            k = K; R--;
            while (1)
            {
                if (vi[i] || k - g[i] < 0) break;
                ans += g[i], k -= g[i], vi[i] = 1, i = (i + 1) % n;
            }
        }
        cout << "Case #" << ++c << ": " << ans << endl;
    }
    return 0;
}
