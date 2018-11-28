#include <cstdio>
using namespace std;

char board[8][8];

void input(){
  for (int i = 0; i < 4; ++ i) {
    scanf("%s", board + i);
  }
}

char solve(){
  int nx, no, nd = 0, nt;
  for (int i = 0; i < 4; ++ i){
    nx = no = nt = 0;
    for (int j = 0;  j < 4; ++ j){
      if (board[i][j] == 'X') {
        ++ nx;
      } else if (board[i][j] == 'O') {
        ++ no;
      } else if (board[i][j] == '.') {
        ++ nd;
      } else {
        ++ nt;
      }
    }
    if (nt + nx == 4) return 'X';
    if (nt + no == 4) return 'O';
  }
  for (int i = 0; i < 4; ++ i){
    nx = no = nt = 0;
    for (int j = 0;  j < 4; ++ j){
      if (board[j][i] == 'X') {
        ++ nx;
      } else if (board[j][i] == 'O') {
        ++ no;
      } else if (board[j][i] == 'T') {
        ++ nt;
      }
    }
    if (nt + nx == 4) return 'X';
    if (nt + no == 4) return 'O';
  }
  nx = no = nt = 0;
  for (int i = 0; i < 4; ++ i){
    if (board[i][i] == 'X') {
      ++ nx;
    } else if (board[i][i] == 'O') {
      ++ no;
    } else if (board[i][i] == 'T') {
      ++ nt;
    }
  }
  if (nt + nx == 4) return 'X';
  if (nt + no == 4) return 'O';
  nx = no = nt = 0;
  for (int i = 0; i < 4; ++ i){
    if (board[3 - i][i] == 'X') {
      ++ nx;
    } else if (board[3 - i][i] == 'O') {
      ++ no;
    } else if (board[3 - i][i] == 'T') {
      ++ nt;
    }
  }
  if (nt + nx == 4) return 'X';
  if (nt + no == 4) return 'O';
  if (nd > 0) return 'N';
  return 'D';
}

int main(){
  int t;
  scanf("%d", &t);
  for (int c = 1; c <= t; ++ c){
    input();
    char r = solve();
    printf("Case #%d: ", c);
    if (r == 'X')
      puts("X won");
    else if (r == 'O')
      puts("O won");
    else if (r == 'D')
      puts("Draw");
    else
      puts("Game has not completed");
  }
  return 0;
}
