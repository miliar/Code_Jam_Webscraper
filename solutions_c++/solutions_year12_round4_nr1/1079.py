#include <algorithm>
#include <cmath>
#include <cstring>
#include <cctype>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define VAR(a,b)        __typeof(b) a=(b)
#define REP(i,n)        for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b)      for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b)     for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c)   for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(c)          (c).begin(),(c).end()
#define TRACE(x)        cerr << "TRACE(" #x ")" << endl;
#define DEBUG(x)        cerr << #x << " = " << x << endl;

typedef long long               ll;
typedef long double             ld;
typedef unsigned long           ulong;
typedef unsigned long long      ull;

pair<ll, ll> v[11234];

pair<ll, ll> dp[11234];

ll ok(int k, int n, ll d) {
    if (d < 0)
        return -1;
    if (dp[k].first != 0 && dp[k].first >= d)
        return dp[k].second;
    //printf("called %d, %d\n", k, d);
    ll m = v[k].first+d;
    ll res = m;
    FOR(j,k+1,n-1) {
        if (v[j].first > m)
            break;
        res = max(res, ok(j,n,min(min(d, v[j].second),v[j].first-v[k].first)));
    }
    dp[k].first = d;
    return dp[k].second = res;
}

int main() {
    //freopen(stdin,  "input",  "r");
    //freopen(stdout, "output", "w");
    int tnum;
    scanf("%d", &tnum);
    FOR(ti,1,tnum) {
        ll D, N;
        printf("Case #%d: ", ti);
        scanf("%lld", &N);
        REP(i,N)
            scanf("%lld%lld", &v[i].first, &v[i].second);
        scanf("%lld", &D);
        memset(dp, 0, sizeof(dp));
        //cerr << ok(0,N,min(v[0].second, v[0].first)) << endl;
        if (ok(0,N,min(v[0].second, v[0].first)) >= D)
            puts("YES");
        else
            puts("NO");
    }
    return 0;
}
