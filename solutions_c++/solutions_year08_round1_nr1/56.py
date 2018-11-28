#include <cstdio>
#include <algorithm>
using namespace std;

long long const inf = 1LL << 50;

int const max_n = 803;

long long mat[max_n][max_n];

int match[2*max_n];
long long cover[2*max_n];

int color = 1;
int vis[max_n];
bool sel[2*max_n];

long long min_slack[max_n];

int n;

bool done;

inline long long slack(int i, int j)
{
  return mat[i][j] - cover[i] - cover[max_n+j];
}

inline bool edge(int i, int j)
{
  return slack(i, j) == 0;
}

bool dfs(int i)
{
  if (vis[i] == color) return false;
  vis[i] = color;
  for (int j = 0; j < n; j++) {
    if (edge(i, j) && match[i] != j && (match[max_n+j] == -1 || dfs(match[max_n+j]))) {
      match[i] = j;
      match[max_n+j] = i;
      return true;
    }
  }
  return false;
}

void dfs2(int i)
{
  if (sel[i]) return;
  sel[i] = true;
  for (int j = 0; j < n; j++) {
    if (edge(i, j) && !sel[max_n+j] && match[i] != j) {
      sel[max_n+j] = true;
      if (match[max_n+j] != -1) {
        dfs2(match[max_n+j]);
      } else {
        done = true;
      }
    } else if (!sel[max_n+j]) {
      min_slack[j] <?= slack(i, j);
    }
  }
}

long long mincostperfectmatching()
{
  for (int i = 0; i < n; i++) {
    match[i] = -1;
    match[max_n+i] = -1;
  }
  for (int i = 0; i < n; i++) {
    match[max_n+i] = -1;
  }
  for (int i = 0; i < n; i++) {
    cover[i] = mat[i][0];
    cover[max_n+i] = 0;
    for (int j = 1; j < n; j++) {
      cover[i] <?= mat[i][j];
    }
  }
  int matched = 0;
  while (314) {
    done = false;
    while (!done) {
      done = true;
      for (int i = 0; i < n; i++) {
        if (match[i] < 0 && dfs(i)) {
          matched++;
          done = false;
        }
      }
    }
    color++;
    if (matched == n) break;
    for (int i = 0; i < n; i++) {
      sel[i] = false;
    }
    for (int i = 0; i < n; i++) {
      sel[max_n+i] = false;
    }
    done = false;
    for (int i = 0; i < n; i++) {
      if (match[i] < 0) {
        dfs2(i);
        break;
      }
    }
    if (done) continue;
    for (int i = 0; i < n; i++) {
      min_slack[i] = inf;
    }
    for (int i = 0; i < n; i++) {
      if (!sel[i]) continue;
      for (int j = 0; j < n; j++) {
        if (sel[max_n+j]) continue;
        min_slack[j] <?= slack(i, j);
      }
    }
    while (!done) {
      long long delta = inf;
      for (int i = 0; i < n; i++) {
        if (sel[max_n+i]) continue;
        delta <?= min_slack[i];
      }
      for (int i = 0; i < n; i++) {
        if (sel[i]) cover[i] += delta;
        if (sel[max_n+i]) cover[max_n+i] -= delta;
      }
      for (int i = 0; i < n; i++) {
        if (sel[max_n+i]) continue;
        min_slack[i] -= delta;
      }
      for (int i = 0; i < n; i++) {
        if (sel[max_n+i]) continue;
        if (min_slack[i] == 0) {
          sel[max_n+i] = true;
          if (match[max_n+i] == -1) {
            done = true;
            break;
          }
          dfs2(match[max_n+i]);
        }
      }
    }
  }
  long long res = 0;
  for (int i = 0; i < n; i++) {
    res += mat[i][match[i]];
  }
  return res;
}

int main()
{
  int t;
  scanf("%d", &t);
  for (int cas = 1; cas <= t; cas++) {
    long long tab[max_n];
    long long tab2[max_n];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      scanf("%lld", &tab[i]);
    }
    for (int i = 0; i < n; i++) {
      scanf("%lld", &tab2[i]);
    }
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        mat[i][j] = tab[i] * tab2[j];
      }
    }
    printf("Case #%d: %lld\n", cas, mincostperfectmatching());
  }
}
