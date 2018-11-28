
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_N 200

#define DPRINTF(f, fmt...)
//#define DPRINTF fprintf

char nonbase[256][256];
char oppose[256][256];

#define CHECK_CHAR(n) do {\
        if (((n) < 'A') || ((n) > 'Z')) { \
            fprintf(stderr, "Bad arg %c (%d)\n", (n), (n)); \
            exit(1); \
        } \
    } while (0)
  
int 
main (int argc, char *argv[])
{
   int rc = 0;
   int num_test_cases;

   if (1 != fscanf(stdin, "%d\n", &num_test_cases)) {
      fprintf(stderr, "can't read number of test cases\n");
      return (1);
    }
    DPRINTF(stderr, "%d test cases\n", num_test_cases);
    for (int test_case = 0; test_case < num_test_cases; ++test_case) {
        int C;
        memset(nonbase, 0, sizeof(nonbase));
        memset(oppose, 0, sizeof(oppose));

        if (1 != fscanf(stdin, " %d", &C)) {
            fprintf(stderr, "Can't read number of mappings for test case %d\n",
                    test_case);
            rc = 1;
            break;
        }
        for (int c = 0; c < C; ++c) {
            char a,b,c;
            if (3 != fscanf(stdin, " %c%c%c", &a, &b, &c)) {
                fprintf(stderr, "Bad mapping %d for test %d\n",
                        c, test_case);
                rc = 1;
                break;
            }
            CHECK_CHAR(a);
            CHECK_CHAR(b);
            CHECK_CHAR(c);
            nonbase[a][b] = c;
            nonbase[b][a] = c;
            DPRINTF(stderr, "Map %c%c -> %c\n", a, b, c);
        }

        int D;
        if (1 != fscanf(stdin, " %d", &D)) {
            fprintf(stderr, "Can't read number of oppositions for test case %d\n",
                    test_case);
            rc = 1;
            break;
        }
        for (int d = 0; d < D; ++d) {
            char a,b;
            if (2 != fscanf(stdin, " %c%c", &a, &b)) {
                fprintf(stderr, "Bad opposition %d for test %d\n",
                        d, test_case);
                rc = 1;
                break;
            }
            CHECK_CHAR(a);
            CHECK_CHAR(b);
            oppose[a][b] = 1;
            oppose[b][a] = 1;
        }

        int N;
        if (1 != fscanf(stdin, " %d ", &N)) {
            fprintf(stderr, "Can't read number of invocations "
                            "for test case %d\n",
                    test_case);
            rc = 1;
            break;
        }
        char invoke_list[MAX_N];
        if (1 != fscanf(stdin, "%s", invoke_list)) {
            fprintf(stderr, "Bad invocation list for test %d\n",
                    test_case);
            rc = 1;
            break;
        }
        if (strlen(invoke_list) != N) {
            fprintf(stderr, "Bad invocation length %d; expect %d;"
                            "for test case %d\n",
                    (int)strlen(invoke_list), N, test_case);
            rc = 1;
            break;
        }
            
        char result[MAX_N];
        memset(result, 0, sizeof(result));
        int r = 0;
        for (int n = 0; n < N; ++n) {
            char e = invoke_list[n];

            result[r] = e;
            if (!r) {
                r++;
                continue;
            }
            char c =  nonbase[e][result[r-1]];
            if (c) {
               result[r - 1] = c;
               continue;
            }

            int i;
            for (i = 0; i < r; ++i) {
                if (oppose[e][result[i]]) {
                    break;
                }
            }
            if (i == r) {
                r++;
            } else {
                r = 0;
            }
        }

        fprintf(stdout, "Case #%d: [", test_case + 1);
        if (r) {
            fprintf(stdout, "%c", result[0]);
            for (int i = 1; i < r; i++) {
                fprintf(stdout, ", %c", result[i]);
            }
        }
        fprintf(stdout, "]\n");
    }
    return (rc);
}

