#include<stdio.h>

#include <string>

using namespace std;

char board[10][10];


bool won(char p) {

  for (int i = 0; i < 4; i ++) {
    bool w = true;
    for (int r = 0; r < 4; r++) {
      if ((board[i][r] != p) && 
	  (board[i][r] != 'T')) {
	w = false;
      }
    }
    if (w) return true;
  }

  for (int i = 0; i < 4; i ++) {
    bool w = true;
    for (int r = 0; r < 4; r++) {
      if ((board[r][i] != p) && 
	  (board[r][i] != 'T')) {
	w = false;
      }
    }
    if (w) return true;
  }
  
  bool w = true;
  for (int r = 0; r < 4; r++) {
    if ((board[r][r] != p) && 
	(board[r][r] != 'T')) {
      w = false;
    }
  }
  if (w) return true;

  w = true;
  
  for (int r = 0; r < 4; r++) {
    if ((board[r][3-r] != p) && 
	(board[r][3-r] != 'T')) {
      w = false;
    }
  }

  if (w) return true;
  
  return false;
}

std::string st() {

  if (won('X')) {
    return "X won";
  }
  if (won('O'))
      return "O won";
  
  for (int i = 0; i < 4; i ++) {
    for (int r = 0; r < 4; r++) {
      if (board[i][r] == '.' ) {
	//	printf("line is %s\n",board[i]);
	return "Game has not completed";
      }
    }
  }
  return "Draw";
}

main() {

  int T;
  char line[10];

  scanf("%d",&T);

  for (int t = 1; t <= T; t++) {
    for (int l = 0; l < 4; l++) {
      scanf("%s",board[l]);
      //  printf("li \"%s\"",board[l]);
    }
    
    string result = st();
  
    printf("Case #%d: %s\n",t,result.c_str());
    
  }
  


}
