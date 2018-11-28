#include <iostream>

#define	X	'X'
#define	O	'O'
#define	DOT	'.'
#define	T	'T'

#define	SIZE	4

using namespace std;

char board[4][4];

bool checkPlayer(char who) {
    int i, j;
    
//     cout << "Checking vertically..." << endl;
    // Check vertically.
    for (j = 0; j < SIZE; ++j) {
      i = 0;
      while (i < SIZE && (board[i][j] == who || board[i][j] == T)) {
	i++;
      }
      if (i == SIZE)
	return true;
    }

//     cout << "Checking horizontally..." << endl;    
    // Check horizontally.
    for (i = 0; i < SIZE; ++i) {
      j = 0;
      while (j < SIZE && (board[i][j] == who || board[i][j] == T)) {
	++j;
      }
      if (j == SIZE)
	return true;
    }

//     cout << "Checking diagonally..." << endl;   
    // Check diagonally.
    i = 0; j = 0;
    while(i < SIZE && (board[i][j] == who || board[i][j] == T)) {
      ++i; ++j;
    }
    if (i == SIZE)
      return true;

//     cout << "Checking antidiagonally..." << endl;   
    // Check antidiagonally.
    i = SIZE - 1; j = 0;
    while (i >= 0 && (board[i][j] == who || board[i][j] == T)) {
      --i; ++j;
    }
    if (i < 0)
      return true;

    return false;
}

bool areAllSymbols() {
  for (int i = 0; i < SIZE; ++i) {
      for (int j = 0; j < SIZE; ++j) {
	if (board[i][j] == DOT)
	  return false;
      }
  }
    
  return true;
}

int main () {
  int nT;
  
  cin >> nT;
  
  for (int t = 0; t < nT; ++t) {
    
    // Read input.
    for (int i = 0; i < SIZE; ++i) {
      for (int j = 0; j < SIZE; ++j) {
	cin >> board[i][j];
      }
    }
    
    bool wonX = checkPlayer(X);
    bool wonO = false;
    if (!wonX)
      wonO = checkPlayer(O);
    
    bool gameHasCompleted = true;
    
    if (!wonX && ! wonO)
      gameHasCompleted = areAllSymbols();
    
    string result;
    
    if (wonX) {
      result = "X won";
    } else {
      if (wonO) {
	result = "O won";
      } else {
	if (gameHasCompleted) {
	  result = "Draw";
	} else {
	  result = "Game has not completed";
	}
      }
    }
    
    cout << "Case #" << t + 1 << ": " << result << endl;
    
  }
  
}