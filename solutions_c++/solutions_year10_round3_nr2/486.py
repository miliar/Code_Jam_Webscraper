#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
#include <string>

#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <iostream>
#include <iomanip>

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

#define sqr(a) ((a) * (a))
#define abs(a) ((a) < 0 ? -(a) : (a))
#define debug(x) {cerr << #x << " = " << x << endl;}

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;
#define X first
#define Y second

const int INF = (int)1e9;                                                                       
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

int c;

int z[1010][1010];
int p[1010][1010];

int solve(int lf, int rg){
    if(lf >= rg)
        return INF;

    if(lf * c >= rg)
        return 0;

    if(z[lf][rg] == -1){                                         
        z[lf][rg] = INF;

        int mid = rg / c;

        for(int i = max(lf + 1, mid - 100); i <= min(rg - 1, mid + 100); ++i){
            if(z[lf][rg] >= max(solve(lf, i), solve(i, rg)) + 1){
                z[lf][rg] = max(solve(lf, i), solve(i, rg)) + 1;
                p[lf][rg] = i;
            }
        }

        mid = lf * c;

        for(int i = max(lf + 1, mid - 100); i <= min(rg - 1, mid + 100); ++i){
            if(z[lf][rg] >= max(solve(lf, i), solve(i, rg)) + 1){
                z[lf][rg] = max(solve(lf, i), solve(i, rg)) + 1;
                p[lf][rg] = i;
            }
        }
    }

    return z[lf][rg];
}

int main(){
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int t;
    cin >> t;

    for1(q, t){
        int lf, rg;
        scanf("%d%d%d", &lf, &rg, &c);

        memset(z, -1, sizeof(z));

        printf("Case #%d: %d\n", q, solve(lf, rg));
    }
    
    return 0;
}
