
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define DEBUG 1
//#define DPRINTF(f, fmt...)
#define DPRINTF fprintf

#define MAX_N (100)

struct data { 
    bool played[MAX_N];
    bool won[MAX_N];

    double wp_sum;
    int wp_c;
    double wp;

    double owp_sum[MAX_N];
    double owp_c[MAX_N];
    double owp;

    double oowp;
    double rpi;
} data[MAX_N];

static int T;
static int N;

void
compute_wp (void)
{
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (!data[i].played[j]) continue; // didn't play each other
            data[i].wp_sum += data[i].won[j];
            data[i].wp_c++;
        }
        data[i].wp = data[i].wp_sum / data[i].wp_c;
    }
}

void
compute_owp (void)
{
    for (int i = 0; i < N; i++) {
        double sum = 0;
        int c = 0;
        for (int j = 0; j < N; j++) {
            if (!data[i].played[j]) continue; // didn't play each other
            for (int k = 0; k < N; k++) {
                if (!data[j].played[k]) continue;
                if (i == k) continue; // exclusion
                data[i].owp_sum[j] += data[j].won[k];
                data[i].owp_c[j]++;
            }
            sum += data[i].owp_sum[j] / data[i].owp_c[j];
            c++;
        }
        data[i].owp = sum / c;
    }
}

void
compute_oowp (void)
{
   for (int i = 0; i < N; i++) {
       double sum = 0;
       int c = 0;
       for (int j = 0; j < N; j++) {
           if (!data[i].played[j]) continue;
           sum += data[j].owp;
           c++;
        }
        data[i].oowp = sum / c;
   }
}

void
compute_rpi (void)
{
    for (int i = 0; i < N; i++) {
        data[i].rpi = (0.25 * data[i].wp) + 
                        (0.5 * data[i].owp) + 
                        (0.25 * data[i].oowp);
    }
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

        if (1 != fscanf(stdin, " %d", &N)) {
            fprintf(stderr, "Can't read N for test case %d\n", test_case);
            exit(1);
        }
        for (int n = 0; n < N; n++) {
            char c[MAX_N + 1];
            int r;
            r = fscanf(stdin, "%s", c);
            c[MAX_N] = 0;
            if (1 != r) {
                fprintf(stderr, "Can't read scheudle %d for test case %d; got %d %s\n", 
                            n, test_case, r, c);
                exit(1);
            }

            for (int i = 0; i < N; i++) {
              if (c[i] == '.') continue;
              data[n].played[i] = 1;
              if (c[i] == '1') {
                  data[n].won[i] = 1;
                  continue;
              }
              if (c[i] != '0') {
                 fprintf(stderr, "illegal character %d for sched %d test %d\n",
                        c[i], n, test_case);
                    exit(1);
                }
            }
        }
        compute_wp();
        compute_owp();
        compute_oowp();
        compute_rpi();
        fprintf(stdout, "Case #%d:\n", test_case);
        for (int i = 0; i < N; i++) {
            fprintf(stdout, "%.6f\n", data[i].rpi);
        }
    }

    return (rc);
}

