#include<fstream>
#include<iostream>
#include<cstdio>

using namespace std;

#define FL(i, a, b) for(int i = a; i < b; i++)
#define MIN(a, b) ((a > b)? b : a)
#define MAX(a, b) ((a > b)? a : b)

char* output(int result) {
  switch (result) {
    case 0:
      return "Game has not completed";
    case 1:
      return "X won";
    case 2:
      return "O won";
    case 3:
      return "Draw";
    default:
      cout<<"qq\n";
  }
}

void add(char c, int &o, int &x, int &t) {
  switch (c) {
    case 'O':
      o++; break;
    case 'X':
      x++; break;
    case 'T':
      t++; break;
    case '.':
      break;
    default:
      cout<<"zz\n";
  }
}

int check(char a, char b, char c, char d) {
  int o,x,t;
  o = x = t = 0;
  add(a, o, x, t);
  add(b, o, x, t);
  add(c, o, x, t);
  add(d, o, x, t);

  if (t == 1) {
    if (x == 3)
      return 1;
    if (o == 3)
      return 2;
  } 
  if (x == 4)
    return 1;
  if (o == 4)
    return 2;
  return 0;
}

int main(int argc, char *argv[]) {
  if (argc != 2) {
    printf("file input\n");
    return -1;
  }

  ifstream fin(argv[1]);

  int T;
  char board[4][4];
  fin>>T;
  FL(t, 0, T) {
    FL(i, 0, 4)
    FL(j, 0, 4)
      fin>>board[i][j];

    int result = 0;
    // Dia 1
    result = check(board[0][0], board[1][1], board[2][2], board[3][3]);
    // Dia 2
    if (result == 0)
      result = check(board[0][3], board[1][2], board[2][1], board[3][0]);
    // Row
    if (result == 0) {
      FL(i,0,4) {
        result = check(board[i][0], board[i][1], board[i][2], board[i][3]);
        if (result > 0)
          break;
      }
    }
    // Col
    if (result == 0) {
      FL(i,0,4) {
        result = check(board[0][i], board[1][i], board[2][i], board[3][i]);
        if (result > 0)
          break;
      }
    }

    // Check full
    if (result == 0) {
      int x,o,t;
      x = o = t = 0;
      FL(i, 0, 4)
      FL(j, 0, 4)
        add(board[i][j], o, x, t);
      result = (o + x + t == 16)? 3: 0;
    }

    printf("Case #%d: %s\n", t + 1, output(result));
  }
  return 0;
}
