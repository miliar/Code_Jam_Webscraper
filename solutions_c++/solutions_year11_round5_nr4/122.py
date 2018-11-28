#include <cstdio>
#include <cstring>

const int maxN = 150;

int n;
char s[maxN + 1];
long long cur, ans;

bool search( int i ) {
  if (i == n) {
    long long mi = 0, ma = 1LL << 31;
    while (mi < ma) {
      long long av = (mi + ma) >> 1;
      if (av * av < cur) {
        mi = av + 1;
      } else {
        ma = av;
      }
    }
    return (mi * mi == cur);
  } else {
    if (s[i] == '?') {
      for (int t = 0; t <= 1; t++) {
        s[i] = '0' + t;
        cur += (long long)t << (n - i - 1);
        if (search(i + 1)) {
          return true;
        }
        cur -= (long long)t << (n - i - 1);
        s[i] = '?';
      }
    } else {
      cur += (long long)(s[i] - '0') << (n - i - 1);
      if (search(i + 1)) {
        return true;
      }
      cur -= (long long)(s[i] - '0') << (n - i - 1);
    }
    return false;
  }
}

int main() {
  int nt;
  scanf("%d", &nt);
  for (int tt = 1; tt <= nt; tt++) {
    printf("Case #%d: ", tt);
    scanf("%s", s);
    n = strlen(s);
    cur = 0;
    search(0);
    for (int i = 0; i < n; i++) {
      printf("%c", s[i]);
    }
    printf("\n");
  }
  return 0;
}
