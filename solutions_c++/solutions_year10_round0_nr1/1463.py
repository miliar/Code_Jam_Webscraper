#include <stdio.h>

int pow2[33];

bool solve(int n, int k) {
  k %= pow2[n];
  return k == pow2[n] - 1;
}

int main(void) {
  int nC, cC;

  pow2[0] = 1;
  for (int i = 1; i <= 30; ++i)
    pow2[i] = 2 * pow2[i - 1];

  scanf("%d", &nC);
  for (cC = 0; cC < nC; ++cC) {
    int n, k;
    scanf("%d%d", &n, &k);
    printf("Case #%d: %s\n", cC + 1, solve(n, k) ? "ON" : "OFF");
  }
}
