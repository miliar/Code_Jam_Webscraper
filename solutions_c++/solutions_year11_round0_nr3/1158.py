#include <algorithm>
#include <cstdio>
using namespace std;

const int infinity = 1000000010;

int main() {
  int cases;
  scanf("%i", &cases);
  for (int numcase = 1; numcase <= cases; ++numcase) {
    printf("Case #%i: ", numcase);

    int n, x = 0, sum = 0, a, m = infinity;
    scanf("%i", &n);
    while (n--) {
      scanf("%i", &a);
      m = min(m, a);
      x ^= a;
      sum += a;
    }
    if (x != 0) puts("NO");
    else printf("%i\n", sum - m);
  }
  return 0;
}
