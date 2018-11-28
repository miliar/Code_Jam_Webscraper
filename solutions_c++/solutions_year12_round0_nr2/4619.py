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
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>

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

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename T> T abs(T a) { return a < 0 ? -a : a; }
template<typename T> T sqr(T a) { return a*a; }

const int INF = (int)1e9;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

int n;
int a[110];
int p, s;

int z[110][110];

int solve(int idx, int s){
    if(s < 0)
        return -INF;
    if(idx == n)
        return 0;
    if(z[idx][s] == -1){
        int& ans = z[idx][s];
        ans = 0;
        for(int i = 0; i <= 10; ++i)
        for(int j = i; j <= i + 2; ++j)
        for(int k = j; k <= i + 2; ++k){
            if(i + j + k != a[idx])
                continue;
            ans = max(ans, solve(idx + 1, s - ((k - i) == 2)) + (k >= p));
        }
    }

    return z[idx][s];
}

int main(){
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "rt", stdin);
        //freopen("output.txt", "wt", stdout);
    #endif

    int tests;
    cin >> tests;

    forn(test, tests){
        cin >> n >> s >> p;

        forn(i, n)
            cin >> a[i];

        memset(z, -1, sizeof(z));

        printf("Case #%d: %d\n", test + 1, solve(0, s));
    }

    return 0;
}
