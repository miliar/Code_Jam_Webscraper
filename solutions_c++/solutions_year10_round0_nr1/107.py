#include <algorithm>
#include <cstdio>

using namespace std;

int main() {
  int cases;
  scanf("%d", &cases);
  for (int e = 1; e <= cases; ++e) {
    printf("Case #%d: ", e);
    unsigned n, k;
    scanf("%d %d", &n, &k);
    unsigned p = (1U << n) - 1;
    if ((p & k) == p) {
      printf("ON\n");
    } else {
      printf("OFF\n");
    }
  }
  return 0;
}
