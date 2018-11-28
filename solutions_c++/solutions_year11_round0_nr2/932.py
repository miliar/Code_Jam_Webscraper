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

struct Element {
    KeyedVector<char, char> combo;
    SortedVector<char>  oppo;
};

struct Problem
{
    // common part

    int id; // case number

    KeyedVector<char, Element*> elements;
    Vector<char> spell;
    Vector<char> result;

    void reset() {
        int n = elements.size();
        for (int i = 0; i < n; ++i) {
            delete elements.editValueAt(i);
        }
        elements.clear();
        spell.clear();
        result.clear();
    }

    void input(FILE* file) {
        reset();

        int C;
        if (fscanf(file, "%d", &C) != 1) {
            bad_input();
        }
        for (int i = 0; i < C; ++i) {
            char x, y, z;
            if (fscanf(file, " %c%c%c", &x, &y, &z) != 3) {
                bad_input();
            }
            addCombo(x, y, z);
            if (x != y) {
                addCombo(y, x, z);
            }
        }

        int D;
        if (fscanf(file, " %d", &D) != 1) {
            bad_input();
        }
        for (int i = 0; i < D; ++i) {
            char x, y;
            if (fscanf(file, " %c%c", &x, &y) != 2) {
                bad_input();
            }
            addOppo(x, y);
            if (x != y) {
                addOppo(y, x);
            }
        }

        int N;
        if (fscanf(file, " %d ", &N) != 1) {
            bad_input();
        }
        for (int i = 0; i < N; ++i) {
            spell.add(fgetc(file));
        }
    }

    void addCombo(char x, char y, char z) {
        Element* e = getElement(x, true);
        e->combo.add(y, z);
    }

    void addOppo(char x, char y) {
        Element* e = getElement(x, true);
        e->oppo.add(y);
    }

    Element* getElement(char x, bool create) {
        ssize_t i = elements.indexOfKey(x);
        if (i < 0) {
            if (create) {
                Element* e = new Element;
                elements.add(x, e);
                return e;
            } else {
                return NULL;
            }
        } else {
            return elements.valueAt(i);
        }
    }

    // internals

    void solve() {
        int n = spell.size();
        for (int i = 0; i < n; ++i) {
            char c = spell[i];
            Element* e = getElement(c, false);
            if (e == NULL) {
                result.add(c);
                continue;
            }

            int m = result.size();
            if (m == 0) {
                result.add(c);
                continue;
            }

            // test last element for combo
            ssize_t i_combo = e->combo.indexOfKey(result[m - 1]);
            if (i_combo >= 0) {
                char r = e->combo.valueAt(i_combo);
                printf("%c + %c -> %c\n", c, result[m - 1], r);
                result.editItemAt(m - 1) = r;
                continue;
            }

            // test oppo from start
            for (int j = 0; j < m; ++j) {
                if (e->oppo.indexOf(result[j]) >= 0) {
                    printf("%c <> %c\n", c, result[j]);
                    result.clear();
                    break;
                }
            }

            // append if not cleared (nothing happened).
            if (result.size() > 0) {
                result.add(c);
            }
        }
    }

    // output
    void output(FILE* file) {
        fprintf(file, "Case #%d: [", id);
        int n = result.size();
        if (n > 0)
        {
            fprintf(file, "%c", result[0]);
            for (int i = 1; i < n; ++i) {
                fprintf(file, ", %c", result[i]);
            }
        }
        fprintf(file, "]\n");
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
