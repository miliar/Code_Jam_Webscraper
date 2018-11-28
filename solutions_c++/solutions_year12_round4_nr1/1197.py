#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define pb push_back
#define mp make_pair

#define ALL(x) (x).begin(),(x).end()
#define CLR(a,b) memset(a,b,sizeof(a))
#define REPN(x,a,b) for (int x=a; x<b;++x)
#define REP(x,b) REPN(x, 0, b)

#define dbg(x) cout << #x << " = " << x << endl;
#define dbg2(x, y) cout << #x << " = " << x << "  " << #y << " = " << y << endl;
#define dbg3(x, y, z) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << endl;
#define dbg4(x, y, z, w) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << "  " << #w << " = " << w <<  endl;

int d[10005], sz[10005], pode[10005];

int main() {
    int T;
    cin >> T;
    REP(tc, T) {
        int n, D;
        cin >> n;
        REP(i, n) cin >> d[i] >> sz[i];
        cin >> D;
        CLR(pode, -1);
        pode[0] = d[0];
        bool res = 0;
        for (int i = 0; i < n; i++) {
            if (pode[i] == -1) break;
            if (d[i] + pode[i] >= D) { res = 1; break; }
            for (int j = i+1; j < n; j++) {
                if (d[i] + pode[i] < d[j]) break;
                pode[j] = max(min(d[j]-d[i], sz[j]), pode[j]);
            }
        }
        if (res) printf("Case #%d: YES\n", tc+1);
        else printf("Case #%d: NO\n", tc+1);
    }
    return 0;
}
