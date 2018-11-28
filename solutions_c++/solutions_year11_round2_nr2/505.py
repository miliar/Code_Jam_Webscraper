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
#define fs first
#define ft first
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
const ld EPS = 1e-8;
const ld PI = 3.1415926535897932384626433832795;

const int N = 1000 * 1000 + 13;

ld a[N];
ld pos[N];
int sz;
ld d;

inline bool can(ld mid)
{
    pos[0] = a[0] - mid;
    
    forn1(i, sz - 1)
    {
        ld npos = pos[i - 1] + d;
        
        if (abs(a[i] - npos) > mid + EPS)
        {
            if (pos[i - 1] < a[i] - mid - EPS && abs(pos[i - 1] - (a[i] - mid)) > d - EPS)
                npos = a[i] - mid;
            else
            if (pos[i - 1] < a[i] + mid - EPS && abs(pos[i - 1] - (a[i] + mid)) > d - EPS)
                npos = a[i] + mid;
            else
                return false;
        }
        
        pos[i] = npos;
    }
    
    return true;
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testCnt;
    
    cin >> testCnt;
    
    forn(t, testCnt)
    {
        int n;
        
        scanf("%d%lf", &n, &d);
        
        sz = 0;
        
        forn(i, n)
        {
            int x, cnt;
            
            scanf("%d%d", &x, &cnt);
            
            forn(j, cnt)
                a[sz++] = ld(x);
        }
        
        ld lf = 0.0;
        ld rg = 1E13;
        
        forn(i, 250)
        {
            ld mid = (lf + rg) / ld(2.0);
            
            if (can(mid))
                rg = mid;
            else
                lf = mid;
        }
        
        assert(can(rg));
        
        printf("Case #%d: %.10lf\n", t + 1, double(rg));
    }
    
    return 0;
}
