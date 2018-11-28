#include <cstdio>
#define MAX 1010

int main () {
  int kases;
  scanf("%d", &kases);
  for (int i = 1; i <= kases; i++) {
    int N, arr[MAX];
    scanf("%d", &N);
    int real_sum = 0, sum = 0;
    for (int j = 0; j < N; j++) {
      scanf("%d", &arr[j]);
      sum = sum^arr[j];
      real_sum += arr[j];
    }
    if (sum == 0) {
      // Find the min. value
      int min = arr[0];
      for (int j = 1; j < N; j++)
          if (min > arr[j]) min = arr[j];
      printf("Case #%d: %d\n", i, real_sum-min);
    }
    else
      printf("Case #%d: NO\n", i);
  }
}
