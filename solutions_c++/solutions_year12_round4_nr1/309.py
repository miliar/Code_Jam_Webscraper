
// Tomasz Kulczynski
#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <numeric>
using namespace std;

#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long LL;
typedef double D;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for (int i=0;i<(n);++i)
#define FOR(i,a,b) for (VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(e,v) for(VAR(e,(v).begin());e!=(v).end();++e)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)(a).size())
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))

bool brut(int n, int dd, VI d, VI l) {
    d.PB(dd);
    l.PB(0);
    VI w(n+1, -1);
    w[0] = d[0];
    REP(i, n) if(w[i] >= 0) {
        w[i] = min(w[i], l[i]);
        FOR(j, i+1, n) if(d[i] + w[i] >= d[j])
            w[j] = max(w[j], d[j] - d[i]);
    }
    return w[n] >= 0;
}

bool rozw(int n, int dd, VI d, VI l) {
    d.PB(dd);
    l.PB(0);
    VI w(n+1, -1);
    vector<PII> st;
    st.PB(MP(d[0], 0));
    REP(i, n+1) {
        w[i] = lower_bound(ALL(st), MP(d[i], 0)) - st.begin();
        if(w[i] == SIZE(st)) {
            w[i] = -1;
            continue;
        }
        w[i] = min(l[i], d[i] - st[w[i]].Y);
        if(!st.empty() && st.back().X >= d[i] + w[i])
            continue;
        st.PB(MP(d[i] + w[i], d[i]));
    }
    return w[n] >= 0;
}

int main() {
    int tt;
    scanf("%d",&tt);
    FOR(cas, 1, tt) {
        int n, DD;
        scanf("%d",&n);
        VI d(n), l(n);
        REP(i, n) scanf("%d %d",&d[i],&l[i]);
        scanf("%d",&DD);
        printf("Case #%d: %s\n", cas, brut(n, DD, d, l) ? "YES" : "NO");
    }
    return 0;
}
