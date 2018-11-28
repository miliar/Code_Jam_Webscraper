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

#define NMAX 13

typedef vector<pii> State;

ll hash(State v)
{
    ll ret = 0;
    forv(i, v)
    {
        ret = ret * 12 + v[i].first;
        ret = ret * 12 + v[i].second;
    }
    return ret;
}

const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {1, 0, -1, 0};

queue<State> q;
map<ll, int> d;
int n, m;
string a[NMAX];

bool valid(int x, int y)
{
    return x >= 0 && y >= 0 && x < n && y < m;
}

int used1[NMAX][NMAX], used[NMAX][NMAX];
int iter, iter1;

void mark(State& v)
{
    forv(i, v)
    {
        used1[v[i].first][v[i].second] = iter1;
    }
}

void dfs(int x, int y)
{
    used[x][y] = iter;

    forn(i, 4)
    {   
        int xx = x + dx[i];
        int yy = y + dy[i];

        if (!valid(xx, yy)) continue;

        if (used[xx][yy] == iter - 1) dfs(xx, yy);
    }
}

bool isDangerous(State& v)
{
    ++iter;
    forv(i, v)
    {
        used[v[i].first][v[i].second] = iter;
    }

    ++iter;

    dfs(v[0].first, v[0].second);

    forv(i, v)
    {
        if (used[v[i].first][v[i].second] != iter) return true;
    }

    return false;
}

void solve(int tc)
{
    cerr << tc << endl;
    printf("Case #%d: ", tc);

    cin >> n >> m;

    forn(i, n)
    {
        cin >> a[i];
    }

    State st, fn;

    forn(i, n)
    {
        forn(j, m)
        {
            if (a[i][j] == 'o' || a[i][j] == 'w')
            {
                st.pb(mp(i, j));
            }
            if (a[i][j] == 'x' || a[i][j] == 'w')
            {
                fn.pb(mp(i, j));
            }
        }
    }

    sort(all(st));
    sort(all(fn));

    d.clear();

    while (!q.empty()) q.pop();

    q.push(st);
    d[hash(st)] = 0;

    ll goal = hash(fn);

    if (goal == hash(st))
    {
        printf("0\n");
        return;
    }

    State u, v;
    while (!q.empty())
    {
        u = q.front();
        q.pop();

        ll hu = hash(u);
        int du = d[hu];

        ++iter1;

        mark(u); 

        bool dan = isDangerous(u);

        forv(i, u)
        {
            forn(j, 4)
            {
                int xx = u[i].first + dx[j];
                int yy = u[i].second + dy[j];

                if (!valid(xx, yy) || a[xx][yy] == '#') continue;

                if (used1[xx][yy] == iter1) continue;

                int nj = (j + 2) % 4;

                int nx = xx + 2 * dx[nj];
                int ny = yy + 2 * dy[nj];

                if (!valid(nx, ny) || a[nx][ny] == '#') continue;

                if (used1[nx][ny] == iter1) continue;

                v = u;
                v[i].first = nx;
                v[i].second = ny;

                sort(all(v));

                if (dan && isDangerous(v))
                {
                    continue;    
                }

                ll hv = hash(v);

                if (d.count(hv)) continue;

                if (hv == goal)
                {
                    printf("%d\n", du + 1);
                    return;
                }

                d[hv] = du + 1;
                q.push(v);
            }
        }
    }

    printf("-1\n");
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
            
