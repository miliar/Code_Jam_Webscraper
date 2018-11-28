#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <sstream>
#include <bitset>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

#define NMAX 405
#define INF 1000000009

int n, m;
vector<int> g[NMAX];
int h[NMAX], d[NMAX][NMAX];
bitset<NMAX> mask[NMAX];

void solve(int test)
{
    printf("Case #%d: ", test);

    cerr << test << endl;
    cin >> n >> m;

    forn(i, n)
    { 
        g[i].clear();
        mask[i].reset();
    }

    forn(i, m)
    {
        string s; cin >> s;
        int u, v;
        sscanf(s.c_str(), "%d,%d", &u, &v);
        g[u].pb(v);
        g[v].pb(u);
        mask[u].set(v);
        mask[v].set(u);
    }

    g[0].pb(0);
    mask[0].set(0);

    queue<int> q; 
    q.push(0);

    forn(i, n) h[i] = INF;
    h[0] = 0;

    vector<int> ord;

    while (!q.empty())
    {
        int u = q.front(); q.pop();

        ord.pb(u);

        forv(i, g[u])
        {
            int v = g[u][i];
            if (h[v] == INF)
            {
                h[v] = h[u] + 1;
                q.push(v);
            }
        } 
    }

    if (h[1] == 1)
    {
        cout << 0 << " " << mask[0].count() - 1 << endl;
        return;
    }
    memset(d, -1, sizeof(d));
    d[0][0] = mask[0].count();

    forv(i, ord)
    {
        int u = ord[i];

        for (int j = i; j < (int)ord.size(); j++)
        {
            int v = ord[j];

            if (d[u][v] == -1) continue;

            bitset<NMAX> tmp = (mask[u] | mask[v]).flip();

            forv(k, g[v])
            {
                int w = g[v][k];
                if (h[w] != h[v] + 1) continue;

                d[v][w] = max(d[v][w], d[u][v] + (int)(tmp & mask[w]).count());
            }
        }
    }

    int ans = 0;
    forv(i, g[1])
    {
        int u = g[1][i];
        if (h[u] != h[1] - 1) continue;

        forv(j, g[u])
        {
            int v = g[u][j];
            if (h[v] != h[u] - 1) continue;
            ans = max(ans, d[v][u]);
        }

    }

    cout << h[1] - 1 << " " << ans - h[1] << endl;
}
int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    
    return 0;
}