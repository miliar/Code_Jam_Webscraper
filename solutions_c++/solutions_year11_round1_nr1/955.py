
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DEBUG 1
//#define DPRINTF(f, fmt...)
#define DPRINTF fprintf

static int T;

int 
main (int argc, char *argv[])
{
   int rc = 0;

   if (1 != fscanf(stdin, "%d\n", &T)) {
      fprintf(stderr, "can't read number of test cases\n");
      return (1);
    }
    DPRINTF(stderr, "%d test cases\n", T);

    unsigned long long N = ~0ull;
    int Pd, Pg;
    for (int t = 1; t <= T; ++t) {
        if (3 != fscanf(stdin, "%lld %d %d", &N, &Pd, &Pg)) {
            fprintf(stderr, "Can't read test case %d\n", t);
            rc = 1;
            break;
        }
        if (!Pd) {
            if (Pg != 100) {
                printf("Case #%d: Possible\n", t);
            } else {
                printf("Case #%d: Broken\n", t);
            }
            continue;
        }
        if (!Pg) {
            printf("Case #%d: Broken\n", t);
            continue;
        }
        if ((Pg == 100) && (Pd != 100)) {
            printf("Case #%d: Broken\n", t);
            continue;
        }
        if (N > 100) {
            N = 100;
        }
        int d;
        for (d = 1; d <= N; d++) {
           int D = (d * Pd);
           DPRINTF(stderr, "t%d: Pd %d; d %d; D %d\n", t, Pd, d, D);
           if (!(D % 100)) {
               break;
            }
        }
        if (d > N) {
            printf("Case #%d: Broken\n", t);
        } else {
            printf("Case #%d: Possible\n", t);
        }
    }
    return (rc);
}

