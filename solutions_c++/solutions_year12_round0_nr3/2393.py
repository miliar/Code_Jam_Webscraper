#include <iostream>
#include <cstdio>

using namespace std;
typedef long long ll;

bool f[2000001];

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int a, b;
        cin >> a >> b;
        for (int i = a; i <= b; i++) f[i] = true;
        ll ans = 0;
        for (int i = a; i <= b; i++) if (f[i]) {
            int j = 1, v = i;
            ll t = 0;
            while (j <= i) j *= 10;
            j /= 10;
            do {
                v = v/10 + j*(v%10);
                if ((v / j) && (a <= v) && (v <= b)) {
                    t++;
                    f[v] = false;
                }
            } while (v != i);
            ans += (t*(t-1))/2;
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
