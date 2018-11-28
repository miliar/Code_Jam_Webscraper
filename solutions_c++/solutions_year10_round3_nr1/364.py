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

    int ts;
    scanf("%d", &ts);
    forn(qq, ts){
        printf("Case #%d: ", qq + 1);

        int n;
        scanf("%d", &n);
        vector<pt> a(n);
        forn(i, n)
            scanf("%d%d", &a[i].X, &a[i].Y);


        sort(all(a));

        int ans = 0;

        forn(i, sz(a)){
            forn(j, i){
                if(a[j].Y > a[i].Y)
                    ans++;
            }
        }

        printf("%d\n", ans);
    }

    return 0;
}





















