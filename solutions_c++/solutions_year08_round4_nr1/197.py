#include <cstdio>
#include <cstring>

using namespace std;

const int M = 10000;
const int INF = 0x0fffffff;

int a[M][2], g[M], c[M];

void go() {
  int m, v; scanf("%d%d", &m, &v);
  for(int i=0; i<(m-1)/2; ++i) {
    scanf("%d%d", &g[i], &c[i]); 
  }
  for(int i=0; i<(m+1)/2; ++i) {
    int t; scanf("%d", &t);
    int j = (m-1)/2+i;
    a[j][t] = 0;
    a[j][1-t] = INF;
  }

  for(int i=(m-1)/2-1; i>=0; --i) {
    int c1 = 2*(i+1)-1;
    int c2 = 2*(i+1);
    if (c[i]) {
      if (g[i] == 1) {
	/* and gate, can change */
	a[i][0] = a[c1][0] <? a[c2][0];
	a[i][1] = (a[c1][1] + a[c2][1]) <? ((a[c1][1] <? a[c2][1])+1);
      } else {
	/* or gate, can change */
	a[i][0] = (a[c1][0] + a[c2][0]) <? ((a[c1][0] <? a[c2][0])+1);
	a[i][1] = a[c1][1] <? a[c2][1];
      }
    } else {
      if (g[i] == 1) {
	/* and gate, can't change */
	a[i][0] = a[c1][0] <? a[c2][0];
	a[i][1] = a[c1][1] + a[c2][1];
      } else {
	/* or gate, can't change */
	a[i][0] = a[c1][0] + a[c2][0];
	a[i][1] = a[c1][1] <? a[c2][1];
      }
    }
  }

  if (a[0][v] >= INF) {
    printf(" IMPOSSIBLE");
  } else {
    printf(" %d", a[0][v]);
  }
}

int main() {
  int T; scanf("%d", &T);
  for(int t=1; t<=T; ++t) {
    printf("Case #%d:", t);
    go();
    printf("\n");
  }
}
