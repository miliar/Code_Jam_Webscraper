#include <stdio.h>

char board[100][100];
int R,C;

int main() {
  int T;
  scanf("%d", &T);
  for (int TT=1;TT<=T;++TT) {
    scanf("%d %d\n", &R, &C);
    for (int i=0;i<R;++i)
      scanf("%s", board[i]);
    bool works = true;
    for (int i=0;i<R-1;++i) {
      for (int j=0;j<C-1;++j)
	if (board[i][j] == '#') {
	  if (board[i+1][j] != '#' || board[i][j+1] != '#' || board[i+1][j+1] != '#') {
	    works = false;
	    break;
	  }
	  board[i][j] = '/';
	  board[i+1][j] = '\\';
	  board[i][j+1] = '\\';
	  board[i+1][j+1] = '/';
	}
      if (!works) break;
    }
    for (int i=0;i<R;++i)
      if (board[i][C-1] == '#') {works=false;break;}
    for (int i=0;i<C;++i)
      if (board[R-1][i] == '#') {works=false;break;}
    if (!works) {
      printf("Case #%d:\nImpossible\n", TT);
    } else {
      printf("Case #%d:\n", TT);
      for (int i=0;i<R;++i)
	printf("%s\n", board[i]);
    }
  }
  return 0;
}
