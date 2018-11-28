#include <cstdio>
#include <cstring>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

#define MAXN 1000

long long x[MAXN], y[MAXN];

int main() {
  int t, cases = 1;
  int n, i, j, kx, ky;
  long long res;

  scanf("%d", &t);
  while (t--) {
    scanf("%d", &n);
    for (i = 0; i < n; i++)
      scanf("%lld", &x[i]);
    for (i = 0; i < n; i++)
      scanf("%lld", &y[i]);

    sort(x,x+n);
    sort(y,y+n);

    kx = ky = 0;
    res = 0;
    for (i = n-1, j = n-1; i >= kx && j >= ky; ) {
      if ((x[i] > y[j] && ky <= j)) {
	res += x[i--]*y[ky++];
      } else {
	res += x[kx++]*y[j--];
      }
    }

    printf("Case #%d: %lld\n", cases++, res);
  }
    

  return 0;
}
