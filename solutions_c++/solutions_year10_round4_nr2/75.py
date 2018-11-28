#include <iostream>
using namespace std;


int p, n;
long long f[5000][12];

int main()
{
    freopen("b2.in", "r", stdin);
    freopen("b2.out", "w", stdout);

    int t2; cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        cin >> p;
        n = 1 << p;
        memset(f, 1, sizeof(f));
        for (int i = n; i < n + n; ++i) {
            int x; cin >> x;
            for (int j = 0; j <= p; ++j)
                f[i][j] = j <= x ? 0 : int(11e8);
        }
        for (int h = p; h; --h)
            for (int i = 1 << (h - 1); i < 1 << h; ++i) {
                int l = i * 2, r = l + 1, x;
                cin >> x;
                for (int j = 0; j <= p; ++j)
                    f[i][j] = min(f[l][j] + f[r][j] + x, f[l][j + 1] + f[r][j + 1]);
            }
        printf("Case #%d: ", t1);
        cout << f[1][0] << endl;
        
    }

    return 0;
}
