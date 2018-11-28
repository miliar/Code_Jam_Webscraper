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

#define NMAX 65

int dx[3] = {1, 0, 0};
int dy[3] = {0, 1, -1};

int n, m;
char a[NMAX][NMAX];
bool us[NMAX][NMAX];

vector<pii> v;

bool valid(int x, int y)
{
    return x >= 0 && y >= 0 && x < n && y < m && a[x][y] != '#';
}

void dfs(int x, int y)
{
    if (us[x][y]) return;
    us[x][y] = true;
    v.pb(mp(x, y));

    forn(i, 3)
    {
        int x1 = x - dx[i];
        int y1 = y - dy[i];

        if (valid(x1, y1)) dfs(x1, y1);
    }
}

set<vector<pii> > used;

vector<pii> apply(vector<pii> u, int dx, int dy)
{
    vector<pii> v;
    forv(i, u)
    {
        int x = u[i].first + dx;
        int y = u[i].second + dy;

        if (valid(x, y)) v.pb(mp(x, y)); else v.pb(u[i]);
    }
    sort(all(v));
    v.erase(unique(all(v)), v.end());
    return v;
}

void solve_cave(char c, int cx, int cy)
{
    memset(us, 0, sizeof(us));

    v.clear();
    dfs(cx, cy);

   sort(all(v));

   if (v.size() == 1)
   {
    printf("%c: %d Lucky\n", c, (int)v.size()); 
    return;
   }
   used.clear();

   queue<vector<pii> > q;
   q.push(v);
   used.insert(v);

   while (!q.empty())
   {
        vector<pii> u = q.front(); q.pop();

        forn(i, 3)
        {
            vector<pii> w = apply(u, dx[i], dy[i]);
            bool ok = true;
            forv(j, w)
            {
                if (w[j].first > cx)
                {
                    ok = false;
                    break;
                }
            }
            if (ok && used.count(w) == 0)
            {
                if (w.size() == 1 && w[0].first == cx && w[0].second == cy)
                {
                    printf("%c: %d Lucky\n", c, (int)v.size());
                    return;
                }
                used.insert(w);
                q.push(w);
            }
        } 
   }

  printf("%c: %d Unlucky\n", c, (int)v.size()); 
}

void solve(int test)
{
    printf("Case #%d:\n", test);

    scanf("%d %d\n", &n, &m);
    forn(i, n)
    {
        forn(j, m)
        {
            scanf("%c", &a[i][j]);
        }
        scanf("\n");
    }

    for (char c = '0'; c <= '9'; c++)
    {
        forn(i, n)
        {
            forn(j, m)
            {
                if (a[i][j] == c)
                {
                    solve_cave(c, i, j);
                }
            }
        }
    }    
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