#include <cstdio>
#include <iostream>

using namespace std;

int a[10010], d[10010], l[10010];

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int T;
    cin >> T;
    for (int CT = 1; CT <= T; CT++) {
        cout << "Case #" << CT << ": ";
        int n;
        cin >> n;
        for (int i = 0; i < n; i++)
            cin >> d[i] >> l[i];
        cin >> d[n];
        a[0] = d[0];
        for (int i = 1; i <= n; i++) {
            a[i] = -1;
            for (int j = 0; j < i; j++)
                if (d[j] + a[j] >= d[i])
                    a[i] = max(a[i], d[i] - d[j]);
            a[i] = min(a[i], l[i]);
        }
        if (a[n] >= 0) cout << "YES";
            else cout << "NO";
        cout << endl;
    }
    return 0;
}
