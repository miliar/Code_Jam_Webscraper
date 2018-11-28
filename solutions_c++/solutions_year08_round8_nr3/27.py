#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <numeric>
#include <sstream>

using namespace std;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define VI vector<int>
#define pb push_back
#define pii pair<int, int>
#define mp make_pair
#define all(v) v.begin(), v.end()

#define NMAX 505

typedef long long ll;

const ll MOD = 1000000009ll;

ll d[NMAX][NMAX];
int n;
vector<int> g[NMAX];
bool used[NMAX];
int pr[NMAX];
int deg[NMAX];
ll inv[NMAX];
ll k;

void dfs(int v, int p)
{
    pr[v] = p;
    used[v] = true;
    deg[v] = 0;
    forv(i, g[v])
    {
        int u = g[v][i];
        if (used[u]) continue;
        deg[v]++;
        dfs(u, v);
    }
}

ll ee(ll a, ll b, ll& x, ll& y)
{
    if (b == 0)
    {
        x = 1;
        y = 0;
        return a;
    }
    ll x1, y1;
    ll d = ee(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}

ll getInv(ll a, ll n)
{
    ll x, y;
    ee(a, n, x, y);
    return ((x % MOD) + MOD) % MOD;
}

ll A(ll k, ll n)
{
    if (k > n) return 0;
    ll ret = 1;
    for (ll i = n - k + 1; i <= n; i++)
    {
        ret = (ret * i) % MOD;
    }
    /*
    for (ll i = 2; i <= k; i++)
    {
        ret = (ret * inv[i]) % MOD;
    }
    */
    return ret;
}

ll calc(int v, int f)
{
    if (d[v][f] != -1) return d[v][f];
    if (deg[v] > int(k) - f) return 0;
    ll ret = A(deg[v], k - f);
    forv(i, g[v])
    {
        int u = g[v][i];
        if (pr[u] != v) continue;
        int ff = deg[v];
        if (v) ++ff;
        ret = (ret * calc(u, ff)) % MOD;
    }
    return ret;
}

void solve(int tc)
{
    printf("Case #%d: ", tc);
    cin >> n >> k;
    forn(i, n) g[i].clear();
    /*
    for (int i = 2; i <= n; i++)
    {
        inv[i] = getInv(i, MOD);
    }
    */
    forn(i, n - 1)
    {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        g[u].pb(v);
        g[v].pb(u);
    }
    forn(i, n)
    {
        used[i] = false;
        pr[i] = -1;
    }
    dfs(0, -1);
    memset(d, 255, sizeof(d));
    cout << calc(0, 0) << endl;
}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);
    int tc;
    cin >> tc;
    forn(it, tc) solve(it + 1);
    return 0;
}
            
