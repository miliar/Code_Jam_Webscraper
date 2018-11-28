#include<cstdio>
#include<algorithm>
using namespace std;
const int N = 2000001;
struct pt {
  int x, y;
  bool operator<(pt a) const {
    if (x != a.x) return x < a.x;
    return y < a.y;
  }
  bool operator!=(pt a) const {
    return x != a.x || y != a.y;
  }  
} s[N*4];
int m;
inline void go(int x) {
  int i, j, k, y;
  for (i = 10, k = 1; i*10 <= x; i*=10, ++k);
  for (y = x; k--; ) {
    j = y%10;
    y = y/10 + j*i;
    if (j > 0 && x < y)
      s[m++] = (pt){x, y};
  }
}
main() {
  int i, j, x, y, T, C = 1;
  char tmp[99];
  for (i = 12; i < N; ++i)
    go(i);
  sort(s, s+m);
  for (i = j = 1; i < m; ++i)
    if (s[i] != s[j-1])
      s[j++] = s[i];
  m = j;
  scanf("%d", &T);
  while (T--) {
    scanf("%d %d", &x, &y);
    for (i = j = 0; i < m; ++i)
      if (x <= s[i].x && s[i].y <= y)
        ++j;
    printf("Case #%d: %d\n", C++, j);
  }
}

