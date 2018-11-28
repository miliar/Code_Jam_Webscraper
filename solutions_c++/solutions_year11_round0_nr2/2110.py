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
#define all(a) (a).begin(),(a).end()
#define UNIQUE(a) sort(all(a)),(a).resize(unique(all(a))-(a).begin())
#define sz(a) ((int) (a).size())
#define pb push_back

#define X first
#define Y second

typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef long long ll;

char C[26][26];
bool D[26][26];

int main() {
#ifdef LOCAL
	freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
#endif
    int test;
    cin >> test;
    FOR (ntest, 1, test + 1) {
        memset (C, -1, sizeof (C));
        memset (D, 0, sizeof (D));
        int c;
        cin >> c;
        string s;
        REP (i, c) {
            cin >> s;
            C[s[0]-'A'][s[1]-'A'] = s[2]-'A';            
            C[s[1]-'A'][s[0]-'A'] = s[2]-'A';            
        }
        int d;
        cin >> d;
        REP (i, d) {
            cin >> s;
            D[s[0]-'A'][s[1]-'A'] = true;
            D[s[1]-'A'][s[0]-'A'] = true;
        }
        
        int tmp;
        cin >> tmp;
        cin >> s;
        vector<int> a;
        REP (i, sz (s)) {
            int x = s[i]-'A';
            if (sz(a) && C[x][a.back()] != -1) {
                int bb = a.back();
                a.pop_back();
                a.pb(C[x][bb]);
                continue;
            }
            bool added = false;
            REP (i, sz (a))
                if (D[x][a[i]]) {
                    a.clear();
                    added = true;
                    break;
                }
            if (!added)
                a.pb(x);
        }
        cout << "Case #" << ntest << ": [";
        REP (i, sz (a)) {
            if (i)
                cout << ", ";
            cout << char(a[i]+'A');            
        }
        cout << "]\n";
    }
	return 0;
}
