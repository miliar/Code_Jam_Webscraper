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
#include <bitset>
#include <ext/hash_map>
#include <ext/hash_set>

using namespace std;
using namespace __gnu_cxx;

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

const int mod = 1000000009;

int n;
VVI adj;

ll ans;
bool zero;
int k;
int d2[512];
int d1[512];
int p[512];

void rec (int q, int prev)
{
    d1[q] = d2[q] = 0;    
    p[q] = prev;
    
    REP (i, SZ (adj[q]))
    if (adj[q][i] != prev)
    {
        d1[q]++;
        rec (adj[q][i], q);
        d2[q] += d1[adj[q][i]];
    }
}

int main() {
//	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-large.in", "r", stdin);
//	freopen("C-small-attempt0.out", "w", stdout);
	freopen("C-large.out", "w", stdout);
	
    int ntest;
    cin >> ntest;
    REP (test, ntest)
    {
        cout << "Case #" << (test+1) << ": ";
        
        cin >> n >> k;        
        adj.clear();
        adj.resize (n);
        
        REP (i, n-1)
        {
            int q, w;
            cin >> q >> w;
            --q, --w;
            adj[q].pb (w);
            adj[w].pb (q);
        }
      
        zero = false;
        ans = 1;  
        rec (0, -1);
        
        REP (i, n)
        {
            int d = k;
            
            if (p[i] != -1)
            {
                d--;
                d = d - d1[p[i]] + 1;
                if (p[p[i]] != -1)
                {
                    d--;
                }                
            }                
            
            if (d < d1[i])
            {
                ans = 0;
                break;
            }
            
//            cout << i << ' ' << d << endl;
            REP (j, d1[i])
            {
                ans = ans * (d - j);
                ans %= mod;
            }
        }
        
        cout << ans << endl;
    }
	return 0;
}
