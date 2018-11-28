#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

/* PREWRITTEN CODE */

#define ALL(x) x.begin(),x.end()
#define PB push_back


#define FOR(i,p,k) for (int i=p; i<k; i++)
#define REP(i,n) for (int i=0; i<n; i++)
#define SIZE(x) (int)x.size()
/* COMPETITION CODE */

int T;
int H, W;
int map[100][100];
int bas[100][100];
char basmap[100];
int curbas = 1;

int xs[4] = {-1,0,0,1};
int ys[4] = {0,-1,1,0};

inline int inmap (int x, int y) {
  if (x < 0 || x >= H || y < 0 || y >= W) return 0;
  return 1;
}

int makebas(int x, int y) {
  if (bas[x][y] != -1) return bas[x][y];
  int bestht = map[x][y];
  int bestx = x;
  int besty = y;
  REP (i, 4) if (inmap(x+xs[i], y+ys[i]) && map[x+xs[i]][y+ys[i]] < bestht) {
    bestht = map[x+xs[i]][y+ys[i]];
    bestx = x + xs[i];
    besty = y + ys[i];
  }
  if (x != bestx || y != besty) bas[x][y] = makebas(bestx,besty);
  else bas[x][y] = curbas++;
  return bas[x][y];
}

int main() {
  scanf("%d", &T);
  REP (test, T) {
    scanf("%d %d", &H, &W);
    REP (i, H) REP (j, W) scanf("%d", &map[i][j]);
    REP (i, H) REP (j, W) bas[i][j] = -1;
    REP (i, H) REP (j, W) makebas(i,j);
    char mark = 'a';
    REP (i, 100) basmap[i] = 0;
    REP (i, H) REP (j, W) if (basmap[bas[i][j]] == 0) basmap[bas[i][j]] = mark++;
    printf("Case #%d:\n", test+1);
    REP(i, H) {
      REP (j, W) {if (j) printf(" "); printf("%c", basmap[bas[i][j]]);}
      printf("\n");
    }
  }
  return 0;
}