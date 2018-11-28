#include <cstdio>
#include <string>
#include <map>

using namespace std;

const int maxL = 110;

struct dir {
  map <string, dir *> x;
};

int add( dir &d, char *s ) {
//  fprintf(stderr, "add(%s)\n", s);
  if (!*s) {
    return 0;
  }
  s++;
  string t;
  while (*s != 0 && *s != '/') {
    t += *(s++);
  }
  int ans = 0;
  if (!d.x.count(t)) {
    d.x[t] = new dir;
    ans++;
  }
  ans += add(*d.x[t], s);
  return ans;
}

int main() {
  int nt;
  scanf("%d", &nt);
  for (int tt = 1; tt <= nt; tt++) {
    int n, k;
    scanf("%d%d", &n, &k);
    dir root;
    char s[maxL];
    for (int i = 0; i < n; i++) {
      scanf("%s", s);
      add(root, s);
    }
    int ans = 0;
    for (int i = 0; i < k; i++) {
      scanf("%s", s);
      ans += add(root, s);
    }
    printf("Case #%d: %d\n", tt, ans);
  }
  return 0;
}
