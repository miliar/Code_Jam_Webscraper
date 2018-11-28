#include <cstdio>
#include <cstring>
#include <cassert>

#include <vector>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define sz(a) (int)(a).size()
#define mp make_pair
#define pb push_back

const int maxn = 100;

int dx[] = {0, -1, 1, 0};
int dy[] = {-1, 0, 0, 1};

int T, H, W, a[maxn][maxn], is[maxn][maxn];
vector < pair<int, int> > c[maxn][maxn];
int cc, u[maxn][maxn], col[maxn * maxn];

void dfs( int x, int y )
{
  u[y][x] = cc;
  forn(i, sz(c[y][x]))
    dfs(c[y][x][i].first, c[y][x][i].second);
}

int main()
{
  scanf("%d", &T);
  for (int t = 1; t <= T; t++)
  {
    scanf("%d%d", &H, &W);
    forn(i, H)
      forn(j, W)
        scanf("%d", &a[i][j]), c[i][j].clear();
    forn(i, H)
      forn(j, W)
      {
        int mi = a[i][j], mx = -1, my = -1;
        forn(k, 4)
        {
          int x1 = j + dx[k], y1 = i + dy[k];
          if (0 <= y1 && y1 < H && 0 <= x1 && x1 < W)
            if (a[y1][x1] < mi)
              mi = a[y1][x1], mx = x1, my = y1;
        }
        is[i][j] = (mi >= a[i][j]);
        if (mi < a[i][j])
          c[my][mx].pb(mp(j, i));
      }
    forn(i, H)
      forn(j, W)
        if (is[i][j])
          cc++, dfs(j, i);
    
    cc = 0;
    memset(col, -1, sizeof(col));
    forn(i, H)
      forn(j, W)
        if (col[u[i][j]] == -1)
          col[u[i][j]] = cc++;

    printf("Case #%d:\n", t);
    forn(i, H)
      forn(j, W)
        printf("%c%c", 'a' + col[u[i][j]], " \n"[j == W - 1]);
  }
  return 0;
}
