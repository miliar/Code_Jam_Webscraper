#include <cstdio>
#include <cassert>
#include <vector>
using namespace std;

typedef long long int64;
int64 const mod = 1000000009;

int n, k;
vector<int> neigh[999];
int deg[999];

int64 dfs(int v, int d, int p=-1)
{
  int s = neigh[v].size();
  int64 res = 1;
  int xx = min(d, 2);
  int c;
  if (p == -1) c = k;
  else c = k - deg[p] - xx + 1;
  for (int i = 0; i < deg[v]; i++) {
    res *= c-i;
    res %= mod;
  }
  for (int i = 0; i < s; i++) {
    int w = neigh[v][i];
    if (w == p) continue;
    res *= dfs(w, d+1, v);
    res %= mod;
  }
  return res;
}

int64 solve()
{
  scanf("%d %d", &n, &k);
  for (int i = 0; i < n; i++) {
    deg[i] = 0;
    neigh[i].clear();
  }
  for (int i = 1; i < n; i++) {
    int a, b;
    scanf("%d %d", &a, &b);
    a--; b--;
    neigh[a].push_back(b); neigh[b].push_back(a);
    deg[a]++; deg[b]++;
  }
  for (int i = 1; i < n; i++) {
    deg[i]--;
  }
  return dfs(0, 0);
}


int main()
{
  int t;
  scanf("%d", &t);
  for (int c = 0; c < t; c++) {
    printf("Case #%d: ", c+1);
    int64 res = solve();
    printf("%lld\n", res % mod);
  }
}
