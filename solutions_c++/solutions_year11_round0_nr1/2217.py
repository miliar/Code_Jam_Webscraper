#include <iostream>
#include <bitset>
#include <cstdio>
#include <sstream>
#include <vector>
#include <stack>
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
#define ALL(a) (a).begin(),(a).end()
#define UNIQUE(a) sort(ALL(a)),(a).resize(unique(ALL(a))-(a).begin())
#define sz(a) ((int) (a).size())
#define pb push_back

#define X first
#define Y second

typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef long long ll;

char ss[128128];

int main() {
#ifdef LOCAL
	freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif
    int T;
    cin >> T;
    FOR (test, 1, T+1) {
        char c;
        int u;
        vector<int> d[2];
        int kk;
        cin >> kk;
        vector<int> hihi;
        while (kk--) {
            cin >> c >> u;
            if (c == 'O') {
                d[0].pb(u);
                hihi.pb(0);
            }
            else {
                d[1].pb(u);
                hihi.pb(1);
            }
        }
        int q = 0, w = 0;
        int res = 0;
        int p[2] = {1, 1};
        reverse(ALL(hihi));
        while (sz(hihi)) {
            bool push = false;
            if (q < sz(d[0])) {
                if (p[0] == d[0][q]) {
                    if (hihi.back() == 0) {
                        hihi.pop_back();
                        ++q;
                        push = true;
                    }
                } else {
                    if (p[0] < d[0][q]) p[0]++; else p[0]--;
                }                
            }  
            if (w < sz(d[1])) {
                if (p[1] == d[1][w]) {
                    if (!push && hihi.back() == 1) {
                        hihi.pop_back();
                        ++w;                        
                    }                    
                } else {
                    if (p[1] < d[1][w]) p[1]++; else p[1]--;                                        
                }
            }                             
            ++res;
        }
        cout << "Case #" << test << ": " << res << endl;
    }
	return 0;
}
