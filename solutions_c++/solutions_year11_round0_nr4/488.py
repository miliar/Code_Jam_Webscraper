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

  for (int ctr = 0; ctr < n_cases; ++ctr) {
    int n;
    scanf("%d", &n);
    int cnt = 0;
    for (int i = 1; i <= n; ++i) {
      int x;
      scanf("%d", &x);
      if (x != i) ++cnt;
    }
    printf("Case #%d: %.6f\n", ctr+1, (double)cnt);
  }
  
  return 0;
}
