#include <string.h>
#include <algorithm>
#include <stdio.h>
#include <set>

#define FOREACH(it, t) for(__typeof(t.begin())it = t.begin(); it!=t.end(); ++it)

void solve(int _case) {
  int n,m;
  scanf("%d %d", &n, &m);
  if (m<10) {
    printf("Case #%d: %d\n", _case, 0);
    return;
  }
  fprintf(stderr, "solving case %d %d %d\n", _case, n, m);

  int l;
  char tmp[100];
  int cnt=0;
  for (int i = n; i < m; i++) {
    std::set<int> mapa;
    sprintf(tmp, "%d", i);
    //printf("%d\n", i);
    int l = strlen(tmp);
    //printf("len: %d\n", l);
    for (int rot = 0; rot < l; rot++) {
      std::rotate(tmp, tmp+1, tmp+l);
      int x;
      sscanf(tmp, "%d", &x);
      mapa.insert(x);
    }
    FOREACH(it, mapa)
      if (*it>i && *it<=m) cnt++;

  }

  printf("Case #%d: %d\n", _case, cnt);
}

int main() {
  int t;
  int n;
  scanf("%d", &n);
  for (t = 0; t < n; t++) {
    solve(t+1);
  }
}
