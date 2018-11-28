#include <cstdio>
#include <algorithm>

using namespace std;

int a[1000];
int N;

int main() {
  int T;
  scanf("%d", &T);

  for (int tt = 1; tt <= T; ++tt) {
    scanf("%d", &N);
    int xorr = 0, summ = 0;
    for (int i = 0; i < N; ++i) {
      scanf("%d", a + i);
      summ += a[i];
      xorr = xorr ^ a[i];
    }
    int sol;

    if (xorr == 0) {
      printf("Case #%d: %d\n", tt, summ - *min_element(a, a+N));
    } else {
      printf("Case #%d: NO\n", tt);
    }
  }

  return 0;
}
