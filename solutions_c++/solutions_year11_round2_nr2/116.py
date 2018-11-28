#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <iomanip>
#include <cassert>
#include <cstring>
using namespace std;

typedef long long LL ;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;

const LL INF = 1000000000000000LL;
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

#define MAXN 203
LL t[MAXN];
LL d[MAXN];

bool check(LL m, LL n, LL k) {
    LL x = -INF;
    for (int i = 0; i < n; i++) {
        LL last = max(t[i] - m, x);
        x = last + d[i] * k;
        LL prev = x - k;
        if (t[i] + m < prev) return false;
        //if (m <= 8) cout << i << ' ' << m << " " << t[i] << ' ' << d[i] << ' ' << x << endl;
    }
    return true;
}

LL solve() {
    LL n, k;
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        LL a, b;
        cin >> a >> b;
        t[i] = 2 * a;
        d[i] = b;
    }
    LL p = 0;
    LL q = INF;
    while (p < q) {
        LL m = (p + q) / 2;
        if (check(m, n, 2 * k)) {
            q = m;
        }
        else p = m + 1;
    }
    return p;
}

int main()
{
    ios_base::sync_with_stdio(0) ;
    int te;
    cin >> te;
    for (int u = 1; u <= te; u++) {
        LL ret = solve();
        cout << "Case #" << u << ": ";
        cout << ret / 2;
        if (ret % 2) cout << ".5";
        cout << "\n";
    }
}

