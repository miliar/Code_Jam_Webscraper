#include <algorithm>
#include <vector>
#include <limits.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static unsigned ci[1001];
static int N;
static unsigned citot;
static unsigned half;

static int
try_pick(int startI, unsigned p1xor, unsigned p1tot, unsigned p2xor)
{
    if (p1tot > half) {
        return INT_MAX;
    }
    unsigned restp2 = p2xor;
    for (int i = startI; i < N; i++) {
        restp2 ^= ci[i];
    }
    if (p1xor == restp2) {
        return p1tot;
    }
    // recurse
    for (int i = startI; i < N; i++) {
        int m = try_pick(i + 1, p1xor ^ ci[i], p1tot + ci[i], restp2 ^ ci[i]);
        if (m != INT_MAX) {
            return m;
        }
    }
    return INT_MAX;
}

static void
solve(int caseI) {
    std::sort((unsigned *)ci, (unsigned *)ci + N);
    // if the total isn't even, NO.
//    printf("n=%d\n", N);
//    for (int i = 0; i < N; i++) {
//        printf("%u ", ci[i]);
//    }
    unsigned tx = 0;
    citot = 0;
    for (int i = 0; i < N; i++) {
        tx ^= ci[i];
        citot += ci[i];
    }
//    printf("t=%u\n", tx);
    if (tx % 2 == 1) {
        printf("Case #%d: NO\n", caseI);
        return;
    }
    half = citot / 2;
    int min = INT_MAX;
    for (int i = 0; i < N; i++) {
        unsigned p2xor = 0;
        for (int j = 0; j < i; j++) {
            p2xor ^= ci[j];
        }
        int m = try_pick(i + 1, ci[i], ci[i], p2xor);
        if (m < min) {
            min = m;
        }
    }
    if (min == INT_MAX) {
        printf("Case #%d: NO\n", caseI);
    } else {
        printf("Case #%d: %d\n", caseI, citot - min);
    }



}

int
main(int argc, char **argv)
{
    if (argc < 2) {
        printf("%s input.in\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    FILE *f = fopen(argv[1], "r");
    int T = 0;
    fscanf(f, "%d", &T);
    for (int i = 0; i < T; i++) {
        fscanf(f, "%d", &N);
        for (int j = 0; j < N; j++) {
            fscanf(f, "%u", &ci[j]);
        }
        solve(i + 1);
    }
    return 0;
}
