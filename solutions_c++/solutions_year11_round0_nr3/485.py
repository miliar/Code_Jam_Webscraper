#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  setvbuf(stdin, NULL, _IOFBF, 10000);
  setvbuf(stdout, NULL, _IOFBF, 10000);

  int n_cases;
  scanf("%d", &n_cases);

  int arr[1024];
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    int n;
    scanf("%d", &n);

    int sum_xor = 0;
    int sum = 0;
    int min_el = -1;
    for (int i = 0; i < n; ++i) {
      scanf("%d", &arr[i]);
      sum_xor ^= arr[i];
      sum += arr[i];
      if (min_el == -1 || min_el > arr[i]) {
        min_el = arr[i];
      }
    }

    printf("Case #%d: ", ctr+1);
    if (sum_xor != 0) {
      printf("NO\n");
    } else {
      printf("%d\n", sum - min_el);
    }
  }
  
  return 0;
}
