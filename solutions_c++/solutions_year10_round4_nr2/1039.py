/*
 * solution.cpp
 *
 *  Created on: 05.06.2010
 *      Author: pakso
 */

#include <iostream>
#include <vector>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); i++)

vector<int> m;
int ans;

void calc(int l, int r, int c) {
    int m1 = 0, m2 = 0;
    if (l + 1 == r) {
        if (m[l] - c == 1) {
            ans++;
        }
        return;
    }
    for(int i = l; i < (r + l) / 2; i++) {
        m1 = max(m1, m[i] - c);
    }
    for(int i = (l+r)/2; i < r; i++) {
        m2 = max(m2, m[i] - c);
    }

    if (m1 == 0 && m2 == 0) {
        return;
    }
    c++;
    ans++;
        calc(l, (l+r)/2, c);
    
        calc((l+r)/2, r, c);
}

int a[10232];

void solve(int tc) {
    printf("Case #%d: ", tc);
    int p; cin >> p;
//    cout << "P" << p << endl;
    m.resize(1 << p);
    forn(i, 1 << p) cin >> m[i];
    forn(i, 1 << p) m[i] = p - m[i];
//    forn(i, 1 << p) cout << m[i] << ',';
//    cout << endl;
    for(int i = p-1; i >= 0; i--) {
        forn(j, 1 << i) cin >> a[j];
    }
//    forn(i, 1 << p) cout << m[i] << endl;
    ans = 0;
    calc(0, 1 << p, 0);
    cout << ans << endl;
}

int main() {
    freopen("input.txt", "rt", stdin);
    int tc;
    cin >> tc;
    forn(i, tc) solve(i+1);
    return 0;
}
                  