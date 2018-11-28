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
typedef pair<int, int> PI;
template <class T> void zlepsi(T &a, T b)
{
    a = max(a, b);
}
void norm(vector<PI> &u)
{
    sort(u.begin(), u.end());
}
vector<int> w;
int sef(int a) {
    if (w[a]<0) return a;
    return w[a]=sef(w[a]);
}
void spoj(int a, int b) {
    int x=sef(a), y=sef(b);
    if (x==y) return;
    if (w[x]>w[y]) swap(x, y);
    w[x]+=w[y]; w[y]=x;
}
bool safe(vector<PI> &a)
{
    w.assign(a.size(), -1);
    REP(i,a.size())
        REP(j,i)
        {
            int q = abs(a[i].first - a[j].first) + abs(a[i].second - a[j].second);
            if (q == 1)
                spoj(i, j);
        }
    REP(i,a.size()) if (-w[i] == a.size())
        return true;
    return false;
}
char z[15][15];
int r, c;
bool ok(int a, int b)
{
    if (a >= 0 && a < r && b >= 0 && b < c)
        if (z[a][b] == '.')
            return true;
    return false;
}
int main() {
    int tt; scanf("%d", &tt);
    int sx[] = {0, 1, 0, -1};
    int sy[] = {1, 0, -1, 0};
    REP(sd,tt)
    {
        scanf("%d %d", &r, &c);
        char t[15][15];
        REP(i,r) scanf("%s", t[i]);

        map<vector<PI>, int> vz;
        vector<PI> u, v;
        REP(i,r) REP(j,c)
        {
            if (t[i][j] == 'o' || t[i][j] == 'w') u.push_back(PI(i, j));
            if (t[i][j] == 'x' || t[i][j] == 'w') v.push_back(PI(i, j));
        }
        norm(v);
        norm(u);
        queue<vector<PI> > q;
        vz[u] = 0;
        for (q.push(u); !q.empty(); q.pop())
        {
            vector<PI> y = q.front();
            if (y == v) break;
            REP(i,r) {
                REP(j,c)
                    if (t[i][j] == '#') z[i][j] = '#';
                    else z[i][j] = '.';
            }
            REP(i,y.size())
                z[y[i].first][y[i].second] = 'x';

            //REP(i,r)
            //    printf("%s\n", z[i]);
            //printf("\n");

            bool saf = safe(y);
            REP(i,y.size())
            {
                int a = y[i].first, b = y[i].second;
                REP(k,4) if (ok(a-sx[k], b-sy[k]) && ok(a+sx[k], b+sy[k]))
                {
                    vector<PI> ny = y;
                    ny[i].first += sx[k];
                    ny[i].second += sy[k];
                    if (!saf && !safe(ny)) continue;
                    norm(ny);
                    if (vz.count(ny) == 0)
                    {
                        vz[ny] = vz[y] + 1;
                        q.push(ny);
                    }
                }
            }
        }

        int res;
        if (vz.count(v) == 0) res = -1;
        else res = vz[v];
        printf("Case #%d: %d\n", sd+1, res);
    }
}
