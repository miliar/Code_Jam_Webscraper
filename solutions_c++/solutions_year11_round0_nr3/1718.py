#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cassert>
#include <cstring>
using namespace std;

typedef long long LL ;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;

const int INF = 1000*1000*1000 + 1000;
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

LL solve() {
    int n;
    cin >> n;
    int mi = INF;
    LL sum = 0;
    int x = 0;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        x ^= a;
        mi = min(mi, a);
        sum += a;
    }
    if (x) return -1;
    return sum - mi;
}

int main()
{
    ios_base::sync_with_stdio(0) ;
    int te;
    cin >> te;
    for (int u = 1; u <= te; u++) {
        LL ret = solve();
        cout << "Case #" << u << ": ";
        if (ret < 0) cout << "NO";
        else cout << ret;
        cout << "\n";
    }
}

