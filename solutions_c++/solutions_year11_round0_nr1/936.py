/*
 * Copyright (C) 2011 Youjia Lu.
 *
 * Libraries:
 * git://android.git.kernel.org/platform/bionic.git
 * git://android.git.kernel.org/platform/system/core.git
 * git://android.git.kernel.org/platform/frameworks/base.git
 * ftp://ftp.gmplib.org/pub/gmp-5.0.1/gmp-5.0.1.tar.bz2
 *
 * The code has not been sanitised - there may be a lot of dead code.
 */

#define LOG_TAG "CodeJam"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <libgen.h>
#include <cutils/log.h>
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
    struct Step {
        int color;
        int pos;
        int time;
    };
    Step seq[100];

    void input(FILE* file) {
        if (fscanf(file, "%d", &N) != 1) {
            bad_input();
        }

        for (int i = 0; i < N; ++i) {
            char c;
            if (fscanf(file, " %c %d", &c, &seq[i].pos) != 2) {
                bad_input();
            }
            seq[i].color = (c == 'B')? 1 : 0;   // doesn't matter who's 0 or 1
        }
    }

    // internals

    void solve() {
        int pos[2] = {1, 1};
        int time[2] = {0, 0};
        int c;

        // first ignore wait.
        for (int i = 0; i < N; ++i) {
            c = seq[i].color;
            int move = pos[c] - seq[i].pos;
            if (move < 0) {
                move = -move;
            }
            time[c] = time[c] + move + 1;
            seq[i].time = time[c];
            pos[c] = seq[i].pos;
        }

        c = seq[0].color;
        y = seq[0].time;
        int wait[2] = {0, 0};

        // then consider wait.
        for (int i = 1; i < N; ++i) {
            int c1 = seq[i].color;
            seq[i].time += wait[c1];
            if (c == c1) {
                y = seq[i].time;
            } else {
                int w = y + 1 - seq[i].time;
                if (w > 0) {
                    wait[c1] += w;
                    seq[i].time += w;
                }
                y = seq[i].time;
                c = c1;
            }
        }
    }

    // output
    int y;
    void output(FILE* output_file) {
        fprintf(output_file, "Case #%d: %d\n", id, y);
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
