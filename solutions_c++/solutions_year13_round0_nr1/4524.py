#include <iostream>
#include <stack>
#include <cstdio>
#include <math.h>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <iterator>
using namespace std;

#define A first
#define B second

int main()
{
  int i, j, T;
  bool full, win;
  char c, board[4][4];
  int countH[256], countV[256];
  cin >> T;
  
  for (int t=1; t<=T; ++t)
  {
    for (i=0; i<4; ++i)
      for (j=0; j<4; ++j)
      {
        do
        {
          scanf("%c", &c);
        }
        while (c != 'X' && c != 'T' && c != 'O' && c!= '.');
        board[i][j] = c;
      }
    win = false;
    full = true;
    for (i=0; i<4; ++i)
    {
      countH['X'] = countH['T'] = countH['.'] = countH['O'] = 0;
      countV['X'] = countV['T'] = countV['.'] = countV['O'] = 0;
      for (j=0; j<4; ++j)
      {
        ++countH[board[i][j]];
        ++countV[board[j][i]];
        if (board[i][j] == '.')
          full = false;
      }
      
      if (countH['O'] + countH['T'] == 4 || countV['O'] + countV['T'] == 4)
      {
        cout << "Case #" << t << ": O won\n";
        win = true;
        break;
      }
      else if (countH['X'] + countH['T'] == 4 || countV['X'] + countV['T'] == 4)
      {
        cout << "Case #" << t << ": X won\n";
        win = true;
        break;
      }
    }
    if (!win)
    {
      countH['X'] = countH['T'] = countH['.'] = countH['O'] = 0;
      countV['X'] = countV['T'] = countV['.'] = countV['O'] = 0;
      for (i=0; i<4; ++i)
      {
        ++countH[board[i][i]];
        ++countV[board[i][3-i]];
      }
      if (countH['O'] + countH['T'] == 4 || countV['O'] + countV['T'] == 4)
        cout << "Case #" << t << ": O won\n";
      else if (countH['X'] + countH['T'] == 4 || countV['X'] + countV['T'] == 4)
        cout << "Case #" << t << ": X won\n";
      else if (full)
        cout << "Case #" << t << ": Draw\n";
      else
        cout << "Case #" << t << ": Game has not completed\n";
    }
  }
	return 0;
}
