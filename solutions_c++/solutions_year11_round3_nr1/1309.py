//
//  code_jam
//
//  Created by Paul O'Neil on 5/20/11.
//  Copyright 2011 Paul O'Neil. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

#define BLUE '#'
#define WHITE '.'
#define TOP_LEFT '/'
#define TOP_RIGHT '\\'
#define BOT_LEFT '\\'
#define BOT_RIGHT '/'

void print_board(char * board, int rows, int cols) {
  for( int r = 0; r < rows; r++ ) {
    for( int c = 0; c < cols; c++ ) {
      cout << board[r*cols + c];
    }
    cout << endl;
  }
}

#define PRINT_BOARD()   print_board(&(board[0][0]), rows, cols)

void do_trial(istream & input) throw() {
  int rows, cols;
  input >> rows >> cols;
  
  char board[rows][cols];
  for( int r = 0; r < rows; r++ ) {
    for( int c = 0; c < cols; c++ ) {
      input >> board[r][c];
    }
  }
  
  for( int r = 0; r < rows - 1; r++ ) {
    for( int c = 0; c < cols - 1; c++ ) {
      if( board[r][c] == BLUE ) {
        // check the other 3 parts of this tile
        if( board[r][c+1]   == BLUE &&
            board[r+1][c]   == BLUE &&
           board[r+1][c+1] == BLUE ) {
          board[r][c]     = TOP_LEFT;
          board[r][c+1]   = TOP_RIGHT;
          board[r+1][c]   = BOT_LEFT;
          board[r+1][c+1] = BOT_RIGHT;
        }
        else {
          goto broken;
        }
      }
    }
  }
  
  for( int r = 0; r < rows; r++ ) {
    for( int c = 0; c < cols; c++ ) {
      if( board[r][c] == BLUE ) {
        goto broken;
      }
    }
  }
  
  PRINT_BOARD();
  
  return;
  
broken:
  cout << "Impossible\n";
  return;
}

int main (int argc, const char * argv[])
{
  int trialCount;
  istream * in;
  if( argc == 1 ) {
    in = &cin;
  }
  else {
    in = new ifstream(argv[1]);
  }
  istream & input = *in;
  input >> trialCount;
  
  for( int i = 1; i <= trialCount; i ++ ) {
    cout << "Case #" << i << ":" << endl;
    do_trial(input);
  }
  
  if( argc > 1 ) {
    delete in;
  }
  return 0;
}
