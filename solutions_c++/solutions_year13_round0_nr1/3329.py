//------------------------------------------------------------------------------
// Copyright (c) 2013 Mineyuki Iwasaki. All rights reserved.
//------------------------------------------------------------------------------
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#define LOG(f,...) fprintf(stderr, f, __VA_ARGS__)
using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  // Loop
  char buffer[5][5];
  bool result = false;
  bool completed = true;
  for (int t = 0; t != T; ++t) {
    //    printf("t=%d,T=%d\n", t, T);
    result = false;
    completed = true;

    gets(&buffer[4][0]);
    gets(&buffer[0][0]);
    gets(&buffer[1][0]);
    gets(&buffer[2][0]);
    gets(&buffer[3][0]);

    // Check horizontal.
    for (int j=0; j!=4; ++j) {
      bool success = true;
      char won = 0;
      for (int i=0; i!=4; ++i) {
        if (buffer[j][i] == '.') {
          success = false;
          completed = false;
          break;
        } else if (won == 0) {
          if (buffer[j][i] == 'X') {
            won = 'X';
          } else if (buffer[j][i] == 'O') {
            won = 'O';
          }
        } else if (buffer[j][i] != won && buffer[j][i] != 'T') {
          success = false;
          break;
        }
      }
      if (success) {
        printf("Case #%d: %c won\n", t+1, won);
        result = true;
        break;
      }
    }

    // Check horizontal.
    if (!result) {
      for (int j=0; j!=4; ++j) {
        bool success = true;
        char won = 0;
        for (int i=0; i!=4; ++i) {
          if (buffer[i][j] == '.') {
            success = false;
            completed = false;
            break;
          }
          else if (won == 0) {
            if (buffer[i][j] == 'X') {
              won = 'X';
            } else if (buffer[i][j] == 'O') {
              won = 'O';
            }
          } else if (buffer[i][j] != won && buffer[i][j] != 'T') {
            success = false;
            break;
          }
        }
        if (success) {
          printf("Case #%d: %c won\n", t+1, won);
          result = true;
          break;
        }
      }
    }

    // Check diagonal 1.
    if (!result) {
      bool success = true;
      char won = 0;
      for (int j=0; j!=4; ++j) {
        if (buffer[j][j] == '.') {
          success = false;
          completed = false;
          break;
        }
        else if (won == 0) {
          if (buffer[j][j] == 'X') {
            won = 'X';
          } else if (buffer[j][j] == 'O') {
            won = 'O';
          }
        } else if (buffer[j][j] != won && buffer[j][j] != 'T') {
          success = false;
          break;
        }
      }
      if (success) {
        printf("Case #%d: %c won\n", t+1, won);
        result = true;
      }
    }

    // Check diagonal 2.
    if (!result) {
      bool success = true;
      char won = 0;
      for (int j=0; j!=4; ++j) {
        if (buffer[3-j][j] == '.') {
          success = false;
          completed = false;
          break;
        }
        else if (won == 0) {
          if (buffer[3-j][j] == 'X') {
            won = 'X';
          } else if (buffer[3-j][j] == 'O') {
            won = 'O';
          }
        } else if (buffer[3-j][j] != won && buffer[3-j][j] != 'T') {
          success = false;
          break;
        }
      }
      if (success) {
        printf("Case #%d: %c won\n", t+1, won);
        result = true;
      }
    }

    // Other
    if (!result) {
      if (completed) {
        printf("Case #%d: Draw\n", t+1);
      } else {
        printf("Case #%d: Game has not completed\n", t+1);
      }
    }
  }
  return 0;
}
