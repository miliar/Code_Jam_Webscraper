#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int nt;
  assert(scanf("%d", &nt) == 1);
  for (int tt = 1; tt <= nt; tt++) {
    printf("Case #%d: ", tt);
    int n, k;
    assert(scanf("%d%d", &n, &k) == 2);
    vector <vector <int> > to(n);
    for (int i = 0; i < k; i++) {
      int a, b;
      assert(scanf("%d,%d", &a, &b) == 2);
      to[a].push_back(b);
      to[b].push_back(a);
    }
    vector <int> d(n, -1);
    vector <int> q;
    q.push_back(0);
    d[0] = 0;
    int fi = 0;
    while (fi < (int)q.size()) {
      int v = q[fi++];
//      fprintf(stderr, ">>>>> v=%d\n", v);
//      fflush(stderr);
      for (int i = 0; i < (int)to[v].size(); i++) {
        int w = to[v][i];
        if (d[w] == -1) {
//          fprintf(stderr, ">>>>> to w=%d\n", w);
          d[w] = d[v] + 1;
          q.push_back(w);
        }
      }
    }
    fprintf(stderr, ">>>>> bfs ok\n");
    vector <vector <int> > l(n), f(n, vector <int> (n, -1));
    vector <int> /*pos(n), */res(n);
    for (int i = 0; i < n; i++) {
      if (d[i] < 0) {
        continue;
      }
//      pos[i] = (int)l[d[i]].size();
      l[d[i]].push_back(i);
    }
    vector <bool> is(n, false);
    for (int i = 0; i < (int)to[0].size(); i++) {
      is[to[0][i]] = true;
    }
    for (int i = 0; i < n; i++) {
      if (d[i] == 1) {
        int cnt = 0;
        for (int j = 0; j < (int)to[i].size(); j++) {
          if (!is[to[i][j]]) {
            cnt++;
          }
        }
        f[0][i] = to[0].size() + cnt - 2;
      }
    }
    for (int i = 1; i < n; i++) {
      for (int j = 0; j < (int)l[i - 1].size(); j++) {
        int v = l[i - 1][j];
        for (int k = 0; k < (int)l[i].size(); k++) {
          int w = l[i][k];
          bool ok = false;
          for (int o = 0; o < (int)to[v].size(); o++) {
            if (to[v][o] == w) {
              ok = true;
            }
          }
          if (!ok || f[v][w] == -1) {
            continue;
          }
          vector <bool> is(n, false);
          for (int o = 0; o < (int)to[v].size(); o++) {
            is[to[v][o]] = true;
          }
          for (int o = 0; o < (int)to[w].size(); o++) {
            is[to[w][o]] = true;
          }
          for (int o = 0; o < (int)to[w].size(); o++) {
            int u = to[w][o];
            if (d[u] != d[w] + 1) {
              continue;
            }
            int cnt = 0;
            for (int p = 0; p < (int)to[u].size(); p++) {
              if (!is[to[u][p]]) {
                cnt++;
              }
            }
            f[w][u] = max(f[w][u], f[v][w] + cnt - 1);
          }
        }
      }
    }
    int ans1 = d[1] - 1;
    int ans2 = -1;
    if (ans1 == 0) {
      ans2 = to[0].size();
    }
    for (int i = 0; i < (int)to[1].size(); i++) {
      if (d[to[1][i]] != d[1] - 1) {
        continue;
      }
      for (int j = 0; j < n; j++) {
        if (d[j] != d[1] - 2) {
          continue;
        }
        ans2 = max(ans2, f[j][to[1][i]]);
      }
    }
    assert(ans2 >= 0);
    printf("%d %d\n", ans1, ans2);
  }
  return 0;
}
