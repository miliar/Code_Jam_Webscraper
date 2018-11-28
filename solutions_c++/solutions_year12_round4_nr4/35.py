#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

int h, w, max_id;
char a[66][66], was[66][66];
int cnt[66], can[66];

typedef pair <int, int> pnt;
#define x first
#define y second

vector <pnt> st;

int dfs (int x, int y) {
  if (was[x][y] || a[x][y] == '#') {
    return 0;
  }
  int res = 1;

  st.push_back (pnt (x, y));

  was[x][y] = 1;
  res += dfs (x, y + 1);
  res += dfs (x, y - 1);
  res += dfs (x - 1, y);
  return res;
}

set <vector <pnt> > swas;
int go (vector <pnt> &st, int max_x);

int test (vector <pnt> &st, int max_x, int dx, int dy) {
  vector <pnt> ne;
  for (int i = 0; i < (int)st.size(); i++) {
    int x = st[i].x, y = st[i].y;
    int nx = x + dx, ny = y + dy;
    if (a[nx][ny] == '#') {
      nx = x; ny = y;
    }
    if (nx > max_x) {
      return 0;
    }
    ne.push_back (pnt (nx, ny));
  }              
  sort (ne.begin(), ne.end());
  ne.erase (unique(ne.begin(), ne.end()), ne.end());

  return go (ne, max_x);
}

int go (vector <pnt> &st, int max_x) {
  if (swas.count (st)) {
    return 0;
  }
  if ((int)st.size() == 1) {
    return 1;
  }
  swas.insert (st);
  if (test (st, max_x, +1, 0) ||
      test (st, max_x, 0, +1) ||
      test (st, max_x, 0, -1)) {
    return 1;
  }
  return 0;
}


void solve (int sx, int sy) {
  int id = a[sx][sy] - '0';
  if (max_id < id) {
    max_id = id;
  }

  memset (was, 0, sizeof (was));
  st.clear();
  cnt[id] = dfs (sx, sy);

  can[id] = 0;

  sort (st.begin(), st.end());
  swas.clear();

  can[id] = go(st, sx);

}

int main (void) {
  int test_n;
  scanf ("%d", &test_n);

  for (int test_id = 0; test_id < test_n; test_id++) {
    scanf ("%d %d", &h, &w);
    for (int i = 0; i < h; i++) {
      scanf	("%s", a[i]);
    }

    
    max_id = -1;

    for (int i = 0; i < h; i++) {
      for (int j = 0; j < w; j++) {
        if (a[i][j] != '#' && a[i][j] != '.') {
          solve (i, j);
        }
      }
    } 

    printf ("Case #%d:\n", test_id + 1);
    for (int i = 0; i <= max_id; i++) {
      printf ("%d: %d %s\n", i, cnt[i], can[i] ? "Lucky" : "Unlucky");
    }

  }
  return 0;
}