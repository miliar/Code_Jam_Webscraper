#include <stdio.h>
#include <stdlib.h>

int main() {
  int ncases;
  scanf("%d\n", &ncases);

  for (int j = 0; j < ncases; ++j) {
    int n_buttons; 
    scanf("%d ", &n_buttons);
    int position_blue = 1;
    int position_orange = 1;
    int button;
    char color;
    char current_color = 'B';
    int time_blue = 0;
    int time_orange = 0;
    int time = 0;
    for (int i = 0; i < n_buttons; ++i) {
      scanf("%c", &color);
      scanf("%d ", &button);
      if (color == current_color) {
        if (color == 'B') {
          time += abs(button - position_blue) + 1;
          time_blue = time;
          position_blue = button;
        }
        else if (color == 'O') {
          time += abs(button - position_orange) + 1;
          time_orange = time;
          position_orange = button;
        }
        //printf("Time: %d\n", time);
      }
      else {
        if (color == 'B') {
          int timez = time_orange - time_blue;
          timez = abs(button - position_blue) + 1 - timez;
          if (timez <= 0) timez = 1;
          time += timez;
          time_blue = time;
          current_color = 'B';
          position_blue = button;
        }
        else if (color == 'O') {
          int timez = time_blue - time_orange;
          timez = abs(button - position_orange) + 1 - timez;
          if (timez <= 0) timez = 1;
          time += timez;
          time_orange = time;
          current_color = 'O';
          position_orange = button;
        }
        //printf("Time: %d\n", time);
      }
    }
    printf("Case #%d: %d\n", j + 1, time);
  }
}
