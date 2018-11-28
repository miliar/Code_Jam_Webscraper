#include <iostream>
#include <string>
#include <cstring>
using namespace std;


const char X_VICT='X';
const char O_VICT='O';
const char DRAW='T';
const char ONGOING='.';


char check_equals(char s[]) {
  int nX, nO, nT;
  nX=nO=nT=0;
  for (int i=0; i<4;++i) {
    if (s[i]=='X') nX++;
    if (s[i]=='O') nO++;
    if (s[i]=='T') nT++;
  }
  if ( nX==4 || (nX==3 && nT==1) ) 
    return X_VICT;
  if ( nO==4 || (nO==3 && nT==1) )
    return O_VICT;
  return DRAW;
}
  



char board_status(char board[4][5]) {
  int np=0;
  char diag1[4], diag2[4];
  for (int i=0; i<4;++i) {
    char r = check_equals(board[i]);
    if (r!=DRAW) return r;
    char vert[4];
    for (int j=0; j<4;++j) {
      if (i==j) diag1[i]=board[i][j];
      if (i==3-j) diag2[i]=board[i][j];
      vert[j]=board[j][i];
      np+=(int)(board[i][j]=='.');
    }
    r = check_equals(vert);
    if (r!=DRAW) return r;
  }
  char r = check_equals(diag1);
  if (r!=DRAW) return r;
  r = check_equals(diag2);
  if (r!=DRAW) return r;
  if (np==0) return DRAW;
  return ONGOING;
}


void print_sol(int t, char s) {
  string str;
  switch (s) {
  case X_VICT:
    str="X won";
    break;
  case O_VICT:
    str="O won";
    break;
  case DRAW:
    str="Draw";
    break;
  case ONGOING:
    str="Game has not completed";
    break;
  }
  

  cout << "Case #" << t << ": " << str << endl;
}

int main() {

  int T;

  cin >> T;

  for (int t=1; t<=T; ++t) {
    char board[4][5];
    for (int i=0; i<4;++i) 
      cin >> board[i];
    
    print_sol(t, board_status(board));
    


  }
  
  
  return 0;


}
