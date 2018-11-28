#include <cstdio>

int main()
{
  int t;
  scanf("%d", &t);
  for (int i  = 1; i <= t; i++) {
    printf("Case #%d: ", i);
    int n, k;
    scanf("%d %d", &n, &k);
    int m = 1 << n;
    k %= m;
    puts(k == m-1 ? "ON" : "OFF");
  }
  return 0;
}
