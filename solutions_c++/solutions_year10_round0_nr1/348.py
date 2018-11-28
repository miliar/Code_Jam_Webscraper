#include <cstdio>
using namespace std;

int main() {
  int cases, n, k;
  scanf("%i", &cases);
  for (int numcase = 1; numcase <= cases; ++numcase) {
    scanf("%i%i", &n, &k);
    printf("Case #%i: %s\n", numcase, (k & ((1 << n) - 1)) == ((1 << n) - 1) ? "ON" : "OFF");
  }
  return 0;
}
