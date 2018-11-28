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

const int maxn = 251;

int g[maxn][maxn], ret1, ret2, T, na, nb, n;
int tx[maxn], ty[maxn], nx[maxn], at[maxn], bt[maxn], cas;
char str[100000];

void init() {
  int h1, m1, h2, m2;
  scanf("%d", &T);
  scanf("%d%d", &na, &nb);
  gets(str);
  rep(i, na + nb) {
    gets(str);
    for (int j = 0 ; str[j]; j++) if (!isdigit(str[j])) str[j] = ' ';
    sscanf(str, "%d %d %d %d", &h1, &m1, &h2, &m2);
    at[i] = h1 * 60 + m1;
    bt[i] = h2 * 60 + m2;        
  }
  n = na + nb;
}

int dfs(int u) {
  if (nx[u]) return 0;
  nx[u] = 1;
  ford(i, n - 1, 0) if (g[u][i]) {
    int tmp = ty[i];
    ty[i] = u;
    if (tmp < 0 || dfs(tmp)) return 1;
    ty[i] = tmp;
  }
  return 0;
}

void solve() {
  memset(g, 0, sizeof(g));
  rep(i, na) rep(j, nb) 
    if (bt[i] + T <= at[na + j]) g[i][na + j] = 1;

  rep(i, nb) rep(j, na)
    if (bt[na + i] + T <= at[j]) g[na + i][j] = 1;
  rep(i, n) tx[i] = ty[i] = -1;

  ret1 = ret2 = 0;
  ford(i, n - 1, 0) {
    memset(nx, 0, sizeof(nx));
    dfs(i);
  }
  memset(nx, 0, sizeof(nx));
  rep(i, n) if (ty[i] >= 0) nx[i] = 1;
  rep(i, n) if (nx[i] == 0) {
    if (i < na) ret1++; else ret2++;
  }
}

int main() {
  scanf("%d", &cas);
  rep(tt, cas) {
    init();
    solve();
    printf("Case #%d: %d %d\n", tt + 1, ret1, ret2);
  }
  
  return 0 ;
}
