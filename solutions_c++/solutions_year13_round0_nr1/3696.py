#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int *read_board() { 
  int * result = new int[16];
  string s;

  for (int i = 0; i < 4; i++) {    
    getline(cin, s);
    //printf("> %s\n", s.c_str());
    for (int j = 0; j < 4; j++) {
      switch(s[j]) {
        case 'X':
          result[i*4 + j] = 1;
          break;
        case 'O':
          result[i*4 + j] = 2;
          break;
        case 'T':
          result[i*4 + j] = 3; 
          break;
        default:
          result[i*4 + j] = 0;
          break;
      }
    }
  }
  getline(cin, s);  
  return result;
}

int get_result(int * board) {
  // check if someone is won
  // rows
  char r;

  for (int i = 0; i < 4; i++) {
    r = board[i * 4];
    for (int j = 1; j < 4; j++) {
      r &= board[i* 4 + j];
    }
    if (r != 0) return r;
  }

  // columns
  for (int i = 0; i < 4; i++) {
    r = board[i];
    for (int j = 1; j < 4; j++) {
      r &= board[j * 4 + i];
    }
    if (r != 0) return r;
  }

  //diagonals
  r = board[0];
  for (int i = 1; i < 4; i++) { 
    r &= board[i * 4 + i];
  }
  if (r != 0) return r;

  r = board[3];
  for (int i = 1; i < 4; i++) { 
    r &= board[i * 4 + (3 - i)];
  }
  if (r != 0) return r;  

  // is completed?
  for (int i = 0; i < 16; i++) {
    if (board[i] == 0) return 0;
  }
  // draw!
  return 3;
}

int main(int argc, char const *argv[])
{
  freopen("input.txt", "r", stdin);
  int t;
  scanf("%d\n", &t);
  for (int i = 0; i < t; i++) {
    int *board = read_board();    
    printf("Case #%d: ", i + 1);
    switch(get_result(board)) {
      case 0:
        printf("Game has not completed\n");
        break;
      case 1:
        printf("X won\n");
        break;        
      case 2:
        printf("O won\n");
        break;                
      case 3:
        printf("Draw\n");
        break;           
    }
    delete [] board;
  }
  return 0;
}