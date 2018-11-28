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

using namespace std;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef pair<int, int> pt;
typedef long double ld;
typedef pair<ld, ld> ptd;
typedef long long li;
typedef unsigned char byte;
typedef vector<vector<int> > matrix;

using namespace std;

const int NMAX = 55;

ld x[NMAX], v[NMAX];
int perm[NMAX];

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
        li n, k, b, t;
        cin >> n >> k >> b >> t;
        
        forn(i, n)
            cin >> x[i];
            
        forn(i, n)
            cin >> v[i];
            
        forn(i, n)
            perm[i] = i;
            
        int ans = INF;
        
        do
        {
            vector<ld> z;
            
            forn(it, k)
            {
                int i = perm[n - 1 - it];
                
                z.pb(max((z.empty()? -INF: z.back() - 1.0), (ld(b) - x[i]) / v[i]));
            }
                
            bool ok = true;
            
            forn(i, sz(z))
                if (t < z[i])
                    ok = false;
                    
            if (ok)
            {
                int cur = 0;
                
                forn(i, n)
                    forn(j, i)
                        if (perm[j] > perm[i])
                            cur++;
                            
                ans = min(ans, cur);
            }
        } while (next_permutation(perm, perm + n));
        
        if (ans == INF)
            printf("Case #%d: IMPOSSIBLE\n", test + 1);
        else
            printf("Case #%d: %d\n", test + 1, ans);
    }
    
    return 0;
}
