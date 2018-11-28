#include <stdio.h>
#include <algorithm>

using namespace std;

int N, k;
int len;

int p[17];
char src[50000 + 10];
char des[50000 + 10];

inline void pert(char *src, char *des, int k) {
  for (int i = 0; i < k; ++i) {
    des[i] = src[p[i]];
  }
}

int GetLen() {
  int i;
  for (i = 0; i < len; i += k) {
    pert(src + i, des + i, k);
  }
  int sum = 1;
  for (i = 1; i < len; ++i) {
    sum += (des[i] != des[i - 1]);
  }
  return sum;
}

int main() {
  int i;
  int totalmin;
  scanf("%d", &N);
  for (int e = 1; e <= N; ++e) {
    printf("Case #%d: ", e);
    scanf("%d", &k);
    scanf("%s", src);
    len = strlen(src);
    for (i = 0; i < k; ++i) {
      p[i] = i;
    }
    totalmin = len + 1;
    do {
      i = GetLen();
      if (totalmin > i) {
        totalmin = i;
      }
    } while (next_permutation(p, p + k));
    printf("%d\n", totalmin);
  }
  return 0;
}

