#include <cstdio>
#include <iostream>

using namespace std;

typedef long long ll;

int h[2010], a[2010][2010], b[2010], n;

ll fndy(ll dx, ll dy, ll ndx) {
    ll l = 0, r = 1000000000;
    while (l < r) {
        ll c = (l+r)/2;
        if (c*dx>dy*ndx) r = c; else l = c+1;
    }
    return l;
}

bool rec(int i, int l, int dx, int dy) {
    for (int j = 0; j < b[i]; j++) {
        int nl = a[i][j];
        if (nl < l) return true;
        dy = fndy(dx, dy, i - nl);
        dx = i - nl;
        h[nl] = h[i] - dy;
        if (rec(nl, l, dx, dy)) return true;
        l = nl;
    }
    return false;
}

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        cout << "Case #" << T << ":";
        cin >> n;
        for (int i = 1; i <= n; i++) {
            b[i] = 0;
            h[i] = -1;
        }
        for (int i = 1; i < n; i++) {
            int t;
            cin >> t;
            a[t][b[t]++] = i;
        }
        h[n] = 1000000000;
        if (rec(n, 0, 1, 0)) cout << " Impossible"; else {
            for (int i = 1; i <= n; i++) {
                cout << ' ' << h[i];
                if (h[i]<0) return 1;
            }
        }
        cout << endl;
    }
    return 0;
}
