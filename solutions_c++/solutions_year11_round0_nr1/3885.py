#include <stdio.h>
#include <stdlib.h>
#include <list>

#include "bot.h"

void next_line(FILE*);

const char DEFAULT_INPUT_FILE[] = "input.txt";
const char DEFAULT_OUTPUT_FILE[] = "output.txt";

int main(int argc, char** argv)
{
    Bot orange, blue;
    std::list<OrdersList> cases;

    char *file_name = const_cast<char*>(DEFAULT_INPUT_FILE);
    if(argc == 2) {
        file_name = argv[1];
    }

    FILE *in = fopen(file_name, "r");
    if(in == NULL) {
        fprintf(stderr, "ERROR: Could not open file %s.\n", file_name);
        exit(0);
    }

    int num_cases = 0;
    if(fscanf(in, "%d", &num_cases) != 1) {
        fputs("ERROR: First line should be the number of cases.\n", stderr);
    }
    printf("Number of cases: %d\n", num_cases);

    for(int n=1; n <= num_cases; ++n) {
        int num_moves = 0, button_pos = 0;
        char bot_color = ' ';
        OrdersList orders;

        next_line(in);
        if(fscanf(in, "%d", &num_moves) != 1) {
            fputs("ERROR: Command lines should start with number of moves.\n", stderr);
        }
        printf("  Case %d: %d moves\n", n, num_moves);

        for(int i=1; i <= num_moves; ++i) {
            if(fscanf(in, " %c %d", &bot_color, &button_pos) != 2) {
                fputs("ERROR: Commands should be a character followed by a number.\n", stderr);
            }

            Bot *bot;
            if(bot_color == 'O')
                bot = &orange;
            else
                bot = &blue;

            printf("\t%c pushes button %d\n", bot_color, button_pos);

            Order* order = new Order;
            *order = {bot, button_pos};

            orders.push_back(order);
        }
        cases.push_back(orders);
    }
    fclose(in);

    int n=1, t;
    std::list<OrdersList>::iterator it;
    FILE *out = fopen(DEFAULT_OUTPUT_FILE, "w");
    for(it = cases.begin(); it != cases.end(); ++it) {
        OrdersList orders = *it;

        orange.set_position(1);
        blue.set_position(1);
        t = 0;
        while(!orders.empty()) {
            ++t;
            bool completed;

            //printf("Time %d  |  Orange: ", t);
            completed = orange.process(orders);
            //printf("  |  Blue: ");
            completed = blue.process(orders) || completed;
            //puts("");

            if(completed)
                orders.pop_front();
        }

        printf("Case #%d: %d\n", n, t);
        fprintf(out, "Case #%d: %d\n", n, t);

        ++n;
    }

    fclose(out);

    return 0;
}

void next_line(FILE* f) {
    fscanf(f, "%*[^\n]%*c");
}
