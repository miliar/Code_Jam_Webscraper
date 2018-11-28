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

const int N = 100 + 13;

int n;
int t[N], pos[N];

int z[N][N][N];

inline void solve(int test)
{
    cin >> n;
    
    forn(i, n)
    {
        char c;
        cin >> c >> pos[i];
        
        t[i] = c == 'O'? 0: 1;
        pos[i]--;
    }
    
    memset(z, 63, sizeof(z));
    queue< pair<int, pt> > q;
    
    z[0][0][0] = 0;
    q.push(mp(0, mp(0, 0)));
    
    int ans = INF;
    
    while (!q.empty())
    {
        int i = q.front().ft, p1 = q.front().sc.ft, p2 = q.front().sc.sc;
        q.pop();
        
        int& dv = z[i][p1][p2];
        assert(dv < INF / 2);
        
        if (i == n)
        {
            ans = min(ans, dv);
            
            continue;
        }
            
        if (t[i] == 0 && p1 == pos[i])
            for (int d = -1; d <= 1; d++)
                if (0 <= p2 + d && p2 + d < 100)
                    if (z[i + 1][p1][p2 + d] > dv + 1)
                    {
                        z[i + 1][p1][p2 + d] = dv + 1;
                        q.push(mp(i + 1, mp(p1, p2 + d)));
                    }
                    
        if (t[i] == 1 && p2 == pos[i])
            for (int d = -1; d <= 1; d++)
                if (0 <= p1 + d && p1 + d < 100)
                    if (z[i + 1][p1 + d][p2] > dv + 1)
                    {
                        z[i + 1][p1 + d][p2] = dv + 1;
                        q.push(mp(i + 1, mp(p1 + d, p2)));
                    }
                    
        for (int d1 = -1; d1 <= 1; d1++)
            for (int d2 = -1; d2 <= 1; d2++)
                if (0 <= p1 + d1 && p1 + d1 < 100)
                    if (0 <= p2 + d2 && p2 + d2 < 100)
                        if (z[i][p1 + d1][p2 + d2] > dv + 1)
                        {
                            z[i][p1 + d1][p2 + d2] = dv + 1;
                            q.push(mp(i, mp(p1 + d1, p2 + d2)));
                        }
    }
            
    assert(ans < INF / 2);
            
    printf("Case #%d: %d\n", test + 1, ans);
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    
    forn(test, testCount)
        solve(test);
    
    return 0;
}
