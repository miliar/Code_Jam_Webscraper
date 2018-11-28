
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define DEBUG 1
//#define DPRINTF(f, fmt...)
#define DPRINTF fprintf

#define MAX_T (100)
#define MAX_C (1000)
#define MAX_N (1000000)
#define MAX_L (1000000)

static int T, L, t, N, C;
struct _data {
    int weight;
    int parsecs;
    int location;
    int star;
} data[MAX_N];

static int
compare (const void *av, const void *bv)
{
    _data *a = (_data *)av;
    _data *b = (_data *)bv;

    if (a->weight < b->weight) {
        return (1);
    } else if (a->weight == b->weight) {
        if (a->location < b->location) {
            return (1);
        } else if (a->location == b->location) {
            return (0);
        } else {
            return (-1);
        }
    } else {
        return (-1);
    }
}

void
compute_location()
{
   int first_boost_parsecs = t / 2;
   int boosters = L;
   int location;

   for (int i = 0; i < N; i++) {
       data[i].star = i;
       data[i].location = location;
       if (location >= first_boost_parsecs) {
           data[i].weight = data[i].parsecs;
       } else {
           data[i].weight = data[i].parsecs - first_boost_parsecs;
           if (data[i].weight < 0) {
               data[i].weight = 0;
           }
       }
       location += data[i].parsecs;
   }
   qsort(data, N, sizeof(data[0]), compare);

   if (DEBUG) {
        for (int i = 0; i < N; i++) {
            DPRINTF(stderr, "Index %d; star %d; wt %d; loc %d\n",
                        i, data[i].star, data[i].weight,
                        data[i].location);
        }
   }

}

unsigned long long
solve (void)
{
    int speed = 1;

    compute_location();
    unsigned long long elapsed = 0;
    int pending_boost = L;
    int first_boost_parsecs = t / 2;
    for (int i = 0; i < N; i++) {
       int star = data[i].star;
        DPRINTF(stderr, "From %d: distance %d\n", star, data[i].parsecs);
       if (!pending_boost) {
           elapsed += data[i].parsecs * 2;
           DPRINTF(stderr, "..no more boosts: time %d\n", data[i].parsecs * 2);
           continue;
       }
       if (data[i].location >= first_boost_parsecs) {
           DPRINTF(stderr, "..full boost: time %d\n", data[i].parsecs);
           elapsed += data[i].parsecs;
           pending_boost--;
           continue;
        }

        /* part of the way */
       int remaining_boost = first_boost_parsecs - data[i].location; 
       if (remaining_boost >= data[i].parsecs) {
           elapsed += data[i].parsecs * 2;
           DPRINTF(stderr, "..can't complete boost: time %d\n", data[i].parsecs * 2);
           continue;
        }

        DPRINTF(stderr, "..partial boost: time %d ... %d\n", 
                        remaining_boost * 2, 
                        data[i].parsecs - remaining_boost);
        elapsed += remaining_boost * 2 +
                        (data[i].parsecs - remaining_boost);
        pending_boost--;
    }
    return (elapsed);
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
        memset(data, 0, sizeof(data));

        if (4 != fscanf(stdin, " %d %d %d %d", &L, &t, &N, &C)) {
            fprintf(stderr, "Can't read LtNc for test case %d\n", test_case);
            exit(1);
        }
        DPRINTF(stderr, "L %d; t %d; N %d; C %d\n", L, t, N, C);
        static int parsecs_template[MAX_C];
        for (int i = 0; i < C; i++) {
           if (1 != fscanf(stdin, " %d", &parsecs_template[i])) {
                fprintf(stderr, "Can't read parsec %d for test case %d\n", 
                                i, test_case);
                exit(1);
            }
            if (parsecs_template[i] < 0) {
                DPRINTF(stderr, "test %d; parsecs_template %d; val %d\n",
                        test_case, i, parsecs_template[i]);
                exit(1);
            }
        }
        for (int i = 0; i < C; i++) {
           DPRINTF(stderr, "test %d; index %d; template %d\n",
                test_case, i, parsecs_template[i]);
        }
        int j = 0; 
        for (int i = 0; i < N; i++) {
            data[i].parsecs = parsecs_template[j];
            if (data[i].parsecs < 0) {
                DPRINTF(stderr, "test %d; data[%d] from template[%d] is %d\n",
                        test_case, i, j, data[i].parsecs);
                exit(1);
            }
            j = (j + 1) % C;
        }
        fprintf(stdout, "Case #%d: %llu\n", test_case, solve());
    }

    return (rc);
}

