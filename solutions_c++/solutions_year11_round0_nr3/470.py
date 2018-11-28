#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

#define FOR(i, m, n) for (int i=m; i<n; i++)

using namespace std;

int N;

int main() {
  int vstupy; scanf("%d", &vstupy);
  FOR (qq, 0, vstupy) {
    scanf("%d", &N);
    int m = 100000007;
    int x = 0;
    int sum = 0;
    FOR (i, 0, N) {
       int a; scanf("%d", &a);
       x ^= a;
       m = min(a, m);
       sum += a;
    }
    printf("Case #%d: ", qq+1);
    if (x==0)
      printf("%d\n", sum-m);
    else printf("NO\n");
  }
  return 0;
}
