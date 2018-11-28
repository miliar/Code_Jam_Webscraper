#include <iostream>
#include <map>
#include <vector>
#include <list>
#include <algorithm>
#include <string>
using namespace std;

char sequence(const string& str) {
  //cout << "string: " << str << endl;
  int i, j;
  // all X
  for (i = 0; i < 4; i++)
    if (str[i] != 'X' && str[i] != 'T')
      break;
  for (j = 0; j < 4; j++)
    if (str[j] != 'O' && str[j] != 'T')
      break;
  if (i == 4 && j == 4) return 'T';
  if (i == 4) return 'X';
  if (j == 4) return 'O';
  return 'D';
}

char checkBoard(const vector<string>& b) {
  // check row
  for (int i = 0; i < 4; i++) {
    string str("");
    for (int j = 0; j < 4; j++)
      str += b[i][j];
    char c = sequence(str);
    if (c != 'D') return c;
  }
  // check col
  for (int i = 0; i < 4; i++) {
    string str("");
    for (int j = 0; j < 4; j++)
      str += b[j][i];
    char c = sequence(str);
    if (c != 'D') return c;
  }
  // check diagonal
  string str1(""), str2("");
  for (int i = 0; i < 4; i++) {
    str1 += b[i][i];
    str2 += b[i][3 - i];
  }
  char c1 = sequence(str1);
  if (c1 != 'D') return c1;
  char c2 = sequence(str2);
  if (c2 != 'D') return c2;
  
  return 'D';
}

bool full(const vector<string>& b) {
  for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++)
      if (b[i][j] == '.') return false;
  return true;
}

int main() 
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
      vector<string> board(4, "....");
      for (int i = 0; i < 4; i++) 
	cin >> board[i];
      char res = checkBoard(board);
      cout << "Case #" << t << ": ";
      switch(res) {
      case 'X':
	cout << "X won" << endl;
	break;
      case 'O':
	cout << "O won" << endl;
	break;
      case 'D':
	{
	  if (full(board)) cout << "Draw" << endl;
	  else cout << "Game has not completed" << endl;
	  break;
	}
      }
    }
    return 0;    
}
