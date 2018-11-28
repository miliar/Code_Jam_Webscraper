//#pragma comment(linker, "/stack:64000000")
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
#include <string>
#include <queue>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define debug(x) cerr << #x << " = " << x << endl;
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define sz(a) int((a).size())
#define pb push_back
#define mp(a, b) make_pair((a), (b))
#define INF (INT_MAX / 2)
#define X first
#define Y second
#define ft first
#define sc second
#define PI 3.1415926535897932384626433832795
#define EPS 1e-9
#define NMAX 1010

using namespace std;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef pair<int, int> pt;
typedef long double ld;
typedef pair<ld, ld> ptd;
typedef __int64 li;
typedef unsigned char byte;
typedef vector<vector<int> > matrix;

using namespace std;

int g[NMAX];

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

    int testCount;
    cin >> testCount;
    
    forn(test, testCount)
    {
        li R, k, n;
        cin >> R >> k >> n;
    
        forn(i, n)
            cin >> g[i];
    
        int it = 0, idx = 0;
        li cnt = 0;
    
        map< int, pair<int, li> > z;
    
        li cycle = -1, ans = 0, len, ft;
    
        while (it < R)
        {
            if (z.count(idx))
            {
                cycle = it - z[idx].ft;
                ans = z[idx].sc;
                len = cnt - z[idx].sc;
                ft = z[idx].ft;
            
                break;
            }
        
            z[idx] = mp(it, cnt);
        
            li cur = 0, next = 0;
        
            while (next < n && cur + g[(idx + next) % n] <= k)
                cur += g[(idx + next) % n], next++;
            
            it++;
            idx = (idx + next) % n;
            cnt += cur;
        }
        
        if (cycle == -1)
            ans = cnt;
        else
        {
            ans += (R - ft) / cycle * len;
            it = ft + (R - ft) / cycle * cycle;
    
            while (it < R)
            {
                li cur = 0, next = 0;
        
                while (next < n && cur + g[(idx + next) % n] <= k)
                    cur += g[(idx + next) % n], next++;
            
                it++;
                idx = (idx + next) % n;
                ans += cur;
            }
        }
    
        printf("Case #%d: %I64d\n", test + 1, ans);
    }
    
    return 0;
}
