
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BUTTONS 101

#define DPRINTF(f, fmt...)
//#define DPRINTF fprintf

static int
next_position (int buttons, char *color, int *position, int robot, int cur)
{
    for (; buttons; --buttons, ++color, ++position) {
        if (*color == robot) {
            return (*position);
        }
    }
    return (cur);
}

static int
solve (int buttons, char *color, int *position)
{
   int cur_pos[2] = { 1, 1 };
   int next_pos[2];
   int elapsed = 0;

   next_pos[0] = next_position(buttons, color, position, 0, cur_pos[0]);
   next_pos[1] = next_position(buttons, color, position, 1, cur_pos[1]);
   DPRINTF(stderr, "next_pos %d %d\n", next_pos[0], next_pos[1]);
   for (;buttons; ) {
       bool pushed = false;
       int robot = *color;
       DPRINTF(stderr, "t%d\n", elapsed + 1);
       for (int iter = 0; iter < 2; ++iter, robot ^= 1) {
           if (cur_pos[robot] < next_pos[robot]) {
               cur_pos[robot]++;
               DPRINTF(stderr, "..%d moves to %d\n", robot, cur_pos[robot]);
           } else if (cur_pos[robot] > next_pos[robot]) {
               cur_pos[robot]--;
               DPRINTF(stderr, "..%d moves to %d\n", robot, cur_pos[robot]);
           } else if ((*color == robot) && !pushed) {
               DPRINTF(stderr, "..%d pushes %d\n", robot, *position);
               buttons--, color++, position++;
               pushed = true;
               next_pos[robot] = next_position(buttons, color, position,
                                 robot, cur_pos[robot]);
               DPRINTF(stderr, "next_pos %d %d\n", next_pos[0], next_pos[1]);
           } else {
               DPRINTF(stderr, "..%d stays at %d\n", robot, cur_pos[robot]);
           }
       }
       elapsed++;
   }
   return (elapsed);
}


int 
main (int argc, char *argv[])
{
   int rc = 0;
   int num_test_cases;
   char room[MAX_BUTTONS];
   int position[MAX_BUTTONS];

   if (1 != fscanf(stdin, "%d\n", &num_test_cases)) {
      fprintf(stderr, "can't read number of test cases\n");
      return (1);
    }
    DPRINTF(stderr, "%d test cases\n", num_test_cases);
    for (int test_case = 0; test_case < num_test_cases; ++test_case) {
        int num_buttons;
        if (1 != fscanf(stdin, " %d", &num_buttons)) {
            fprintf(stderr, "Can't read number of buttons for test case %d\n",
                    test_case);
            break;
        }
        if (num_buttons >= MAX_BUTTONS) {
            fprintf(stderr, "invalid num buttons %d for test case %d\n",
                    num_buttons, test_case);
            rc = 1;
            break;
        }
        for (int button = 0; button < num_buttons; ++button) {
            if (2 != fscanf(stdin, " %c %d", 
                            &room[button], &position[button])) {
                fprintf(stderr, "Can't read button position for test case %d, "
                                "button %d\n", test_case, button);
                rc = 1;
                break;
            }
            if (room[button] == 'O') {
                room[button] = 0;
            } else if (room[button] == 'B') {
                room[button] = 1;
            } else {
                fprintf(stderr, "Bad color %c (%d) for test case %d, "
                                "button %d\n", room[button], room[button],
                                test_case, button);
                rc = 1;
                break;
            }
        }
        if (rc) {
            break;
        }
        int seconds = solve(num_buttons, room, position);
        fprintf(stdout, "Case #%d: %d\n", test_case + 1, seconds);
    }
    return (rc);
}

