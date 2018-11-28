/*
 * Tic-Tac-Toe-Tomek.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: admin
 */

#include <cstdio>

#define SIZE 4
enum {
  XWON, OWON, DRAW, NOTCOMPLETE
};

int getStatus(char board[SIZE][SIZE]) {
  int xcount, ocount;
  bool done = true;
  for (int x = 0; x < SIZE; ++x) {
    xcount = ocount = 0;
    for (int y = 0; y < SIZE; ++y) {
      if (board[x][y] == 'X')
        xcount++;
      else if (board[x][y] == 'O')
        ocount++;
      else if (board[x][y] == 'T')
        xcount++, ocount++;
    }
    if (xcount == SIZE)
      return XWON;
    if (ocount == SIZE)
      return OWON;
    if (xcount == 0 || ocount == 0)
      done = false;
  }

  for (int y = 0; y < SIZE; ++y) {
    xcount = ocount = 0;
    for (int x = 0; x < SIZE; ++x) {
      if (board[x][y] == 'X')
        xcount++;
      else if (board[x][y] == 'O')
        ocount++;
      else if (board[x][y] == 'T')
        xcount++, ocount++;
    }
    if (xcount == SIZE)
      return XWON;
    if (ocount == SIZE)
      return OWON;
    if (xcount == 0 || ocount == 0)
      done = false;
  }

  xcount = ocount = 0;
  for (int x = 0; x < SIZE; ++x) {
    if (board[x][x] == 'X')
      xcount++;
    else if (board[x][x] == 'O')
      ocount++;
    else if (board[x][x] == 'T')
      xcount++, ocount++;
  }
  if (xcount == SIZE)
    return XWON;
  if (ocount == SIZE)
    return OWON;
  if (xcount == 0 || ocount == 0)
    done = false;

  xcount = ocount = 0;
  for (int x = 0; x < SIZE; ++x) {
    if (board[x][SIZE - 1 - x] == 'X')
      xcount++;
    else if (board[x][SIZE - 1 - x] == 'O')
      ocount++;
    else if (board[x][SIZE - 1 - x] == 'T')
      xcount++, ocount++;
  }
  if (xcount == SIZE)
    return XWON;
  if (ocount == SIZE)
    return OWON;
  if (xcount == 0 || ocount == 0)
    done = false;

  return done ? DRAW : NOTCOMPLETE;
}

int main() {
  int numTest;
  scanf("%d", &numTest);

  char board[SIZE][SIZE];
  char buff[SIZE + 1];

  for (int i = 1; i <= numTest; ++i) {
    printf("Case #%d: ", i);
    for (int x = 0; x < SIZE; ++x) {
      scanf("%s", buff);
      for (int y = 0; y < SIZE; ++y) {
        board[x][y] = buff[y];
      }
    }
    int status = getStatus(board);
    switch (status) {
    case XWON:
      printf("X won\n");
      break;
    case OWON:
      printf("O won\n");
      break;
    case DRAW:
      printf("Draw\n");
      break;
    default:
      printf("Game has not completed\n");
    }
  }

  return 0;
}

