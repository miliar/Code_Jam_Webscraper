#include <cstdio>

#define maxn 1000

int T;

char cs[maxn][4];
char ds[maxn][4];
char ns[maxn];

char st[maxn];
int cp;

int main() {
  scanf("%d", &T);
  for (int q = 1; q <= T; q++) {
    int c, d, n;
    scanf("%d", &c);
    for (int i = 0; i < c; i++) {
      scanf("%s", cs[i]);
    }
    scanf("%d", &d);
    for (int i = 0; i < d; i++) {
      scanf("%s", ds[i]);
    }

    scanf("%d", &n);
    scanf("%s", ns);

    cp = 0;
    for (int i = 0; i < n; i++) {     
      int cur = ns[i];

      if (cp == 0) {
        st[cp++] = cur;
        continue;
      }

      int last = st[cp - 1];

      int fd = 0;
      for (int j = 0; j < c; j++) {
        if ((cs[j][0] == cur && cs[j][1] == last) || (cs[j][1] == cur && cs[j][0] == last)) {
          st[cp - 1] = cs[j][2];
          fd = 1;
          break;
        }
      }
      if (!fd) {
        st[cp++] = cur;
      }

      last = st[cp - 1];
      for (int j = 0; cp && j < d; j++) {
        int other = -1;
        if (ds[j][0] == last) {
          other = ds[j][1];
        } else if (ds[j][1] == last) {
          other = ds[j][0];
        }
        if (other == -1) continue;

        for (int k = 0; k < cp - 1; k++) {
          if (st[k] == other) {
            cp = 0;
            break;
          }
        }
      }
    }

    printf("Case #%d: [", q);
    if (cp == 0) printf("]\n"); else 
    for (int i = 0; i < cp; i++) {
      printf("%c%c%c", st[i], ",]"[i + 1 == cp], " \n"[i + 1 == cp]);
    }
  }

  return 0;
}
