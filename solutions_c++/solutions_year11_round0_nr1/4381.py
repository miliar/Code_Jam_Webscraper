#include <iostream.h>

int getNext(char robot, int index, char * actor, int N)
{
    int i;
    for(i = index; i < N; i++)
    {
          if(actor[i] == robot)
          {
              return i;
          }
    }
    return -1;
}

int action(char robot, int &target_robot, int pos, int &global, char * actor, int N, int * target, int to_press)
{
    if(pos == target[target_robot]) {
        // if has permission to press, press
        if(to_press == 1) {
            // press button
            global++;
            //target_global = target[global];
            target_robot = getNext(robot, target_robot+1, actor, N);
        } // otherwise just wait
        else {
        }
        return pos;
    } else if(pos < target[target_robot]) {
        return pos + 1;
    } else {
        return pos - 1;
    }
}

int main() {
    FILE * input;
    input = fopen("A-large.in", "r");
    FILE * output;
    output = fopen("A-large.out", "w");
    
    int T;    // num cases
    int N;    // num buttons to press
    int i, j, k;  // iterators
    int took;   // result
    
    int O, B;   // actual position on the hallway of O and B robots, from 1 to N
    int global; // index of current instruction
    int target_O, target_B, target_global;     // index of instruction the robot must reach, 0 to N-1
    
    // get number of cases
    fscanf(input, "%d\n", &T);
    
    for(i = 1; i <= T; i++)
    {
          O = 1;
          B = 1;
          global = 0;
          took = 0;
          // solve for each case
          fscanf(input, "%d ", &N);    // get num of buttons to press
          
          char actor [N];
          int target [N];
          // pairs of actor[i]target[i] represent each action to do, ie O2
          
          // fill vector
          for(j = 0; j < N; j++)
          {
                fscanf(input, "%c ", &actor[j]);
                fscanf(input, "%d ", &target[j]);
          }
          
          target_O = getNext('O', 0, actor, N);    // get next instruction the robot must reach
          target_B = getNext('B', 0, actor, N);    // get next instruction the robot must reach
          target_global = target[global];
          // while not all the buttons have been pressed
          while(global < N)
          {
              took++;
              if(target_O != -1 && global == target_O)
              {
                  O = action('O', target_O, O, global, actor, N, target, 1);
                  B = action('B', target_B, B, global, actor, N, target, 0);
              } else
              {
                  O = action('O', target_O, O, global, actor, N, target, 0);
                  B = action('B', target_B, B, global, actor, N, target, 1);
              }
          }
          fprintf(output, "Case #%d: %d\n", i, took);     
    }
    fclose(input);
    fclose(output);
    return 0;
}
