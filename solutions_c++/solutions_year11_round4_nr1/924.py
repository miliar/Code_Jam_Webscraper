#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <numeric>
#include <algorithm>
using namespace std;
#ifdef DEBUGRUN
#define LOG(a) (cerr<<__LINE__<<": "#a" = "<<(a)<<endl)
#define DBG(...) (__VA_ARGS__)
#else
#define LOG(...) ((void)0)
#define DBG(...) ((void)0)
#endif
#define rep(i, n) for(int i=0; i<(int)(n); i++)
#define mp make_pair
#define foreach(it, c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++)
typedef long long Int;
#define INF (MY_INFINITY)
#define MOD (YOUR_MODULUS)

int x, s, r, t, n;
int b[1000], e[1000], w[1000];

void solve() {
    scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
    double T = t;
    r -= s;
    rep(i, n) scanf("%d%d%d", b+i, e+i, w+i);
    vector<pair<int, int> > v;
    LOG(x);
    rep(i, n) x -= e[i]-b[i];
    LOG(x);
    v.push_back(mp(s, x));
    rep(i, n) v.push_back(mp(s+w[i], e[i]-b[i]));
    sort(v.begin(), v.end());
    double ans = 0;
    rep(i, v.size()) {
        const double rv = v[i].first+r;
        const double rt = min(T, (double)v[i].second/rv);
        LOG(v[i].first);
        LOG(v[i].second);
        LOG(ans);
        LOG(T);
        LOG(rt);
        ans += rt + (v[i].second-rv*rt)/v[i].first;
        T -= rt;
    }
    printf("%.8f\n", ans);
}

int main() {
    int T;
    scanf("%d", &T);
    rep(t, T) {
        printf("Case #%d: ", t+1);
        solve();
    }
    return 0;
}



