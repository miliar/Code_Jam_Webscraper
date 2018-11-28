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
#include <cutils/log.h>
#include <utils/String8.h>
#include <utils/Vector.h>
#include <utils/KeyedVector.h>
#include <utils/SortedVector.h>

#define countof(x) (sizeof(x)/sizeof(*(x)))

#define min(a, b) ((a) < (b)? (a) : (b))
#define max(a, b) ((a) > (b)? (a) : (b))

using namespace android;

void die(const char* message)
{
    fprintf(stderr, "Fatal: %s\n", message);
    exit(1);
}

struct Problem
{
    int id; // case number

    int N;
    int sche[100][100]; // 1 win, 0 lose, -1 no play

    void input(FILE* file) {
        if (fscanf(file, "%d\n", &N) != 1) {
            die("bad input");
        }
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                char c;
                if (fscanf(file, "%c", &c) != 1) {
                    die("bad input");
                }
                if (c == '0') {
                    sche[i][j] = 0;
                } else if (c == '1') {
                    sche[i][j] = 1;
                } else if (c == '.') {
                    sche[i][j] = -1;
                } else {
                    die("bad sche");
                }
            }
            fscanf(file, "\n");
        }
    }

    int win[100];
    int played[100];

    double WP[100];
    double OWP[100];
    double OOWP[100];
    double CPI[100];

    void solve() {
        memset(win, 0, sizeof(win));
        memset(played, 0, sizeof(played));

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (sche[i][j] == 1) {
                    win[i]++;
                }
                if (sche[i][j] != -1) {
                    played[i]++;
                }
            }
            WP[i] = (double)win[i] / played[i];
        }

        for (int i = 0; i < N; ++i) {
            double sum = 0;
            for (int j = 0; j < N; ++j) {
                int r = sche[j][i];
                if (r < 0) {
                    continue;
                }

                double wp = double(win[j] - r) / (played[j] - 1);
                sum += wp;
            }
            OWP[i] = sum / played[i];
        }

        for (int i = 0; i < N; ++i) {
            double sum = 0;
            for (int j = 0; j < N; ++j) {
                int r = sche[i][j];
                if (r < 0) {
                    continue;
                }

                sum += OWP[j];
            }
            OOWP[i] = sum / played[i];
        }

        for (int i = 0; i < N; ++i) {
            CPI[i] = WP[i] * 0.25 + OWP[i] * 0.5 + OOWP[i] * 0.25;
        }
    }

    void output(FILE* file) {
        fprintf(file, "Case #%d:\n", id);
        for (int i = 0; i < N; ++i) {
            fprintf(file, "%f\n", CPI[i]);
        }
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
        die("bad num_cases");
    }

    Problem p;

    // Case #x is 1-based.
    for (int i = 1; i <= num_cases; i++) {
        printf("-------------case %d--------------\n", i);
        p.id = i;
        p.input(input_file);
        p.solve();
        p.output(output_file);
        p.output(stdout);
    }

    delete[] buffer;
    fclose(input_file);
    fclose(output_file);

    return 0;
}
