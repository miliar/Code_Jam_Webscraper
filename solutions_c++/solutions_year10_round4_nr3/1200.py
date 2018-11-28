#include <cstdio>

#define MAXD 105

FILE *input = fopen("C-smallAttempt0.in" , "r");
FILE *output = fopen("Csmall.out", "w");



bool grid[MAXD][MAXD];
bool grid2[MAXD][MAXD];
bool temp[MAXD][MAXD];

int C, R;

int main(){

  fscanf(input, "%d", &C);
  for (int foo = 0; foo < C; foo++){
    for (int bar = 0; bar < MAXD; bar++){
      for (int baz = 0; baz < MAXD; baz++){
        grid[bar][baz] = false;
        grid2[bar][baz] = false;
      }
    }
    int seconds = 0;
    int x1, y1, x2, y2;
    fscanf(input, "%d", &R);
    for (int bar = 0; bar < R; bar++){
      fscanf(input, "%d%d%d%d", &x1, &y1, &x2, &y2);
      for (int baz = x1; baz <= x2; baz++){
        for (int spam = y1; spam <= y2; spam++){
          grid[baz][spam] = true;
        }
      }
    }
//    for (int bar = 0; bar < MAXD; bar++){
//      for (int baz = 0; baz < MAXD; baz++){
//        printf("%d", grid[bar][baz]);
//      }
//      printf("\n");
//    }
//    printf("\n");
    bool bactremain = true;
    while (bactremain){
      bactremain = false;
      for (int baz = 1; baz < MAXD; baz++){
        for (int spam = 1; spam < MAXD; spam++){
          if (!grid[baz-1][spam] && !grid[baz][spam-1]){
            grid2[baz][spam] = false;
          } else if (grid[baz-1][spam] && grid[baz][spam-1]){
            grid2[baz][spam] = true;
          } else {
            grid2[baz][spam] = grid[baz][spam];
          }
//          printf("%d", grid[baz][spam]);
          if (grid2[baz][spam]){
            bactremain = true;
          }
        }
//        printf("\n");
      }
//      printf("\n");
      seconds++;
      for (int i = 0; i < MAXD; i++){
        for (int j = 0; j < MAXD; j++){ 
          grid[i][j] = grid2[i][j];
          grid2[i][j] = false;
        }
      }
    }
    fprintf(output, "Case #%d: %d\n", foo+1, seconds); 
  }
  return 0;
}



