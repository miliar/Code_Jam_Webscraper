
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DEBUG 0
#define DPRINTF(f, fmt...)
//#define DPRINTF fprintf

#define MAX_N   (1001)
#define BITS_PER_LONG 32
#define BITSET_DIM ((MAX_N + BITS_PER_LONG - 1) / BITS_PER_LONG)

static void bitset_ident(void);

unsigned long bitset[BITSET_DIM];
int N;

struct stats_s {
    unsigned long xor_sean;
    unsigned long sum_sean;

    unsigned long xor_patrick;

    int num_sean;
    int num_patrick;

    bool max_found;
    unsigned long max_sum;

    unsigned long pile[MAX_N];
} stats;

static inline void
adjust (int start, unsigned long old_mask, unsigned long new_mask)
{
   unsigned long delta = old_mask ^ new_mask;

   while (delta && (start < N)) {
       if (delta & 1) {
           unsigned long value = stats.pile[start];

           stats.xor_sean ^= value;
           stats.xor_patrick ^= value;

            if (old_mask & 1) {
                /* move from patrick to sean */
                stats.sum_sean += value;
                stats.num_sean++;
                stats.num_patrick--;
            } else {
                /* move from sean to patrick */
                stats.sum_sean -= value;
                stats.num_sean--;
                stats.num_patrick++;
            }

            if ((stats.xor_sean == stats.xor_patrick) &&
                stats.num_sean && stats.num_patrick) {
                if (!stats.max_found) {
                    stats.max_found = true;
                    stats.max_sum = stats.sum_sean;
                } else if (stats.sum_sean > stats.max_sum) {
                    stats.max_sum = stats.sum_sean;
                }
            }
        }
        delta >>= 1;
        old_mask >>= 1;
        new_mask >>= 1;
        start++;
    }

    if (DEBUG) {
        bitset_ident();
        fprintf(stderr, "...xor %lu:%lu; num %u:%u",
                stats.xor_sean, stats.xor_patrick,
                stats.num_sean, stats.num_patrick);
        if (stats.xor_sean ==  stats.xor_patrick) {
            fprintf(stderr, "; sum %lu\n", stats.sum_sean);
        }
    }
}

static inline void 
bitset_inc (void) 
{
    for (int i = 0; i < BITSET_DIM; ++i) {
        unsigned long old_mask = bitset[i];
        unsigned long new_mask = ++bitset[i];
        adjust(i * BITS_PER_LONG, old_mask, new_mask);
        if (new_mask) {
            break;
        }
    }
}

static inline bool
bitset_test (int bit)
{
    return (bitset[bit / BITS_PER_LONG] & (1 << (bit % BITS_PER_LONG)));
}

static void
bitset_ident (void)
{
    for (int n = 0; n < N; n++) {
        if (bitset_test(n)) {
            fprintf(stderr, "%lu", stats.pile[n]);
        } else {
            fprintf(stderr, "[%lu]", stats.pile[n]);
        }
    }
}

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
        memset(&stats, 0, sizeof(stats));

        if (1 != fscanf(stdin, " %d", &N)) {
            fprintf(stderr, "Can't read number of candy for test case %d\n",
                    test_case);
            rc = 1;
            break;
        }

        unsigned long total_xor = 0;
        unsigned long total_sum = 0;
        for (int n = 0; n < N; ++n) {
            if (1 != fscanf(stdin, " %lu", &stats.pile[n])) {
                fprintf(stderr, "Bad value for candy %d for test %d\n",
                        n, test_case);
                rc = 1;
                break;
            }
            total_xor ^= stats.pile[n];
            total_sum += stats.pile[n];
        }
        if (total_xor || (N <= 1)) {
            fprintf(stdout, "Case #%d: NO\n", test_case + 1);
            continue;
        }
            
        memset(bitset, 0, sizeof(bitset));
        stats.xor_sean = total_xor;
        stats.sum_sean = total_sum;
        stats.num_sean = N;
        do {
            bitset_inc();
        } while (!bitset_test(N));

        if (stats.max_found) {
            fprintf(stdout, "Case #%d: %lu\n", test_case + 1, stats.max_sum);
        } else {
            fprintf(stdout, "Case #%d: NO\n", test_case + 1);
        }
    }
    return (rc);
}

