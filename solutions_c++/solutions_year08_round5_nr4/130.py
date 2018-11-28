#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <vector>
#include <map>

using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define foru(i,a,b) for (int i=(a);i<=(b);i++)
#define ford(i,a,b) for (int i=(a);i>=(b);i--)

const int maxn = 200;

int cas, h, w, r;

struct tnode {
  int l;
  int a[100];
};

int d[maxn][maxn];
int g[maxn][maxn];

void show(tnode &t) {
  while (t.l > 1 && t.a[t.l - 1] == 0) t.l--;
  if (t.l == 0) { 
    t.l = 1;
    t.a[0] = 0;
  }
  ford(i, t.l - 1, 0) printf("%d", t.a[i]);
  printf("\n");
}

tnode operator+(const tnode &a, const tnode &b) {
  tnode c;
  memset(c.a, 0, sizeof(c.a));
  c.l = max(a.l, b.l);
  int tmp = 0;
  rep(i, c.l) {
    c.a[i] = a.a[i] + b.a[i] + tmp;
    if (c.a[i] >= 10) {
      tmp = c.a[i] / 10;
      c.a[i] %= 10;
    } else tmp = 0;
  }
  if (tmp) c.a[c.l++] = tmp;
  while (c.l > 1 && c.a[c.l - 1] == 0) c.l--;
  return c;
}

int main() {
  cin >> cas;
  rep(tt, cas) {
    cin >> h >> w >> r;
    memset(g, 0, sizeof(g));
    memset(d, 0, sizeof(d));
    /*    foru(i, 1, h) foru(j, 1, w) {
      d[i][j].l = 1;
      memset(d[i][j].a, 0, sizeof(d[i][j].a));
    }
    d[1][1].l = 1;
    d[1][1].a[0] = 1;*/
    d[1][1] =1;
    rep(i, r) {
      int x, y;
      cin >> x >> y;
      g[x][y] = 1;
    }
    foru(i, 1, h) foru(j, 1, w) if (g[i][j] == 0) {
      if (i - 2 >= 1 && j - 1 >= 1) d[i][j] =d[i][j] +  d[i-2][j-1];
      if (i - 1 >= 1 && j - 2 >= 1) d[i][j] =d[i][j] + d[i-1][j-2];
      d[i][j] %= 10007;
    }
    printf("Case #%d: ", tt + 1);
    printf("%d\n", d[h][w]);
    //    show(d[h][w]);
  }
}
