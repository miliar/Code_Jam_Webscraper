#include <stdio.h>
#include <stdlib.h>
#include <iostream>

#ifndef SMALLDATASET
    #define __SIZE__ 100
#else
    #define __SIZE__ 3
#endif //SMALLDATASET

int get_maximum_number_with_p_points(int n, int s,
                                      int p, int *t) {
  int ret = 0;

    for (int i = 0; i < n; i++) {
        if (t[i] >= p) {
          int a0 = p;
          int a1 = p-1;
          int a2 = p-1;

            if (a0 + a1 + a2 <= t[i]) {
                ret++;
            }
            else if (a0 + (a1 - 1) + (a2 - 1) <= t[i] && s) {
                ret++;
                s--;
            }
        }
    }

  return ret;
}

int main(int argc, char **argv) {
  int T = 0;
  int S = 0;
  int N = 0;
  int p = 0;
  int t[__SIZE__];

    fscanf(stdin, "%d", &T);

    for (int32_t i = 0; i < T; i++) {
        fscanf(stdin, "%d", &N);
        fscanf(stdin, "%d", &S);
        fscanf(stdin, "%d", &p);

        for (int32_t j = 0; j < N; j++) {
            fscanf(stdin, "%d", &t[j]);
        }

        fprintf(stdout, "Case #%d: %d\n", i+1,
                get_maximum_number_with_p_points(N, S, p, t));
    }
  return 0;
}
