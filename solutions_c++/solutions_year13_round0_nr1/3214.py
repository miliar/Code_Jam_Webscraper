#include <iostream>
#include <vector>
#include <algorithm>

#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

const int X_WON = 1;
const int O_WON = 2;
const int DRAW = 3;
const int NOT_FINISHED = 4;

int solve(const vector<vector<int> >& field)
{
  bool not_finished = false;
  
  // vertical line
  for (int col = 0; col < 4; ++col) {
    int sum = 0;
    for (int i = 0; i < 4; ++i) {
      sum += field[i][col];
      if (!field[i][col]) not_finished = true;
    }
    if (sum == 4 || sum == 13) return X_WON;
    if (sum == -4 || sum == 7) return O_WON;
  }
  
  // horizontal line
  for (int row = 0; row < 4; ++row) {
    int sum = 0;
    for (int i = 0; i < 4; ++i)
      sum += field[row][i];
    if (sum == 4 || sum == 13) return X_WON;
    if (sum == -4 || sum == 7) return O_WON;
  }
  
  // diagonal line
  for (int dir = 0; dir < 2; ++dir) {
    int sum = 0;
    for (int i = 0; i < 4; ++i) {
      sum += field[dir ? i : 3 - i][i];
    }
    if (sum == 4 || sum == 13) return X_WON;
    if (sum == -4 || sum == 7) return O_WON;
  }
  
  if (not_finished) return NOT_FINISHED;
  return DRAW;
}

int main()
{
  int T;
  cin >> T;
  
  for (int cs = 1; cs <= T; ++cs) {
    vector<vector<int> > field(4, vector<int>(4, 0));
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
	char ch;
	int val = 255;
	cin >> ch;
	
	switch (ch) {
	case 'X': val = 1; break;
	case 'O': val = -1; break;
	case '.': val = 0; break;
	case 'T': val = 10; break;
	default: break;
	}

	field[i][j] = val;
      }
    }

    cout << "Case #" << cs << ": ";
    
    int ans = solve(field);
    switch (ans) {
    case X_WON: cout << "X won" << endl; break;
    case O_WON: cout << "O won" << endl; break;
    case DRAW: cout << "Draw" << endl; break;
    case NOT_FINISHED: cout << "Game has not completed" << endl;
    }
  }

  return 0;
}

