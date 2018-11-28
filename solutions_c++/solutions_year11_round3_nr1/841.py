
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define DEBUG 1
//#define DPRINTF(f, fmt...)
#define DPRINTF fprintf

#define MAX_T (50)
#define MAX_R (50)
#define MAX_C (50)

static int T, R, C;
char picture[MAX_R][MAX_C + 1];

bool
transform(void)
{
    /* guaranteed to have some blue */

    /* Require minimum dimensions */
    if ((R < 2) || (C < 2)) return (false);

    int r, c;
    for (r = 0; r < (R - 1); r++) {
        for (c = 0; c < (C - 1); c++) {
           if (picture[r][c] != '#') continue;
           if (picture[r][c + 1] == '.') return (false);
           if (picture[r+1][c] == '.') return (false);
           if (picture[r+1][c + 1] == '.') return (false);
           picture[r][c] = '/';
           picture[r][c+1] = '\\';
           picture[r+1][c] = '\\';
           picture[r+1][c+1] = '/';
        }
        if (picture[r][c] == '#') return (false);
    }
    for (c = 0; c < C; c++) {
        if (picture[r][c] == '#') return (false);
    }
    return (true);
}

int 
main (int argc, char *argv[])
{
   int rc = 0;

   if (1 != fscanf(stdin, "%d\n", &T)) {
      fprintf(stderr, "can't read number of test cases\n");
      return (1);
    }
    DPRINTF(stderr, "%d test cases\n", T);

    for (int test_case = 1; test_case <= T; ++test_case) {
        memset(picture, 0, sizeof(picture));

        if (2 != fscanf(stdin, " %d %d", &R, &C)) {
            fprintf(stderr, "Can't read R,C for test case %d\n", test_case);
            exit(1);
        }
        bool all_white = true;
        for (int r = 0; r < R; r++) {
            char line[MAX_C + 1];
            if ((1 != fscanf(stdin, " %s", line)) || 
                        (strlen(line) != C)) {
                fprintf(stderr, "Can't read picture[%d] for test case %d;"
                                        "'%s'\n", r, test_case, line);
                exit(1);
            }
            memcpy(&picture[r][0], line, C);
            if (memchr(line, '#', R)) {
                all_white = false;
            }
        }
        fprintf(stdout, "Case #%d:\n", test_case);
        if (all_white || transform()) {
            for (int r = 0; r < R; r++) {
                fprintf(stdout, "%*.*s\n", C, C, &picture[r][0]);
            }
        } else {
            fprintf(stdout, "Impossible\n");
        }
    }

    return (rc);
}

