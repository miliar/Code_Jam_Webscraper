#include <vector>
#include <iostream>
#include <cstdlib>
#include <map>
#include <algorithm>
#include <iterator>
#include <set>
#include <list>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
#include <string>
#include <stack>
#include <queue>

using namespace std;
using namespace std::tr1;

int main()
{
  int T;
  cin >> T;
  int R, C;
  char c;
  for (int caseNumber = 1;caseNumber <= T;++caseNumber) {
    cin >> R >> C;
    vector<vector<char> > originalBoard(R,vector<char>(C,'\0'));
    for (int row = 0;row < R;++row) {
      for (int col = 0;col < C;++col) {
	cin >> c;
	originalBoard[row][col] = c;
      }
    }

    bool isPossible = true;
    for (int row = 0;row < R;++row) {
      for (int col = 0;col < C;++col) {
	if (originalBoard[row][col] == '#') {
	  if (row == R-1 || col == C-1) {
	    isPossible = false;
	  break;
	  } else if (originalBoard[row+1][col] == '#' &&
		     originalBoard[row+1][col+1] == '#' &&
		     originalBoard[row][col+1] == '#') {
	    originalBoard[row][col] = '/';
	    originalBoard[row+1][col] = '\\';
	    originalBoard[row][col+1] = '\\';
	    originalBoard[row+1][col+1] = '/';
	  } else {
	    isPossible = false;
	    break;
	  }
	}
      }
      if (!isPossible) {
	break;
      }
    }

    cout << "Case #" << caseNumber
	 << ":" << endl;

    if (isPossible) {
      for (int row = 0;row < R;++row) {
	for (int col = 0;col < C;++col) {
	  cout << originalBoard[row][col];
	}
	cout << endl;
      }
    } else {
      cout << "Impossible" << endl;
    }
  }
  return 0;
}
