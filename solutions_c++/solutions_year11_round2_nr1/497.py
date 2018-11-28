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
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int N = 100 + 13;

char a[N][N];
int n;
ld wp[N], owp[N], oowp[N];

inline ld calcWP(int i)
{
    int cnt = 0;
    int all = 0;
    
    forn(j, n)
        if (a[i][j] == '1')
            cnt++, all++;
        else
            if (a[i][j] == '0')
                all++;
                
    ld ans = ld(cnt) / ld(all);
    
    return ans;
}

inline ld calcWP2(int i, int bad)
{
    int cnt = 0;
    int all = 0;
    
    forn(j, n)
    {
        if (j == bad)
            continue;
            
        if (a[i][j] == '1')
            cnt++, all++;
        else
            if (a[i][j] == '0')
                all++;
    }
                
    ld ans = ld(cnt) / ld(all);
    
    return ans;
}

inline ld calcOWP(int i)
{
    ld sum = 0;
    int all = 0;
    
    forn(j, n)
        if (a[i][j] != '.')
            sum += calcWP2(j, i), all++;
                
    ld ans = sum / ld(all);
    
    return ans;
}

inline ld calcOOWP(int i)
{
    ld sum = 0;
    int all = 0;
    
    forn(j, n)
        if (a[i][j] != '.')
            sum += owp[j], all++;
                
    ld ans = sum / ld(all);
    
    return ans;
}

inline ld calc(int i)
{
    ld ans = ld(0.25) * wp[i] + ld(0.5) * owp[i] + ld(0.25) * oowp[i];
    
    return ans;
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testCnt;
    
    cin >> testCnt;
    
    forn(t, testCnt)
    {
        cin >> n;
        
        forn(i, n)
            forn(j, n)
                cin >> a[i][j];
                
        forn(i, n)
            wp[i] = calcWP(i);
            
        forn(i, n)
            owp[i] = calcOWP(i);
            
        forn(i, n)
            oowp[i] = calcOOWP(i);
            
        printf("Case #%d:\n", t + 1);
        
        forn(i, n)
        {
            ld ans = calc(i);
            
            printf("%.10lf\n", double(ans));
        }
    }
    
    return 0;
}
