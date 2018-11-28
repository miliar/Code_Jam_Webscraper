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

const int NMAX = 2100000;
vector<int> ok[NMAX];

int main() {
    #ifdef myproject
    freopen("input.txt", "rt", stdin);
    //freopen("output.txt", "wt", stdout);
    #endif

    int cs[10];
    for1(v, NMAX-1){
        int cnt = 0, cv = v;
        while(cv > 0){
            cs[cnt++] = cv % 10,
            cv /= 10;
        }
        reverse(cs, cs + cnt);

        forn(i, cnt){
            int cur = 0;
            forn(j, cnt){
                int t = i + j;
                if(t >= cnt) t -= cnt;
                cur = cur * 10 + cs[t];
            }
            if(cur > v)
                ok[v].pb(cur);
        }
        sort(all(ok[v]));
        ok[v].erase(unique(all(ok[v])), ok[v].end());
    }

    int testCount = 0;
    scanf("%d", &testCount); char testBuf[10]; gets(testBuf);
    for1(currentTest, testCount){
        printf("Case #%d: ", currentTest);
        //solution
    
        int a, b, ans = 0;
        cin >> a >> b;
        fore(c, a, b+1){
            forn(i, sz(ok[c])){
                if(ok[c][i] > b) break;
                ans++;
            }            
        }

        cout << ans;
//        fprintf(stderr, "Test #%d: %d\n", currentTest, (int)clock());
        puts("");
    }

    return 0;
}


