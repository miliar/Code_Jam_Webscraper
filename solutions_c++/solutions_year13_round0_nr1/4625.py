#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool isfinished(vector<string>& b, char side) {
  for(int i = 0; i < 4; ++i) {
    bool win = true;
    for(int j = 0; j < 4; ++j)
      if(b[i][j] != side && b[i][j] != 'T')
        win = false;
    if(win)
      return true;
  }

  for(int i = 0; i < 4; ++i) {
    bool win = true;
    for(int j = 0; j < 4; ++j)
      if(b[j][i] != side && b[j][i] != 'T')
        win = false;
    if(win)
      return true;
  }

  bool win = true;
  for(int i = 0; i < 4; ++i)
    if(b[i][i] != side && b[i][i] != 'T')
      win = false;

  if(win)
    return true;

  win = true;
  for(int i = 0; i < 4; ++i)
    if(b[i][3-i] != side && b[i][3-i] != 'T')
      win = false;

  if(win)
    return true;

  return false;
}

int main () {
	int T;
	cin >> T;

  vector<string> b(4);
	for(int t = 0; t < T; ++t) {
    for(int i = 0; i < 4; ++i) {
      cin >> b[i];
    }

    int dot_count = 0;
    for(int i = 0; i < 4; ++i)
      for(int j = 0; j < 4; ++j)
        dot_count += (b[i][j] == '.');

		cout << "Case #" << t+1 << ": ";
    if(isfinished(b, 'X'))
      cout << "X won" << endl;
    else if(isfinished(b, 'O'))
      cout << "O won" << endl;
    else if(dot_count == 0)
      cout << "Draw" << endl;
    else 
      cout << "Game has not completed" << endl;
      
	}
	return 0;
}
