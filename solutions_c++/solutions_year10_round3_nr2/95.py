#include <algorithm>
#include <cstdio>

using namespace std;

typedef long long ll;

int main() {
  int cases;
  scanf("%d", &cases);
  for (int e = 1; e <= cases; ++e) {
    printf("Case #%d: ", e);
    ll l, r, c;
    scanf("%lld %lld %lld", &l, &r, &c);
    int result = 0;
    int seg_num = 0;
    while (l < r) {
      ++seg_num;
      l *= c;
    }
    //printf("%d  ", seg_num);
    while (seg_num != 1) {
      ++result;
      seg_num = (seg_num + 1) / 2;
    }
    printf("%d\n", result);
  }
  return 0;
}
