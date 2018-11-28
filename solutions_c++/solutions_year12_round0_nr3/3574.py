#include <algorithm>
#include <functional>

#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <string>
#include <vector>

using namespace std;

const int kMaxN = 2000100;

int cookie[kMaxN];

int main(void)
{
  int _ret;
  int T; scanf("%d", &T);

  for (int counter = 0; counter < T; ++counter) {
    int A, B; _ret = scanf("%d %d", &A, &B);
    int sol = 0;

    memset(cookie, -1, sizeof cookie);

    for (int a = A; a <= B; ++a) {
      int tmp = a, lb = 1;
      int dig = 0; for (tmp = a; tmp > 0; tmp /= 10) { ++dig; lb *= 10; }
      lb /= 10;

      int b = a;

      for (int i = 0; i < dig; ++i) {
        if (A <= b && a < b && b <= B && b >= lb) {
          if (cookie[b] != a) {
            cookie[b] = a;
            ++sol;
          }
        }

        int w = b/lb;
        b = (b-w*lb)*10 + w;
      }
    }

    printf("Case #%d: %d", counter + 1, sol);
    printf("\n");
  }

  return (_ret-_ret);
}
