#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdio>
#include <iomanip>

using namespace std;

typedef long long LL;
typedef pair<LL, int> PLLI;

void solve(int T) {
    int r, k, n;
    cin >> r >> k >> n;
    vector<int> g(n);
    for(int i=0; i<n; i++)
        cin >> g[i];
    vector<vector<PLLI> > a(100, vector<PLLI>(n, make_pair(0, 0)));
    for(int i=0; i<n; i++) {
        LL s = 0;
        int x = 0;
        while(s <= k) {
            s += g[(i+x)%n];
            x++;
            if (x == n+1)
                break;
        }
        s -= g[(i+x-1)%n];
        a[1][i] = make_pair(s, (i+x-1)%n);
    }
//    for(int i=0; i<n; i++)
//        cout << a[1][i].first << "," << a[1][i].second << " "; cout << endl;
    for(int i=2; i<40; i++) {
        for(int j=0; j<n; j++) {
            a[i][j].first = a[i-1][j].first + a[i-1][a[i-1][j].second].first;
            a[i][j].second = a[i-1][a[i-1][j].second].second;
        }
    }
    int d = r;
    int l = 1;
    int cs = 0;
    LL count = 0;
    while(d) {
        int t = d%2;
        d /= 2;
        if (t) {
            count += a[l][cs].first;
            cs = a[l][cs].second;
        }
        l++;
    }
    cout << "Case #" << T << ": " << count << endl;
}

int main() {
    //freopen("in.txt", "r", stdin);
    freopen("C-large.in", "r", stdin);
    freopen("result.out", "w", stdout);
    cin.sync_with_stdio(false);
    int T;
    cin >> T;
    for(int t=0; t<T; t++)
        solve(t+1);
    return 0;
}
