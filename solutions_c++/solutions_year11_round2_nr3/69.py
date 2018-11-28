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

const int N = 8 + 3;

int n, m;
int is[N][N];
vector<pt> e;
vector< vector<int> > face;

int ansVal;
vector<int> ans;

int curVal;
vector<int> cur;

inline void checkAns()
{
    if (ansVal >= curVal)
        return;
        
    forn(i, sz(face))
    {
        int cnt2[N];
        memset(cnt2, 0, sizeof(cnt2));
        
        int cur2 = 0;
        
        forn(j, sz(face[i]))
            if (++cnt2[cur[face[i][j]]] == 1)
                cur2++;
            
        if (cur2 < curVal)
            return;
    }
    
    ansVal = curVal;
    ans = cur;
}

int cnt[N];

void solve(int idx)
{
    if (idx == n)
        return checkAns();
        
    for (cur[idx] = 0; cur[idx] < n; cur[idx]++)
    {
        if (++cnt[cur[idx]] == 1)
            curVal++;
            
        solve(idx + 1);
        
        if (--cnt[cur[idx]] == 0)
            curVal--;
    }
}

int g = 0, good[N][N];

void solvep(int test)
{
    face.clear();
    memset(is, 0, sizeof(is));
    
    scanf("%d%d", &n, &m);
    
    e = vector<pt> (m);
    
    forn(i, m)
        scanf("%d", &e[i].ft), e[i].ft--;
        
    forn(i, m)
        scanf("%d", &e[i].sc), e[i].sc--;
        
    forn(i, m)
    {
        is[e[i].ft][e[i].sc] = true;
        is[e[i].sc][e[i].ft] = true;
    }
        
    forn(mask, (1 << n))
    {
        vector<int> cur;
        
        forn(i, n)
            if (mask & (1 << i))
                cur.pb(i);
                
        if (sz(cur) < 3)
            continue;
            
        bool bad = false;
                
        g++;
        
        forn(i, sz(cur))
        {
            int x = cur[i], y = cur[(i + 1) % sz(cur)];
            
            good[x][y] = good[y][x] = g;
            
            if ((x + 1) % n != y && !is[x][y])
                bad = true;
        }
        
        if (bad)
            continue;
        
        forn(i, sz(e))
            if ((mask & (1 << e[i].ft)) && (mask & (1 << e[i].sc)))
                if (good[e[i].ft][e[i].sc] != g)
                    bad = true;
                    
        if (bad)
            continue;
            
        face.pb(cur);
    }
    
    ansVal = 0;
    ans.clear();
    
    cur.resize(n);
    cur[0] = 0;
    
    memset(cnt, 0, sizeof(cnt));
    cnt[0] = 1;
    curVal = 1;
    
    solve(1);
    
    assert(ansVal > 0);
    
    printf("Case #%d: %d\n", test + 1, ansVal);
    
    forn(i, sz(ans))
    {
        printf("%d", ans[i] + 1);
        
        if (i + 1 < sz(ans))
            putchar(' ');
    }
    
    puts("");
    
    cerr << test + 1 << ' ' << clock() << endl;
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    
    forn(test, testCount)
        solvep(test);
    
    return 0;
}
