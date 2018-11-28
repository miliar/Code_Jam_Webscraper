#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <queue>
#include <bitset>
#include <utility>
#include <list>
#include <numeric>

#include <cstdio>
#include <cmath>
#include <cctype>
using namespace std;

#define REP(i,n) for(__typeof(n) i=0; i<(n); ++i)
#define FOR(i,a,b) for(__typeof(b) i=a; i<(b); ++i)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

typedef long long ll;
vector<int> par;
vector<bool> bol;
bool najdi(int j, vector<vector<int> > &g) {
    if (par[j] == -1) return true;
    bol[j] = true; int di = par[j];
    REP(i,g[di].size())
    {
        int u = g[di][i];
        if (!bol[u] && najdi(u, g))
        {
            par[u] = di;
            par[j] = -1;
            return true;
        }
    }
    return false;
}
int match(vector<vector<int> > g, int n, int m)
{
    par.assign(m, -1);
    REP(i,n)
    {
        bol.assign(m, false);
        REP(j,g[i].size())
            if (najdi(g[i][j], g))
            {
                par[g[i][j]] = i;
                break;
            }
    }
    return m - count(par.begin(), par.end(), -1);
}
int main() {
    int tt; scanf("%d", &tt);
    REP(sd,tt)
    {
        int n, k; scanf("%d %d", &n, &k);
        int a[n][k];
        REP(i,n)
            REP(j,k) scanf("%d", &a[i][j]);

        vector<vector<int> > g(n);
        REP(i,n)
            REP(j,n)
            {
                bool ok = true;
                REP(l,k) if (a[i][l] >= a[j][l]) ok = false;
                if (ok) g[i].push_back(j);
            }

        printf("Case #%d: %d\n", sd+1, n - match(g, n, n));
    }
}
