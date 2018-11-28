#include <cstdio>
#include <cstdlib>
#include <vector>
#define INF 1000000000
using namespace std;

int parent(int node) {
  return ((node-1)/2);
}

int lchild(int node) {
  return (node*2+1);
}

int rchild(int node) {
  return (node*2+2);
}

int main() {
  int N, M, V;
  vector<vector<int> > best;
  vector<int> G;
  vector<int> C;
  vector<int> I;
  scanf("%d", &N);
  for (int cnum = 1; cnum <= N; cnum++) {
    scanf("%d%d", &M, &V);
    best = vector<vector<int> >(M, vector<int>(2, INF));
    G = vector<int>(M);
    C = vector<int>(M);
    I = vector<int>(M);

    for (int j = 0; j < M; j++) {
      if (j < (M-1)/2) {
	scanf("%d%d", &G[j], &C[j]);
      }
      else {
	scanf("%d", &I[j]);
      }
    }

    for (int j = M-1; j >= (M-1)/2; j--) {
      best[j][I[j]] = 0;
    }
    for (int j = (M-1)/2-1; j >= 0; j--) {
      int lc = lchild(j);
      int rc = rchild(j);
      
      // OR gate
      if (G[j] == 0 || (G[j] == 1 && C[j] == 1)) {
	int change = (G[j] == 1 ? 1 : 0);
	best[j][0] <?= best[lc][0] + best[rc][0] + change;
	best[j][1] <?= best[lc][1] + best[rc][0] + change;
	best[j][1] <?= best[lc][0] + best[rc][1] + change;
	best[j][1] <?= best[lc][1] + best[rc][1] + change;
      }
      // AND gate
      if (G[j] == 1 || (G[j] == 0 && C[j] == 1)) {
	int change = (G[j] == 0 ? 1 : 0);
	best[j][0] <?= best[lc][0] + best[rc][0] + change;
	best[j][0] <?= best[lc][0] + best[rc][1] + change;
	best[j][0] <?= best[lc][1] + best[rc][0] + change;
	best[j][1] <?= best[lc][1] + best[rc][1] + change;
      }
    }
    
    if (best[0][V] < INF) {
      printf("Case #%d: %d\n", cnum, best[0][V]);
    }
    else {
      printf("Case #%d: IMPOSSIBLE\n", cnum);
    }
  }
  return 0;
}
