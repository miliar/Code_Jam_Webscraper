#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cstdio>
using namespace std;
#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

const int NMAX = 104;
int a[NMAX][NMAX];
int n, m;
int px[NMAX][NMAX];
int py[NMAX][NMAX];
vector<pair<int, int> > g[NMAX][NMAX];
const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};
char ans[NMAX][NMAX];

bool inside(int x, int y)
{
    return x >= 0 && y >= 0 && x < n && y < m;
}

vector<pair<int ,int> > tmp;

void dfs(int x, int y)
{
    tmp.pb(mp(x, y));
    forv(i, g[x][y])
    {
        dfs(g[x][y][i].first, g[x][y][i].second);
    }
}

vector<vector<pair<int, int> > > v;


void solve(int tc)
{
    cin >> n >> m;
    forn(i, n)
    {
        forn(j, m)
        {
            scanf("%d", &a[i][j]);
        }
    }
    forn(i, n) forn(j, m) g[i][j].clear();
    forn(i, n) forn(j, m) px[i][j] = -1;
    forn(i, n)
    {
        forn(j, m)
        {
            int i0 = -1;
            forn(k, 4)
            {
                int x = i + dx[k];
                int y = j + dy[k];
                if (!inside(x, y)) continue;
                if (a[x][y] >= a[i][j]) continue;
                if (i0 == -1 || a[x][y] < a[i+dx[i0]][j+dy[i0]])
                {
                    i0 = k;
                }
            }
            if (i0 != -1) 
            {
                px[i][j] = i + dx[i0];
                py[i][j] = j + dy[i0];
            }
        }
    }


    v.clear();
    vector<pair<int, int> > start;
    forn(i, n)
    {   
        forn(j, m)
        {
            if (px[i][j] == -1) 
            {
                start.pb(mp(i, j));
            }
            g[px[i][j]][py[i][j]].pb(mp(i, j));
        }
    }

    forv(i, start)
    {
        tmp.clear();
        dfs(start[i].first, start[i].second);
        sort(all(tmp));
        v.pb(tmp);
    }
    sort(all(v));
    printf("Case #%d:\n", tc);
    forv(i, v)
    {
        forv(j, v[i])
        {
            ans[v[i][j].first][v[i][j].second] = char(i+'a');
        }
    }
    forn(i, n)
    {
        forn(j, m) 
        {
            if (j) printf(" ");
            printf("%c", ans[i][j]);
        }
        cout << endl;
    }
}

int main()
{
    int tc;
    cin >> tc;    
    forn(it, tc) solve(it+1);
}