#include <stdio.h>
#include <math.h>
#include <memory.h>
#include <stdlib.h>

const int MAXN = 100;

int* h[MAXN];
int* fa[MAXN];
char lab[MAXN*MAXN];
int n, m;

void init() {
  scanf("%d %d", &n, &m);
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j) {
      scanf("%d", &h[i][j]);
      fa[i][j] = i * m + j;
      lab[fa[i][j]] = 0;
    }
}

const int dirx[4] = {-1, 0, 0, 1};
const int diry[4] = {0, -1, 1, 0};

int getfa(int x, int y) {
  if (fa[x][y] != x * m + y)
    return getfa(fa[x][y] / m, fa[x][y] % m);
  else
    return fa[x][y];
}

void combine(int i, int j, int x, int y) {
  int tmp1 = getfa(i, j);
  int tmp2 = getfa(x, y);
  if (rand()%2 == 0)
    fa[tmp1 / m][tmp1 % m] = tmp2;
  else
    fa[tmp2 / m][tmp2 % m] = tmp1;
}

void solve() {
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      int min = h[i][j];
      int who = -1;
      for (int d = 0; d < 4; ++d) {
	int x = i + dirx[d];
	int y = j + diry[d];
	if (x >= 0 && x < n && y >= 0 && y < m) {
	  if (h[x][y] < min) {
	    min = h[x][y];
	    who = d;
	  }
	}
      }
      if (who > -1) {
	int x = i + dirx[who];
	int y = j + diry[who];
	combine(i, j, x, y);
      }
    }
  }
}

void print() {
  int cnt = -1;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      int f = getfa(i, j);
      if (lab[f] == 0) {
	++cnt;
	lab[f] = 'a'+cnt;
      }
      printf("%c ", lab[f]);
    }
    printf("\n");
  }
}

int main() {
  int nt;
  scanf("%d", &nt);
  for (int i = 0; i < MAXN; ++i) {
    h[i] = new int[MAXN];
    fa[i] = new int[MAXN];
  }
  for (int i = 0; i < nt; ++i) {
    init();
    solve();
    printf("Case #%d:\n", i+1);
    print();
  }  
}

