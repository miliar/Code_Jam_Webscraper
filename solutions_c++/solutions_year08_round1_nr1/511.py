#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i)
#define FOREACH(it,c) for(typeof((c).begin())it=(c).begin();it!=(c).end();++it)
#define CLR(x) memset((x),0,sizeof((x)))
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
#define MAXN 1000000000
typedef long long LL;

void run() {
    int n;
    cin >> n;
    vector<LL> a(n), b(n);
    REP(i,n) cin >> a[i];
    REP(i,n) cin >> b[i];
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    LL ret = 0;
    REP(i,n) {
        ret += a[i] * b[n - 1 - i];
    }
    cout << ret << endl;
}

int main() {
    int kase;
    cin >> kase;
    for (int k = 1; k <= kase; ++k) {
        cout << "Case #" << k << ": ";
        run();
    }
    return 0;
}
