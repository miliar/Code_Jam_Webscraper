#include <iostream>
#include <climits>
#include <algorithm>

using namespace std;

char board[4][5];

bool lined(int r, int c, int dr, int dc, char ch){
  bool ok = true;
  for(int k = 0; k < 4; ++k, r += dr, c += dc){
    ok &= board[r][c] == ch || board[r][c] == 'T';
  }
  return ok;
}

bool won(char ch){
  if(lined(0, 0, 1, 1, ch) || lined(0, 3, 1, -1, ch)) return true;
  for(int k = 0; k < 4; ++k){
    if(lined(k, 0, 0, 1, ch)) return true;
    if(lined(0, k, 1, 0, ch)) return true;
  }
}

bool draw(void){
  for(int r = 0; r < 4; ++r)
    if(find(board[r], board[r]+4, '.') != board[r]+4)
      return false;
  return true;
}

int main(void){
  int T;
  cin >> T;
  cin.ignore(INT_MAX, '\n');
  for(int x = 0; x < T; ++x){
    for(int i = 0; i < 4; ++i){
      cin.read(board[i], sizeof(char)*4);
      cin.ignore(INT_MAX, '\n');
    }
    cin.ignore(INT_MAX, '\n');

    cout << "Case #" << x+1 << ": ";
    if(won('X'))
      cout << "X won" << endl;
    else if(won('O'))
      cout << "O won" << endl;
    else if(draw())
      cout << "Draw" << endl;
    else
      cout << "Game has not completed" << endl;
  }
  return 0;
}
