#include <cstdio>
#include <iostream>

using namespace std;

int a[1001][11], f[1001], b[1001], k = 0;

bool dfs(int i) {
    if (f[i] == k) return true;
    f[i] = k;
    for (int j = 1; j <= a[i][0]; j++)
        if (dfs(a[i][j]))
            return true;
    return false;
}

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        int n;
        cin >> n;
        for (int i = 1; i <= n; i++) {
            cin >> a[i][0];
            for (int j = 1; j <= a[i][0]; j++) {
                cin >> a[i][j];
                b[a[i][j]] = t;
            }
        }
        bool f = true;
        for (int i = 1; i <= n; i++)
            if (b[i] != t) {
                k++;
                if (dfs(i)) {
                    cout << "Yes" << endl;
                    f = false;
                    break;
                }
            }
        if (f) cout << "No" << endl;
    }
    return 0;
}
