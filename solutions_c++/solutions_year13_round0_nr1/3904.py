#include <stdio.h>
#include <stdlib.h>

using namespace std;

char board[5][5];

void printboard() {
  for (int i = 0;i < 4;i++) {
    for (int j = 0;j < 4;j++) {
      printf("%c",board[i][j]);
    }
    printf("\n");
  }
  printf("------------\n");

}

bool process(int c,int r,bool &incomplete) {
  if (r == 1) {
    printf("Case #%d: X won\n",c);
    return true;
  }
  if (r == 2) {
    printf("Case #%d: O won\n",c);
    return true;
  }
  if (r == -1) {
    incomplete = true;
    return false;
  }
  return false;
}

//return 0 = no winner
int check(char a,char b,char c,char d) {
  bool x = false;
  bool o = false;
  bool t = false;
  if (a == '.' || b == '.' || c == '.' || d == '.') return -1;
  if (a == 'X' || b == 'X' || c == 'X' || d == 'X') x = true;
  if (a == 'O' || b == 'O' || c == 'O' || d == 'O') o = true;
  //if (a == 'T' || b == 'T' || c == 'T' || d == 'T') t = true;
  if (x && o) return 0;
  if (x) return 1; else return 2;
}

int main()
{
  freopen("A-large.in","r",stdin);
  int T;
  scanf("%d\n",&T);
  for (int i = 1;i <= T;i++) {
    // read board
    char st[10];
    gets(board[0]);
    gets(board[1]);
    gets(board[2]);
    gets(board[3]);
    gets(st);
    //printboard();

    //check
    int r;
    bool incomplete;
    incomplete = false;
    // horizontal
    r = check(board[0][0],board[0][1],board[0][2],board[0][3]); if (process(i,r,incomplete)) continue;
    r = check(board[1][0],board[1][1],board[1][2],board[1][3]); if (process(i,r,incomplete)) continue;
    r = check(board[2][0],board[2][1],board[2][2],board[2][3]); if (process(i,r,incomplete)) continue;
    r = check(board[3][0],board[3][1],board[3][2],board[3][3]); if (process(i,r,incomplete)) continue;

    // vertical
    r = check(board[0][0],board[1][0],board[2][0],board[3][0]); if (process(i,r,incomplete)) continue;
    r = check(board[0][1],board[1][1],board[2][1],board[3][1]); if (process(i,r,incomplete)) continue;
    r = check(board[0][2],board[1][2],board[2][2],board[3][2]); if (process(i,r,incomplete)) continue;
    r = check(board[0][3],board[1][3],board[2][3],board[3][3]); if (process(i,r,incomplete)) continue;

    // diagonal
    r = check(board[0][0],board[1][1],board[2][2],board[3][3]); if (process(i,r,incomplete)) continue;
    r = check(board[0][3],board[1][2],board[2][1],board[3][0]); if (process(i,r,incomplete)) continue;

    if (incomplete) printf("Case #%d: Game has not completed\n",i); else printf("Case #%d: Draw\n",i);


  }
}
