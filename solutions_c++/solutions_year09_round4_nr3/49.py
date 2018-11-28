#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cmath>
#include <list>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b(b);i<_b;++i)
#define FORD(i,a,b) for(int i=(a),_b(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(),a.end()
#define SORT(a) sort(ALL(a))
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
#define SZ(a) ((int) a.size())
#define pb push_back

#define VAR(a,b) __typeof(b) a=(b)
#define FORE(it,a) for(VAR(it,(a).begin());it!=(a).end();it++)
#define X first
#define Y second
#define DEBUG(x) cout << #x << " = " << x << endl;

#define INF 1000000000

typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long ll;

int a[128][128];


struct pm {
    int n, m;
    VVI adj;
    VI rev;

    void add_pair(int q, int w) {
        adj[q].pb(w+n);
    }    
    
    int solve() {
        int res = 0;
        while (true) {
            VI st;
            VI p(n + m, -1);
            vector<bool> b(n + m);
            int cr = 0;
            int f = -1;
            REP(i, n) if (rev[i] == -1 && !b[i]) {
                st.pb(i);
                b[i] = true;
                for(; cr < SZ(st); ++cr) {
                    int j = st[cr];
                    if (j >= n) {
                        if (rev[j] == -1) { f = j; goto augment; }
                        if (!b[rev[j]]) {b[rev[j]] = true; p[rev[j]] = j; st.pb(rev[j]); }
                    } else {
                        REP(k, SZ(adj[j])) {                            
                            int t = adj[j][k];
                            if (!b[t] && rev[t] != j) { b[t] = true; p[t] = j; st.pb(t); }
                        }
                    }
                }                             
            }               
augment:    
            if (f == -1) break;
            ++res;
            while (f != -1) {
                rev[p[f]] = f;
                rev[f] = p[f];
                f = p[p[f]];
            }
        }
        return res;
    }
    
    pm(int n, int m) : n(n), m(m) {
        adj.resize(n);
        rev.resize(n+m, -1);            
    }       
};
int main() {
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test;
    cin >> test;
    FOR (ntest, 1, test+1)
    {
        int n, k;
        cin >> n >> k;
        REP (i, n)
            REP (j, k)
                cin >> a[i][j];
        pm res(n, n);
        REP (i, n)
            REP (j, n)
                if (a[i][0] > a[j][0])
                {
                    bool ok = true;
                    REP (q, k)
                        if (a[i][q] <= a[j][q])
                        {
                            ok = false;
                            break;
                        }
                    if (ok)
                        res.add_pair (i, j);
                }
        cout << "Case #" << ntest << ": " << (n-res.solve()) << endl;
    }
	return 0;
}
