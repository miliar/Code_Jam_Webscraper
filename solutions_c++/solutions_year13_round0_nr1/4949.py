#include <iostream>
#include <vector>

using namespace std;


// Returns 'X' if 'X' wins, 'O' if O wins 'D' if draw and 'G' if game
// is unfinshed.
char checkStatus(const vector< vector<char> >& gameBoard) {
  char startChar = 'a';
  bool win = true;
  bool dotDetected = false;
  // First check rows
  for (int i=0; i<4; i++) {
    win = true;
    startChar = gameBoard[i][0];
    if (startChar == 'T') {
      startChar = gameBoard[i][1];
    }
    if (startChar == '.') {
      continue;
    }
    for (int j=1; j<4; j++) {
      if (gameBoard[i][j] != startChar && gameBoard[i][j] != 'T') {
	win = false;
	break;
      }
    }
    if (win) {
      return startChar;
    }
  }
  // Check cols

  for (int i=0; i<4; i++) {
    win = true;
    startChar = gameBoard[0][i];
    if (startChar == 'T') {
      startChar = gameBoard[1][i];
    }
    if (startChar == '.') {
      continue;
    }
    for (int j=1; j<4; j++) {
      if (gameBoard[j][i] != startChar && gameBoard[j][i] != 'T') {
	win = false;
	break;
      }
    }
    if (win) {
      return startChar;
    }
  }
  // Check first diag
  win = true;
  startChar = gameBoard[0][0];
  if (startChar == 'T') {
    startChar = gameBoard[1][1];
  }
  if (startChar != '.') {
    for (int i=1; i<4; i++) {
      if (gameBoard[i][i] != startChar && gameBoard[i][i] != 'T') {
	win = false;
	break;
      }
    }
  } else {
    win = false;
  }
  if (win) {
    return startChar;
  }

  // Check second diag
  win = true;
  startChar = gameBoard[3][0];
  if (startChar == 'T') {
    startChar = gameBoard[2][1];
  }
  if (startChar != '.') {
    for (int i=1; i<4; i++) {
      if (gameBoard[3-i][i] != startChar && gameBoard[3-i][i] != 'T') {
	win = false;
	break;
      }
    }
  } else {
    win = false;
  }
  if (win) {
    return startChar;
  }  
  // Check for draw
  for (int i=0; i<4; i++) {
    for (int j=0; j<4; j++) {
      dotDetected = (gameBoard[i][j] == '.');
      if (dotDetected) {
	return 'G';
      }
    }
  }
  return 'D';
}

int main() {
  int T;
  cin >> T;
  vector< vector<char> > gameBoard(4, vector<char>(4, '.'));
  char status;
  for (int i=0; i<T; i++) {
    // Read game board
    for (int j=0; j<4; j++) {
      for (int k=0; k<4; k++) {
	cin >> gameBoard[j][k];
      }
    }
    status = checkStatus(gameBoard);
    switch(status) {
    case 'X': cout << "Case #" << i+1 << ": X won" << endl;
      break;
    case 'O': cout << "Case #" << i+1 << ": O won" << endl;
      break;
    case 'G': cout << "Case #" << i+1 << ": Game has not completed" << endl;
      break;
    default : cout << "Case #" << i+1 << ": Draw" << endl;
      break;
    }
  }
}
