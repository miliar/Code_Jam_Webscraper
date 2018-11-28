#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

int t[10005], tt[10005], e[10005];

bool check(int ans)
{
    memmove(t, tt, sizeof(t));
    memset(e, 0, sizeof(e));
    for (int i = 1; i <= 10000; ++i)
        while (t[i]) {
            bool ok = true;
            for (int j = 0; j < ans; ++j)
                if (!t[i + j]) {
                    ok = false;
                    break;
                }
            if (ok) {
                for (int j = 0; j < ans; ++j)
                    --t[i + j];
                ++e[i + ans];
            }else {
                if (!e[i]) return false;
                --e[i];
                int j = i;
                while (t[j]) {
                    --t[j];
                    ++j;
                }
                ++e[j];
            }
        }
    return true;
}

int main()
{
    freopen("b1.in", "r", stdin);
    freopen("b1.out", "w", stdout);
    
    int t1;
    cin >> t1;
    for (int t2 = 1; t2 <= t1; ++t2) {
        int n;
        cin >> n;
        memset(t, 0, sizeof(t));
        for (int i = 1; i <= n; ++i) {
            int x;
            cin >> x;
            ++t[x];
        }
        memmove(tt, t, sizeof(t));
        for (int ans = n; ans >= 0; --ans)
            if (!ans || check(ans)) {
                cout << "Case #" << t2 << ": " << ans << endl;
                break;
            }
    }
    
    return 0;
}
