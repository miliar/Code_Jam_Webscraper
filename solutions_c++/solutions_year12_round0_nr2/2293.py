#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define debug(x) {cerr << #x << " = " << x << endl;}
template<typename T> inline T abs(T a){ return ((a < 0) ? -a : a); }
template<typename T> inline T sqr(T a){ return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = (int)1E9 + 7;
const ld EPS = 1E-9;
const ld PI = 3.1415926535897932384626433832795;

vector<pt> ok[40]; 

int main() {
    #ifdef myproject
    freopen("input.txt", "rt", stdin);
    //freopen("output.txt", "wt", stdout);
    #endif

    forn(i, 32)
        forn(j, 32){
            if(abs(j-i) > 2) continue;
            forn(k, 32){
                if(abs(i-k) > 2 || abs(j-k) > 2) continue;
                if(i+j+k > 30) continue;

                int maxv = max(max(i, j), k);
                int surp = abs(i-j) == 2 || abs(i-k) == 2 || abs(j-k) == 2;
                ok[i+j+k].pb(mp(surp, maxv));
            }
        }
    forn(i, 32){
        sort(all(ok[i]));
        ok[i].erase(unique(all(ok[i])), ok[i].end());
    }

    int testCount = 0;
    scanf("%d", &testCount); char testBuf[10]; gets(testBuf);
    for1(currentTest, testCount){
        printf("Case #%d: ", currentTest);
        //solution

        int n, s, p;
        cin >> n >> s >> p;
        vector<int> t(n);
        forn(i, n)
            cin >> t[i];

        vector<vector<int> > d(n+1, vector<int>(s+1, 0));
        forn(i, n){
            forn(cs, s+1){
                forn(k, sz(ok[t[i]])){
                    int ncs = cs + ok[t[i]][k].X,
                        nval = d[i][cs] + int(ok[t[i]][k].Y >= p);
                    if(ncs <= s)
                        d[i + 1][ncs] = max(d[i + 1][ncs], nval);
                }                
            }
        }

        cout << d[n][s];
//        fprintf(stderr, "Test #%d: %d\n", currentTest, (int)clock());
        puts("");
    }

    return 0;
}


