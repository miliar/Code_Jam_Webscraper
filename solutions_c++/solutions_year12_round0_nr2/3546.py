#include <algorithm>
#include <functional>

#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <string>
#include <vector>

using namespace std;

int main(void)
{
  int T; scanf("%d", &T);

  for (int counter = 0; counter < T; ++counter) {
    int n, s, p; scanf("%d %d %d", &n, &s, &p);
    int A = 0, B = 0;

    for (int i = 0; i < n; ++i) {
      int x; scanf("%d", &x);
      if (x >= 3*p - 2) ++A;
      else if (x >= 3*p - 4 && p > 1) ++B;
    }

    printf("Case #%d: %d\n", counter + 1, A + min(B, s));
  }

  return (0-0);
}
