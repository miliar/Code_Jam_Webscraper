#include <iostream>

using namespace std;

template <typename S>
char WinnerOneDirection(const char testCase[4][4], unsigned int maxRows, unsigned int maxCols,  S selector) {
  unsigned int X,O,T;
  for(unsigned int i=0;i<maxRows;i++) {
    X=O=T=0;
    for(unsigned int j=0;j<maxCols;j++) {
      switch(selector(testCase, i, j)) {
	case 'X':
	  X++;
	  break;
	case 'O':
	  O++;
	  break;
	case 'T':
	  T++;
	  break;
	case '.':
	  break;
	default:
	  cout << "Invalid input" <<std::endl;
      }
    }
    
    unsigned int neededToWin = 4 - T;
    if(X==neededToWin)
      return 'X';
    else if(O==neededToWin)
      return 'O';
  }
  return '.';
}


char GetWinner(const char testCase[4][4]) {
  auto rowsGetter = [](const char arr[4][4], unsigned int i, unsigned int j) { return arr[i][j]; };
  auto colsGetter = [](const char arr[4][4], unsigned int i, unsigned int j) { return arr[j][i]; };
  auto diag1Getter = [](const char arr[4][4], unsigned int i, unsigned int j) { return arr[j][j]; };
  auto diag2Getter = [](const char arr[4][4], unsigned int i, unsigned int j) { return arr[j][3-j]; };
  
  char winner;
  
  
  winner = WinnerOneDirection(testCase, 4, 4, rowsGetter);
  if (winner != '.') return winner;
  winner = WinnerOneDirection(testCase, 4, 4, colsGetter);
  if (winner != '.') return winner;
  winner = WinnerOneDirection(testCase, 1, 4, diag1Getter);
  if (winner != '.') return winner;
  winner = WinnerOneDirection(testCase, 1, 4, diag2Getter);
  if (winner != '.') return winner;
}

bool GameEnded(const char testCase[4][4]) {
  for(unsigned int i=0;i<4;i++) {
    for(unsigned int j=0;j<4;j++) {
      if(testCase[i][j] == '.') return false;
    }
  }
  return true;
}

int main() {

  //read the input
  unsigned int nTests;
  cin >> nTests;

  char testCase[4][4];
  for(unsigned int test = 1; test <= nTests; test++) {
    
    for(unsigned int i = 0; i < 4; i++)
      cin >> testCase[i][0] >> testCase[i][1] >> testCase[i][2] >> testCase[i][3]; 
    //PrintTestCase(testCase);
    char winner = GetWinner(testCase);
    if(winner=='.') {
      if(GameEnded(testCase)) {
	cout << "Case #" << test << ": Draw" << endl;
      } else {
	cout << "Case #" << test << ": Game has not completed" << endl;
      }
    } else {
      cout << "Case #" << test << ": " << winner << " won" << endl;
    }
    
  }

}