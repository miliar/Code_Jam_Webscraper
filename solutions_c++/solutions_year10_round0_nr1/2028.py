#include <cstdio>

int main() {
  int t;
  scanf("%d", &t);
  for( int tc = 0; tc < t; ++tc ) {
    int n, k;
    scanf("%d%d", &n, &k);
    k %= (1<<n);
    printf("Case #%d: %s\n", tc+1, k == (1<<n)-1 ? "ON" : "OFF");
  }
  return 0;
}
