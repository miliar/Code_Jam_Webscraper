#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
using namespace std;
#define forn(i,n) for(int i=0; i<int(n); i++)
#define forsn(i,s,n) for(int i=(s); i<int(n); i++)
#define dforn(i,n) for(int i = int(n) - 1; i >= 0; i--)
#define forall(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(__typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)
#define all(c) (c).begin(), (c).end()
#define esta(v,c) ((c).find(v) != (c).end())
#define zMem(c) memset((c), 0, sizeof(c))
#define pb push_back
#define x first
#define y second
const int INF = 1000000000;
typedef long long tint;
typedef long double tdbl;
typedef pair<int,int> pint;

int main()
{
	#ifdef ACMTUYO
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int TT; cin >> TT;
    forn(tt, TT) {
        int cn, d, n;
        
        map<pair<char,char>, char> T;
        cin >> cn;
        forn(i, cn) {
            char a, b, c;
            cin >> a >> b >> c;
            T[make_pair(a,b)] = c;
            T[make_pair(b,a)] = c;
        }

        map<char, vector<char> > D;
        cin >> d;
        forn(i, d) {
            char a, b;
            cin >> a >> b;
            D[a].pb(b);
            D[b].pb(a);
        }

        cin >> n;
        cout << "Case #" << tt + 1 << ": [";
        vector<char> res;
        map<char, int> gay;
        forn(i, n) {
            char a; cin >> a;
            if (!res.empty() && esta(make_pair(res.back(), a), T)) {
                gay[res.back()]--;
                gay[res.back() = T[make_pair(res.back(), a)]]++;
            } else {
                bool pasa = false;
                forall(c, D[a]) if(gay[*c] > 0) {
                    gay.clear();
                    res.clear();
                    pasa = true;
                    break;
                }
                if (!pasa) {
                    res.pb(a);
                    gay[a]++;
                }
            }
        }
        forn(i, res.size()) {
            if(i) cout << ", ";
            cout << res[i];
        }
        cout << "]" << endl;
    }
	return 0;
}
