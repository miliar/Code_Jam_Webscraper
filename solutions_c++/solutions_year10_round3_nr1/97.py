#include <algorithm>
#include <cstdio>

using namespace std;

const int kMaxN = 1000 + 24;

int N;
int a[kMaxN], b[kMaxN];

int main() {
  int cases;
  scanf("%d", &cases);
  for (int e = 1; e <= cases; ++e) {
    printf("Case #%d: ", e);
    scanf("%d", &N);
    int result = 0;
    for (int i = 0; i < N; ++i) {
      scanf("%d %d", a + i, b + i);
      for (int j = 0; j < i; ++j)
        if ((a[i] - a[j]) * (b[i] - b[j]) < 0)
          ++result;
    }
    printf("%d\n", result);
  }
  return 0;
}
