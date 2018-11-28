#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <algorithm>

using namespace std;

#define rep(i, n) for (int i = 0; i < (n); i++)
#define foru(i, a, b) for (int i = (a); i <=(b); i++)
#define ford(i, a, b) for (int i = (a); i >=(b); i--) 

int n, m;

const int maxl = 210, maxn = 500, maxm = 10000, inf = 1000000000;

char nm[maxn][maxl], str[maxl];
int q[maxm], flag[maxm], ans, tim, tot, cas, g[111][1101], sta[maxm];

void init() {
  scanf("%d", &n);  
  gets(str);
  rep(i, n) gets(nm[i]);
  scanf("%d", &m);
  gets(str);
  rep(i, m) {
    gets(str);
    rep(j, n) if (strcmp(str, nm[j]) == 0) q[i] = j;
  }
}

void solve() {
  if (m == 0) {
    ans = 0;
    return;
  }
  rep(i, n) rep(j, m + 1) g[i][j] = inf;
  rep(i, n) g[i][0] = 0;

  rep(j, m + 1) rep(i, n) if (g[i][j] < inf) {
    if (j + 1 <= m && q[j] != i) g[i][j + 1] <?= g[i][j];
    if (j + 1 <= m && q[j] == i) 
      rep(k, n) if (k != i) g[k][j + 1] <?= g[i][j] + 1;
  }
  ans = inf;
  rep(i, n) ans <?= g[i][m];  
}


int main() {
  scanf("%d", &cas);
  rep(tt, cas) {
    init();
    solve();
    printf("Case #%d: %d\n", tt + 1, ans);
  }  
  return 0;
}
