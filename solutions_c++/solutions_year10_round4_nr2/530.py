#include <cstdio>
#include <algorithm>

using namespace std;

const int inf = 1000000000;

int n, p;
int M[1<<10];
int cost[10][1<<10];
int D[(1<<10) + 1][11];
int dep[10];
int sol;

void solve(int l, int r, int node, int depth) {
  for (int i = 0; i < p; ++i) 
    D[node][i] = inf;
      
  if (depth == 0) {
    for (int i = 0; i < p; ++i) {
      int maxv = 0;
      for (int j = l; j <= r; ++j) {
        if (M[j] - i > maxv)
          maxv = M[j] - i;
      }
      if (maxv == 0) D[node][i] = 0;
      else if (maxv == 1) D[node][i] = cost[depth][dep[depth]];
      else D[node][i] = inf;
    }
    dep[depth]++;
    return;
  }
  
  int m = (l + r) / 2;
  solve(l, m, node * 2, depth - 1);
  solve(m + 1, r, node * 2 + 1, depth - 1);
  
  for (int i = 0; i < p - depth; ++i) {
    D[node][i] = min(D[node][i], D[node * 2][i] + D[node * 2 + 1][i]);
    D[node][i] = min(D[node][i], D[node * 2][i + 1] + D[node * 2 + 1][i + 1] + cost[depth][dep[depth]]);
  }
  dep[depth]++;
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int cs, r = 0;
  scanf("%d", &cs);
  while (cs--) {
    scanf("%d", &p);
    n = 1 << p;
    for (int i = 0; i < n; ++i) {
      scanf("%d", &M[i]);
      M[i] = p - M[i];
    }
      
    for (int i = p - 1; i >= 0; --i) {
      for (int j = 0; j < (1 << i); ++j)
        scanf("%d", &cost[p - 1 - i][j]);
    }
    fill(dep, dep + p, 0);
    solve(0, n - 1, 1, p - 1);
      
    printf("Case #%d: %d\n", ++r, D[1][0]);
  }
  return 0;
}