#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int N, K;
int P[111][100];
bool G[111][111];
int D[1<<16];

bool check_clique(int S) {
  for (int i = 0; i < N; i++) if (S & (1<<i)) {
    for (int j = 0; j < i; j++) if (S & (1<<j)) {
      if (!G[i][j]) return false;
    }
  }
  return true;
}

int dfs(int S) {
  if (S == 0) return 0;
  if (D[S]) return D[S];
  
  if (check_clique(S)) {
    D[S] = 1;
    return D[S];
  }

  int R = 1234567890;
  for(int s=S; s; s=(s-1)&S) if (s != S) {
    R = min(R, dfs(s) + dfs(S & (~s)));
  }
  D[S] = R;
  return R;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; tc++) {
    printf("Case #%d: ", tc);
    scanf("%d%d", &N, &K);
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < K; j++) {
        scanf("%d", &P[i][j]);
      }
    }

    memset(G, 0, sizeof(G));
    memset(D, 0, sizeof(D));
    for (int i = 0; i < N; i++) {
      for (int j = i+1; j < N; j++) {
        bool ok = true;
        bool up = (P[i][0] > P[j][0]);
        if (P[i][0] == P[j][0]) continue;
        for (int k = 0; k < K; k++) {
          if (P[i][k] == P[j][k]) { ok = false; break; }
          if (P[i][k] > P[j][k] != up) { ok = false; break; }
        }
        if (ok) G[i][j] = G[j][i] = true;
      }
    }

    printf("%d\n", dfs((1<<N)-1));
  }
  return 0;
}
