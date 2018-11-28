#include <cstdio>

enum game_status { X_WON, O_WON, DRAW, NOT_DONE };

const int mov[][2] = {{0, 1}, {1, 0}, {1, 1}, {1, -1}};

int N;
char board[10][10];

void read_board() {
  for (int i = 0; i < 4; i++) scanf("%s", board[i]);
}

bool is_winner(char cc) {
  for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++) {
      if (i && j) continue;
      
      for (int d = 0; d < 4; d++) {
        int r = i, c = j;
        bool ok = true;

        for (int k = 0; k < 4; k++) {
          if (r < 0 || r >= 4 || c < 0 || c >= 4 || 
            (board[r][c] != cc && board[r][c] != 'T')) {
            ok = false;
            break;
          }

          r += mov[d][0];
          c += mov[d][1];
        }

        if (ok) return true;
      }
    }

    return false;
}

bool all_occupied() {
  for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++)
      if (board[i][j] == '.') return false;

  return true;      
}

game_status solve() {
  if (is_winner('X')) return X_WON;
  if (is_winner('O')) return O_WON;
  if (all_occupied()) return DRAW;
  return NOT_DONE;
}

void print_board() {
  for (int i = 0; i < 4; i++) printf("%s\n", board[i]);
}


int main() {

  scanf("%d", &N);

  for (int i = 1; i <= N; i++) {
    read_board();

    //print_board();
    
    printf("Case #%d: ", i);

    switch (solve()) {
    
    case X_WON:
      printf("X won\n");
      break;
    
    case O_WON:
      printf("O won\n"); 
      break;

    case DRAW:
      printf("Draw\n");
      break;

    case NOT_DONE:
      printf("Game has not completed\n");
      break;
    }
  }

  return 0;
}
