#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <cmath>
#include <cassert>
#include <cstdio>
#include <ctime>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <algorithm>
#include <stack>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define for1(i, n) for (int i = 1; i <= (int)(n); i++)
#define forv(i, v) forn(i, v.size())

typedef pair<int, int> pii;
typedef long long ll;
typedef set<pii> setp;

#define NMAX 11

const int dx[3] = {1, 0, 0};
const int dy[3] = {0, -1, 1};

char a[NMAX][NMAX];
int n, m, c;
int cx[NMAX], cy[NMAX];
set<pii> r[NMAX];
int wh[NMAX];
bool used[NMAX][NMAX];

void bfs(int sx, int sy)
{
    memset(used, 0, sizeof(used));
    queue<int> qx, qy;
    qx.push(sx);
    qy.push(sy);
    used[sx][sy] = true;
    while (!qx.empty())
    {
        int x = qx.front(); qx.pop();
        int y = qy.front(); qy.pop();

        forn(i, 3)
        {
            int xx = x + dx[i];
            int yy = y + dy[i];
            if (xx < 0 || yy < 0 || xx >= n || yy >= m || used[xx][yy] || a[xx][yy] == '#') continue;

            used[xx][yy] = true;
            qx.push(xx);
            qy.push(yy);
        }
    }
}

queue<setp> q;
set<setp> us;

bool is_lucky(int id)
{
    us.clear();
    while (!q.empty()) q.pop();
    setp start = r[id];

    q.push(start);
    us.insert(start);

    if (start.size() == 1) return true;

    while (!q.empty())
    {
        setp s = q.front();
        q.pop();
        vector<pii> pt(all(s));

        forn(j, 3)
        {
            setp ns;

            bool ok = true;

            forv(k, pt)
            {   
                int xx = pt[k].first + dx[j];
                int yy = pt[k].second + dy[j];

                if (xx < 0 || yy < 0 || xx >= n || yy >= m || a[xx][yy] == '#')
                {
                    ns.insert(pt[k]); 
                }
                else
                {
                    if (start.count(mp(xx, yy)) == 0)
					{
						ok = false;
						break;
					}
                    ns.insert(mp(xx, yy));
                }
            }

            if (ok && us.count(ns) == 0)
            {
                if (ns.size() == 1) return true;
                us.insert(ns);
				q.push(ns);
            }
        }
    }

	return false;
}

void solve(int tc)
{
    cerr << tc << endl;
    printf("Case #%d:\n", tc);
    cin >> n >> m;
    c = 0;
    forn(i, n)
    {
        string s;
        cin >> s;
        forn(j, m) 
        {
            a[i][j] = s[j];
            if (isdigit(a[i][j]))
            {
                cx[c] = i;
                cy[c] = j;
                wh[a[i][j] - '0'] = c;
                c++;
            }
        }
    }

    forn(i, c) r[i].clear();

    forn(x, n)
    {
        forn(y, m)
        {
            if (a[x][y] == '#') continue;
            bfs(x, y);
            forn(i, c)
            {
                if (used[cx[i]][cy[i]])
                {
                    r[i].insert(mp(x, y));
                }
            }
        }
    }

    forn(i, c)
    {
        int j = wh[i];
        printf("%d: %d ", i, r[j].size());

        if (is_lucky(j)) printf("Lucky"); else printf("Unlucky");

        printf("\n");
    }
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int tc;
    cin >> tc;
    forn(it, tc) solve(it + 1);
    return 0;
}
