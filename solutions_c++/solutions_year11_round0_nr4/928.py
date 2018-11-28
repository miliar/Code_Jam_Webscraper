/*
 * Copyright (C) 2011 Youjia Lu.
 *
 * Libraries:
 * git://android.git.kernel.org/platform/bionic.git
 * git://android.git.kernel.org/platform/system/core.git
 * git://android.git.kernel.org/platform/frameworks/base.git
 */

#define LOG_TAG "CodeJam"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <libgen.h>
#include <math.h>
#include <cutils/log.h>
#include <utils/String8.h>
#include <utils/Vector.h>
#include <utils/KeyedVector.h>
#include <utils/SortedVector.h>

#define countof(x) (sizeof(x)/sizeof(*(x)))

using namespace android;

void die(const char* message)
{
    fprintf(stderr, "Fatal: %s\n", message);
    exit(1);
}

void bad_input()
{
    die("bad input");
}

struct Problem
{
    // common part

    int id; // case number

    int N;
    int C[1000];

    void input(FILE* file) {
        if (fscanf(file, "%d\n", &N) != 1) {
            bad_input();
        }
        for (int i = 0; i < N; ++i) {
            if (fscanf(file, "%d", &C[i]) != 1) {
                bad_input();
            }
            // make the numbers 0-based as is the array index.
            --C[i];
            printf("%d ", C[i]);
        }
        printf("\n");
    }

    int E;

    void solve() {
        E = 0;
        // It's the number of items that not already in the correct place when
        // input.
        //
        // Strategy: always hold all the items that are in the correct place
        // and hit the rest.  Since each permutation is equally likely, the
        // expected number of correct items after hitting is 1.  So Goro
        // expects to hold one more item after each hit.
        for (int i = 0; i < N; ++i) {
            if (C[i] != i) {
                ++E;
            }
        }
//        solve_sub(0, N);
    }
#if 0
    // each call reduce problem size by at least 1.
    void solve_sub(int start, int end) {
        int n = end - start;
        if (n == 1) {
            LOG_ALWAYS_FATAL_IF((C[start] != start), "wrong sub [%d] = %d",
                    start, C[start]);
            return;
        }

        int m = 0;  // total displacements of items up to i.
        int sub_start = start;  // TODO clean me
        int sub_end = end;
        for (int i = start; i < end; i++) {
            m += C[i] - i;
            if (m == 0) {
                sub_end = i + 1;
                break;
            }
        }

        if (sub_end == end) {
            printf("%d - %d\n", sub_start, sub_end);
            // For non-reducible sub-problems the expectation is its size.
            E += end - sub_start;

            return;
        }

        solve_sub(sub_start, sub_end);

        // the remaining one is also a sub-problem (guaranteed smaller size)
        sub_start = sub_end;
        solve_sub(sub_start, end);
    }
#endif
    // output
    void output(FILE* file) {
        fprintf(file, "Case #%d: %1.06f\n", id, (float)E);
    }
};

int main(int argc, char* argv[])
{
    LOG_ALWAYS_FATAL_IF(argc < 2, "Invalid command line.");

    const char* input_filename = argv[1];
    FILE* input_file = fopen(input_filename, "r");
    LOG_ALWAYS_FATAL_IF (input_file == NULL,
            "Cannot open input file '%s'\n", input_filename);

    const char* output_filename = NULL;
    char* buffer = NULL;
    if (argc == 3) {
        output_filename = argv[2];
    } else {
        const char* input_suffix[] = {
                // Order is important.
                ".in",      // Chrome
                ".in.txt",  // Safari
                ".txt"      // Android Browser
        };
        const char* output_suffix = ".out.txt";

        int n = strlen(input_filename);
        buffer = new char[n + 10];  // plenty room
        strcpy(buffer, input_filename);
        for (int i = 0; i < (int)countof(input_suffix); i++) {
            int m = strlen(input_suffix[i]);
            if (strcmp(buffer + n - m, input_suffix[i]) == 0) {
                strcpy(buffer + n - m, output_suffix);
                output_filename = buffer;
                break;
            }
        }

        LOG_ALWAYS_FATAL_IF (output_filename == NULL,
                "Cannot work out output filename.\n");
    }

    FILE* output_file = fopen(output_filename, "w");
    LOG_ALWAYS_FATAL_IF (output_file == NULL,
            "Cannot open output file '%s'\n", output_filename);

    int num_cases = 0;
    if (fscanf(input_file, "%d\n",
            &num_cases) != 1) {
        bad_input();
    }

    Problem p;

    // Case #x is 1-based.
    for (int i = 1; i <= num_cases; i++) {
        printf("-------------case %d--------------\n", i);
        p.id = i;
        p.input(input_file);
        p.solve();
        p.output(output_file);
    }

    delete[] buffer;
    fclose(input_file);
    fclose(output_file);

    return 0;
}
