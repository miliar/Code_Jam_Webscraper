#include <algorithm>
#include <cstdio>
using namespace std;

int main() {
  int cases;
  scanf("%i", &cases);
  for (int numcase = 1; numcase <= cases; ++numcase) {
    printf("Case #%i: ", numcase);
    int n, v;
    scanf("%i", &n);
    double ret = 0;
    for (int i = 1; i <= n; ++i) {
      scanf("%i", &v);
      if (v != i) ++ret;
    }
    printf("%lf\n", ret);
  }
  return 0;
}
