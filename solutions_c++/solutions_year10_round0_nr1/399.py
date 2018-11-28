#include <cstdio>

int main() {
  int nCases, nBits, nSnaps;
  scanf("%d", &nCases);
  for (int iCase = 1; iCase <= nCases; iCase++) {
    scanf("%d%d", &nBits, &nSnaps);
    int period = 1 << nBits;
    bool light = (nSnaps % period == period - 1);
    printf("Case #%i: %s\n", iCase, light ? "ON" : "OFF");
  }
  return 0;
}
