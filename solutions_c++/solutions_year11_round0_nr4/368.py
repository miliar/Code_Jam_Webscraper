#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 1010;

int num[MAXN];
bool vis[MAXN];
int n;

void solve()
{
  memset(vis, 0, sizeof(vis));

  double ans = 0.0;
  for (int tot, i = 1; i <= n; ++i) {
    if (vis[i]) continue;

    tot = 0;
    for (int p = i; !vis[i]; i = num[i]) ++tot, vis[i] = 1;
    
    ans += 2.0*(tot-1);
  }

  printf("%.6lf\n", ans);
}

int main() 
{
  int t;
  scanf("%d", &t);
  for (int l = 1; l <= t; ++l) {
    printf("Case #%d: ", l);
    
    scanf("%d", &n);
    for (int i = 1; i <= n; ++i) scanf("%d", &num[i]);
    
    solve();
  }
  return 0;
}
