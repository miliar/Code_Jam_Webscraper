#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int n, m, k, T, t;

int main(void) {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    scanf("%d", &T);
    for (t = 1; t <= T; t++) {
      scanf("%d%d", &n, &k);
      m = 1 << n;
      if (k % m == m - 1) {
	printf("Case #%d: ON\n", t);
      } else {
	printf("Case #%d: OFF\n", t);
      }
    }

    exit(0);
}
