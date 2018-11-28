#pragma comment(linker, "/stack:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <algorithm>
#include <iostream>
#include <cassert>
#include <iomanip>
#include <climits>
#include <utility>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <bitset>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forn1(i, n) for (int i = 1; i <= int(n); i++)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define debug(x) cerr << #x << " = " << x << endl;
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define X first
#define Y second
#define sc second

using namespace std;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;
typedef pair<ld, ld> ptd;
typedef unsigned char byte;
typedef vector<vector<int> > matrix;

const int INF = INT_MAX / 2;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int N = 1000 + 13;

struct seg
{
    int ft, sc, w;
    
    seg(int ft = 0, int sc = 0, int w = 0): ft(ft), sc(sc), w(w) { }
};

inline bool cmp(const seg& a, const seg& b)
{
    return a.w < b.w;
}

seg a[N];

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int testCnt;
    
    cin >> testCnt;
    
    forn(test, testCnt)
    {
        int x, s, r, t, n;
        
        scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
        
        forn(i, n)
        {
            int l, r, w;
            
            scanf("%d%d%d", &l, &r, &w);
            
            a[i] = seg(l, r, w);
        }
        
        ld ans = 0.0;
        
        ld len = 0.0;
        
        forn(i, n)
        {
            len += ld(a[i].sc - a[i].ft);
            ans += ld(a[i].sc - a[i].ft) / ld(s + a[i].w);
        }

        ld ost = ld(x) - len;
        
        ans += ost / s;
        
        ld all = t;            
        
        ld can = min(ost, all * r);
        ld tcan = can / r;
        
        all -= tcan;
        ans += tcan - (can / ld(s));

        sort(a, a + n, cmp);
        
        forn(i, n)
        {
            ld can = min(all * ld(r + a[i].w), ld(a[i].sc - a[i].ft));
            ld tcan = can / ld(r + a[i].w);
        
            ans += tcan - can / ld(s + a[i].w);

            all -= tcan;
        }
    
        printf("Case #%d: %.10lf\n", test + 1, double(ans));
    }

    return 0;
}
