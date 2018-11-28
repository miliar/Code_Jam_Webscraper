#include <cstdio>
#include <cassert>
#include <cstring>


typedef enum {
  XWON,
  OWON,
  DRAW,
  NOTCOMPLETE
} result_t;

const char * ans[] =
{
  "X won",
  "O won",
  "Draw",
  "Game has not completed"
};

char scratch[5];
void solve(int tc) {
  char board[4][5];
  result_t res = DRAW;

  for (int i = 0; i < 4; ++i)
    gets(&board[i][0]);
  gets(&scratch[0]);
  assert(scratch[0] == '\0');

  int horiz[4][128], vert[4][128], diag[2][128];
  memset(horiz, 0, sizeof horiz);
  memset(vert, 0, sizeof vert);
  memset(diag, 0, sizeof diag);
  bool empties = false;

  for (int r = 0; r < 4; ++r) {
    for (int c = 0; c < 4; ++c) {
      char ch = board[r][c];
      if (r == c) {
        diag[0][ch] += 1;
      } else if (r == 3-c) {
        diag[1][ch] += 1;
      }
      horiz[r][ch] += 1;
      vert[c][ch] += 1;

      empties = empties || ch == '.';
    }
  }

  // check for winners
  for (int i = 0; i < 4; ++i) {
    if ( (vert[i]['X'] + vert[i]['T'] == 4) ||
         (horiz[i]['X'] + horiz[i]['T'] == 4) ) {
      res = XWON;
      break;
    } else if ( (vert[i]['O'] + vert[i]['T'] == 4) ||
         (horiz[i]['O'] + horiz[i]['T'] == 4) ) {
      res = OWON;
      break;
    }
  }
  if (diag[0]['X'] + diag[0]['T'] == 4 ||
      diag[1]['X'] + diag[1]['T'] == 4) {
    res = XWON;
  } else if (diag[0]['O'] + diag[0]['T'] == 4 ||
      diag[1]['O'] + diag[1]['T'] == 4) {
    res = OWON;
  }

  if (res == DRAW && empties) res = NOTCOMPLETE;

  printf("Case #%d: %s\n", tc, ans[res]);
}

int main() {
  int T;
  scanf("%d\n", &T);
  for (int i = 0; i < T; ++i)
    solve(i+1);
  return 0;
}
