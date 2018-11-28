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
#include <ctime>

using namespace std;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

#define NMAX 100005

struct Edge
{
    int v;
    string w;
};

int n, m;
int kv;
vector<Edge> g[NMAX];

vector<string> split_path(string s)
{
    vector<string> r;

    while (s.find('/') != -1)
    {
        int pos = s.find_last_of('/');
        r.pb(s.substr(pos + 1, s.size()));
        s.erase(pos, s.size());
    }

    reverse(all(r));

    return r;
}

void solve(int tc)
{
    printf("Case #%d: ", tc);
    scanf("%d %d\n", &n, &m);

    forn(i, kv)
    {
        g[i].clear();
    }

    string s;

    kv = 1;

    forn(i, n)
    {
        getline(cin, s);
        vector<string> p = split_path(s);

        int v = 0;

        forv(j, p)
        {
            int nv = -1;

            forv(k, g[v])
            {
                if (g[v][k].w == p[j])
                {
                    nv = g[v][k].v;
                    break;
                }
            }

            if (nv == -1)
            {
                g[kv].clear();
				nv = kv;
                Edge e = {nv, p[j]};
                g[v].pb(e);
                kv++;
            }

            v = nv;
        }
    }

    vector<string> vs;

    forn(i, m)
    {
        getline(cin, s);
        vs.pb(s);
    }

    sort(all(vs));

    int ans = 0;

    forv(i, vs)
    {
        s = vs[i];
        vector<string> p = split_path(s);

        int v = 0;

        forv(j, p)
        {
            int nv = -1;

            forv(k, g[v])
            {
                if (g[v][k].w == p[j])
                {
                    nv = g[v][k].v;
                    break;
                }
            }

            if (nv == -1)
            {
                g[kv].clear();
				nv = kv;
                Edge e = {nv, p[j]};
                g[v].pb(e);				
                kv++;
                ans++;
            }

            v = nv;
        }          
    }

    cout << ans << endl;
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
            
