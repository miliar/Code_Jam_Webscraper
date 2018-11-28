#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

#define SIZE 5
#define MAX 4

typedef enum {INITIAL, X_WON, O_WON, DRAW, NOT_COMPLETE} Result;

void count(char c, int * x_qty, int * o_qty) {
  if (c == 'T') {
    (*x_qty)++; 
    (*o_qty)++;
  }
  else if (c == 'X')
    (*x_qty)++;
  else if (c == 'O')
    (*o_qty)++;
}

int main() {

  int tests;
  scanf(" %d", &tests);

  for (int t = 1; t <= tests; t++) {

    char tic[MAX][SIZE];
    
    for(int i = 0; i < MAX; i++)
      scanf(" %s", tic[i]);
    
    // Verifying if the game is complete
    bool completed = true;
    for(int i = 0; i < MAX; i++)
      for (int j = 0; j < MAX; j++)
	if (tic[i][j] == '.')
	  completed = false;

    Result result = INITIAL;
    for(int i = 0; i < MAX && result == INITIAL; i++) {
      
      // Row processing
      int x_qty = 0, o_qty = 0;
      for (int j = 0; j < MAX; j++)
	count(tic[i][j], &x_qty, &o_qty);
      
      result = (x_qty == 4 ? X_WON : (o_qty == 4 ? O_WON : INITIAL));
    }
    
    for(int i = 0; i < MAX && result == INITIAL; i++) {
      int x_qty = 0, o_qty = 0;
      for(int j = 0; j < MAX; j++) 
	count(tic[j][i], &x_qty, &o_qty);
      result = (x_qty == 4 ? X_WON : (o_qty == 4 ? O_WON : INITIAL));
    }

    if (result == INITIAL) {
      //Diagonal processing
      int diag_x = 0, diag_o = 0;
      for(int i = 0; i < MAX; i++) 
	count(tic[i][i], &diag_x, &diag_o);
      result = (diag_x == 4 ? X_WON : (diag_o == 4 ? O_WON : INITIAL));
    }
    
    if (result == INITIAL) {
      int diag_x = 0, diag_o = 0;
      for(int i = 0; i < MAX; i++) 
	count(tic[i][MAX - i - 1], &diag_x, &diag_o);
      result = (diag_x == 4 ? X_WON : (diag_o == 4 ? O_WON : INITIAL));
    }

    if (completed && result == INITIAL)
      result = DRAW;
    else if (!completed && result == INITIAL)
      result = NOT_COMPLETE;

    printf("Case #%d: ", t);
    switch (result) {
    case X_WON:
      printf("X won\n");
      break;
    case O_WON:
      printf("O won\n");
      break;
    case DRAW:
      printf("Draw\n");
      break;
    case NOT_COMPLETE:
      printf("Game has not completed\n");
    default:
      break;
    }
  }
  return 0;
}
