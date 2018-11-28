#include <cstdio>
#include <algorithm>

bool a[101];
int b[101], bb[101];
int o[101], oo[101];

int main() {
  char ch;
  int case_no, n, t, bn, on, bi, oi, ans;

  b[0] = o[0] = 1;

  scanf("%d", &t);
  for (case_no = 1; case_no <= t; case_no++) {
    scanf("%d", &n);
    bn = on = 0;
    bb[0] = 0;
    oo[0] = 0;
    for (int i = 1; i <= n; i++) {
      getchar();
      ch = getchar();
      if (ch == 'O') {
        a[i] = false;
        scanf("%d", &o[++on]);
      }
      else {
        a[i] = true;
        scanf("%d", &b[++bn]);
      }
    }

    for (int i = bn; i; i--)
      b[i] = std::abs(b[i] - b[i-1]);
    for (int i = on; i; i--)
      o[i] = std::abs(o[i] - o[i-1]);
    
    bi = oi = 0;
    for (int i = 1; i <= n; i++)
      if (a[i]) {
        // b
        bi++;
        bb[bi] = std::max(bb[bi-1] + b[bi], oo[oi]) + 1;
      }
      else {
        // o
        oi++;
        oo[oi] = std::max(oo[oi-1] + o[oi], bb[bi]) + 1;
      }
    
    ans = std::max(bb[bn], oo[on]);
    printf("Case #%d: %d\n", case_no, ans);
  }

  return 0;
}
