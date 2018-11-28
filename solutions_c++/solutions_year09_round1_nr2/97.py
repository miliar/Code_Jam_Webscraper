#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iomanip>
#include <memory>
#include <cstring>
#include <climits>
#include <cassert>
using namespace std;

#define ALL(a) (a).begin(), (a).end()
#define PB push_back
#define MP make_pair
#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); (i)++)
#define FORD(i, a, b) for(int (i) = (a); (i) >= (b); (i)--)
#define REP(i, n) for (int (i) = 0; (i) < n; (i)++)
#define SIZE(a) (int)(a).size()
#define DBGN(x) cout << #x << " = " << x << endl;
#define DBG(x) cout << #x << " = " << x << ", ";
#define DBGARR(x, n) REP(i, n) cout << #x << '[' << i << "] = " << x[i] << endl;
#define DBGTBL(x, a, b) REP(i, a) REP(j, b) cout << #x << '[' << i << "][" << j << "] = " << x[i][j] << endl;

#define FIN "test.in"
#define FOUT "test.out"

#define MAXN 20

struct light {
  int S;
  int W;
  int T;
};

typedef pair< long long, pair<int,int> > elem;

set<elem> se;

long long a[MAXN * 2][MAXN * 2];
int p[MAXN * 2][MAXN * 2];
light l[MAXN][MAXN];

int N, M;

int dx[] = {0, 1, 0, -1};
int dy[] = {-1, 0, 1, 0};

void doit(int _x, int _y, long long best_t) {
    REP(k, 4) {
      int nx = _x + dx[k];
      int ny = _y + dy[k];
      if (nx < 0 || nx >= 2 * N || ny < 0 || ny >= 2 * M)
        continue;
      if (p[nx][ny])
        continue;
      long long v = best_t;
      long long mn = 1000000000000000LL;
      int x, y;
      x = nx;
      y = ny;
      nx = _x;
      ny = _y;
      if (nx != x) {
        if ((nx / 2) != (x / 2)) {
          mn = min(mn, v + 2);
        } else {
          long long s = l[x/2][y/2].S;
          long long w = l[x/2][y/2].W;
          long long t = l[x/2][y/2].T;
          long long T = s + w;
          t %= T;
          long long vv = v % T;
          if (vv < t) vv += T;
          if (vv <= (t + s - 1)) {
            mn = min(mn, v + 1);
          } else {
            vv -= T;
            mn = min(mn, v + (t - vv) % T + 1); // wait
          }
        }
      } else {
        if ((ny / 2) != (y / 2)) {
          mn = min(mn, v + 2);
        } else {
          long long s = l[x/2][y/2].S;
          long long w = l[x/2][y/2].W;
          long long t = l[x/2][y/2].T;
          long long T = s + w;
          t %= T;
          long long vv = v % T;
          if (vv < t) vv += T;
          if (vv >= t + s) {
            mn = min(mn, v + 1);
          } else {
            vv -= T;
            mn = min(mn, v + (t + s - vv) % T + 1); // wait
          }
        }
      }
      if (mn < a[x][y]) {
        elem e = MP(a[x][y], MP(x, y));
        se.erase(se.find(e));
        a[x][y] = mn;
        se.insert(MP(a[x][y], MP(x, y)));
      }
    }
}

int main()
{
    freopen(FIN, "r", stdin);
    freopen(FOUT, "w", stdout);

    int C;
    cin >> C;
    string s;
    getline(cin, s);
    REP(zzz, C) {
      REP(i, 2 * MAXN) REP(j, 2 * MAXN) a[i][j] = -1;
      cin >> N >> M;
      REP(i, N) REP(j, M) {
        cin >> l[i][j].S >> l[i][j].W >> l[i][j].T;
      }

      se.clear();
      memset(p, 0, sizeof(p));
      REP(i, 2 * N) REP(j, 2 * M) {
        a[i][j] = 1000000000000000LL;
      }
      a[2 * N - 1][0] = 0;
      REP(i, 2 * N) REP(j, 2 * M) {
        se.insert(MP(a[i][j], MP(i, j)));
      }

      while (!se.empty()) {
        elem e = *(se.begin());
        long long best_t = e.first;
        int x = e.second.first;
        int y = e.second.second;
        se.erase(se.begin());
        p[x][y] = 1;
        doit(x, y, best_t);
      }
      cout << "Case #" << zzz + 1 << ": " << a[0][2 * M - 1] << endl;
    }

    fflush(stdout);
    fclose(stdin);
    fclose(stdout);

    return 0;
}
