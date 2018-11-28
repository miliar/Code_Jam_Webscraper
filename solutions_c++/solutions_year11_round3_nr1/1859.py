#pragma warning(disable:4996)
#include <cstdio>
#include <algorithm>
using namespace std;

int main(void)
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "wt", stdout);

  int no_case;
  scanf("%d", &no_case);

  char board[50][50];

  for(int i=1; i<=no_case; i++) {
    int R, C;
    scanf("%d %d", &R, &C);

    char buffer[52];
    for(int i=0; i<R; i++) {
      scanf("%s", buffer);
      for(int j=0; j<C; j++) {
        board[i][j] = buffer[j];
      }
    }

    for(int i=0; i<R; i++) {
      for(int j=0; j<C; j++) {
        if(board[i][j] == '#') {
          if((j != C-1 && board[i][j+1] == '#') &&
             (i != R-1 && board[i+1][j] == '#') &&
             (board[i+1][j+1] == '#'))
          {
            board[i][j] = board[i+1][j+1] = '/';
            board[i][j+1] = board[i+1][j] = '\\';
          }
          else {
            goto IMPOSSIBLE;
          }
        }
      }
    }
    printf("Case #%d:\n", i);

    for(int i=0; i<R; i++) {
      for(int j=0; j<C; j++) {
        printf("%c", board[i][j]);
      }
      printf("\n");
    }
    continue;

IMPOSSIBLE:
    printf("Case #%d:\nImpossible\n", i);
  }

  return 0;
}
