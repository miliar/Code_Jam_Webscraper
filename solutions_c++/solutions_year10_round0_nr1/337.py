#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

static int lightOn(int n, int k)
{
  int mask = (1 << n) - 1;
  if ((k & mask) == mask)
    return 1;
  return 0;
}

int main()
{
  int i, T, n, k;
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  scanf("%d", &T);
  for (i = 0; i < T; i++) {
    scanf("%d%d", &n, &k);
    if (lightOn(n, k)) {
      printf("Case #%d: %s\n", i + 1, "ON");
    } else {
      printf("Case #%d: %s\n", i + 1, "OFF");
    }
  }
  return 0;
}