#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
char s[32];
int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    scanf("%s", s);
    int l = strlen(s);
    int y, r = 2000000000;
    sscanf(s, "%d", &y);
    s[l] = '0'; l++;
    s[l] = '\0';
    sort(s, s + l);
    do {
      int x;
      sscanf(s, "%d", &x);
      if (x > y && x < r) r = x;
    } while (next_permutation(s, s + l));
    printf("%d\n", r);
  }
  return 0;
}
