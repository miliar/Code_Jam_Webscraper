#pragma comment(linker, "/stack:64000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <cstring>
#include <ctime>
#include <cmath>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <utility>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(x, y) make_pair((x), (y))
#define ft first
#define sc second
#define X first
#define Y second

using namespace std;

typedef unsigned int uint;
typedef unsigned char byte;
typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;
typedef pair<ld, ld> ptd;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

const int N = 1000 + 13;

double t, len, v1, v2;

int n;
pair<pt, int> a[N];

void read()
{
    scanf("%lf%lf%lf%lf%d", &len, &v1, &v2, &t, &n);
    
    forn(i, n)
        scanf("%d%d%d", &a[i].ft.ft, &a[i].ft.sc, &a[i].sc);
}

int sz = 0;
ptd z[N];

inline bool cmp(const ptd& a, const ptd& b)
{
    if (abs(a.sc - b.sc) > EPS)
        return a.sc + EPS < b.sc;
        
    return a.ft + EPS < b.ft;
}

void solve(int test)
{
    ld sum = 0.0;
    
    forn(i, n)
        sum += a[i].ft.sc - a[i].ft.ft;
        
    assert(sum < len + EPS);
    
    sz = 0;
    
    z[sz++] = mp(len - sum, 0.0);
    
    forn(i, n)
        z[sz++] = mp(a[i].ft.sc - a[i].ft.ft, a[i].sc);
        
    sort(z, z + sz, cmp);
    
    ld ans = 0.0;
    
    forn(i, sz)
    {
        ld curl = z[i].ft;
        ld curv = z[i].sc;
        
        if (curl < t * (curv + v2) + EPS)
        {
            ld curt = curl / (curv + v2);
            ans += curt;
            t -= curt;
        }
        else
        {
            ld curt = t + (curl - t * (curv + v2)) / (curv + v1);
            ans += curt;
            t = 0.0;
        }
    }
    
    printf("Case #%d: %.10lf\n", test + 1, double(ans));
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    
    forn(test, testCount)
    {
        read();
        solve(test);
    }
    
    return 0;
}
