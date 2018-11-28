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

static int compare_int(const int* lhs, const int* rhs) {
    return (*lhs - *rhs);
}

struct Card {
    int c, s, t;
};

struct Problem
{
    int id; // case number

    int M, N;
    Vector<Card> mHand;
    Vector<Card> mDeck;

    void input(FILE* file) {
        mHand.clear();
        mDeck.clear();

        if (fscanf(file, "%d\n", &N) != 1) {
            die("bad input");
        }
        for (int i = 0; i < N; ++i) {
            Card c;
            if (fscanf(file, "%d %d %d\n", &c.c, &c.s, &c.t) != 3) {
                die("bad input");
            }
            mHand.add(c);
        }

        printf("hand\n");
        for (int i = 0; i < N; ++i) {
            printf("%d: %d %d %d\n", i, mHand[i].c, mHand[i].s, mHand[i].t);
        }

        if (fscanf(file, "%d\n", &M) != 1) {
            die("bad input");
        }
        for (int i = 0; i < M; ++i) {
            Card c;
            if (fscanf(file, "%d %d %d\n", &c.c, &c.s, &c.t) != 3) {
                die("bad input");
            }
            mDeck.add(c);
        }
        printf("deck\n");
        for (int i = 0; i < M; ++i) {
            printf("%d: %d %d %d\n", i, mDeck[i].c, mDeck[i].s, mDeck[i].t);
        }
    }

    struct State {
        Vector<Card> hand;
        Vector<Card> deck;
        int turn;
        int score;
    };

    void solve() {
        y = 0;
        State state;
        state.hand = mHand;
        state.deck = mDeck;
        state.turn = 1;
        state.score = 0;
        while (next_turn(state)) {
            ;
        }
    }

    bool next_turn(State& state) {
        int n = state.hand.size();

        if (state.turn == 0 || n == 0) {
            if (y < state.score) {
                y = state.score;
            }
            return false;
        }

        --state.turn;
        // play any card with a non-zero turn bonus
        for (int i = 0; i < n; ++i) {
            if (state.hand[i].t > 0) {
                play(state, i);
                return true;
            }
        }

        // no card with turn bonus

        int hs[3], hi[3];  // c = 0, 1, 2
        for (int c = 0; c < 3; ++c) {
            hs[c] = -1;
            hi[c] = -1;
        }
        for (int i = 0; i < n; ++i) {
            int c = state.hand[i].c;
            if (state.hand[i].s > hs[c]) {
                hs[c] = state.hand[i].s;
                hi[c] = i;
            }
        }

        for (int c = 0; c < 3; ++c) {
            printf("hi[%d] = %d\n", c, hi[c]);
        }

        LOG_ALWAYS_FATAL_IF((hi[2] >= 0), "hi[2] = %d", hi[2]); // small!

        if (hi[1] >= 0) {
            // fork
            State s1 = state;
            printf(">>> s1\n");
            play(s1, hi[1]);
            while (next_turn(s1)) {
                ;
            }
            printf("<<< s1\n");
        }

        // TODO hi[2];

        if (hi[0] < 0) {
            return false;
        }

        play(state, hi[0]);
        return true;
    }

    void play(State& state, int i) {
        Card c = state.hand[i];
        state.hand.removeAt(i);
        state.score += c.s;
        state.turn += c.t;
        for (int i = 0; i < c.c; ++i) {
            if (state.deck.size() == 0) {
                break;
            }

            Card c1 = state.deck[0];
            state.deck.removeAt(0);
            state.hand.add(c1);
        }
        printf("play %d %d %d: turn %d score %d hand %d\n", c.c, c.s, c.t,
                state.turn, state.score, state.hand.size());
    }

    int y;
    void output(FILE* file) {
        fprintf(file, "Case #%d: %d\n", id, y);
        printf("Case #%d: %d\n", id, y);
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
    }

    delete[] buffer;
    fclose(input_file);
    fclose(output_file);

    return 0;
}
