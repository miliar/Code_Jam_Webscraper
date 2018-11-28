#pragma comment(linker, "/STACK:10000000")

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
#include <utility>
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
#define iter(i, v) for(typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)

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

const int NMAX = (int)1E3 + 7;

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int test;
    scanf("%d", &test);
    for1(Q, test){
        printf("Case #%d: ", Q);

        int R, K, n;
        scanf("%d%d%d", &R, &K, &n);
        vector<li> g(n), used(n, 0), cost(n, -1), idx(n, -1), to(n, -1), curcost(n, -1);
        forn(i, n)
            scanf("%d", &g[i]);

        int start = 0, cur = 0;
        li ans = 0;

        while(!used[start]){
            used[start] = true, cost[start] = ans, idx[start] = cur;

            li sum = 0;
            int i = start;
            while(sum + g[i] <= K){
                sum += g[i];
                i++;
                i %= n;

                if(i == start) break;
            }
            to[start] = i;
            curcost[start] = sum;
            start = i;

            cur++;
            ans += sum;

            if(cur == R) break;
        }


        if(cur == R){
            cout << ans << endl;
            continue;
        }

        li incicle = ans - cost[start], leng = cur - idx[start], cnt = (R - cur) / leng, ost = (R - cur) % leng;
    
        ans += li(cnt) * incicle;
        int now = start;
        forn(i, ost){
            ans += curcost[now];
            now = to[now];
        }

        cout << ans << endl;
    }

    return 0;
}





















