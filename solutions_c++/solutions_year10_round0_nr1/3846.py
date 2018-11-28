#include <iostream>
#include <cstdio>
using namespace std;

int power(int x, int y) {
      if (y == 1) {
            return x;
      } else {
            int k = power(x, y/2);
            if (y % 2) {
                  return x * k * k;
            } else {
                  return k * k;
            }
      }
}

int main()
{
      int T, N, K, i;
      scanf("%d", &T);
      for (int i = 1; i <= T; i++) {
            scanf("%d %d", &N, &K);
            printf("Case #%d: ", i);
            if ((K + 1) % power(2, N) == 0) {
                  printf("ON\n");
            } else {
                  printf("OFF\n");
            }
      }

      return 0;
}
