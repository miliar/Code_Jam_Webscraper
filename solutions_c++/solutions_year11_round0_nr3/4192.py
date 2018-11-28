#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  freopen("C-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);

  int T;
  scanf("%d", &T);

  for (int i = 1; i <= T; i++) {
    printf("Case #%d: ", i);
    int c;
    scanf("%d", &c);
    int n;
    int total = 0;
    int btotal = 0;
    int nums[c];
    for (int j = 0; j < c; j++) {
      scanf("%d", &n);
      nums[j] = n;
      btotal = btotal ^ n;
      total = total + n;
    }
    if (btotal == 0)
      printf("%d\n", total - *min_element(nums, nums + c));
    else 
      printf("NO\n");
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
