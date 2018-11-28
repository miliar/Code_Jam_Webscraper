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

inline li hash(const string& s)
{
    li ans = 0;
    
    forn(i, sz(s))
        ans = ans * 1009 + s[i];
        
    return ans;
}

int ans = 0;

map< li, set<li> > g;

void add(bool is)
{
    string s;
    getline(cin, s);
    
    string prev(""), cur("");
    
    for (int i = 0; i < sz(s); )
    {
        cur.pb(s[i++]);
        
        while (i < sz(s) && s[i] != '/')
            cur.pb(s[i++]);
            
        li v = hash(prev), vv = hash(cur);
        
        if (!g[v].count(vv))
            g[v].insert(vv), ans += is;
            
        prev = cur;
    }
}

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
        g.clear();
        
        int n, m;
        cin >> n >> m;
        
        string s;
        getline(cin, s);
        
        ans = 0;
        
        forn(i, n)
            add(false);
            
        forn(j, m)
            add(true);
            
        printf("Case #%d: %d\n", test + 1, ans);
    }
    
    return 0;
}
