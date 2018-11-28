#include <iostream>
#include <string>
#include <vector>

using namespace std;

string board[4];
char win(int x, int y, int dx, int dy, char type) {
  for (int i=0;i<4;++i) {
    if (!(board[x][y] == type || board[x][y] == 'T')) {
      return 0;
    }
    x += dx;
    y += dy;
  }
  return type;
}

int main() {
  int T;
  cin>>T;
  for (int t=1;t<=T;++t) {
    for (int i=0;i<4;++i) cin >> board[i];

    char winner = 0;
    char types[] = {'X', 'O'};
    for (int j=0;j<2;++j) {
    for (int i=0;i<4;++i) {
      char type = types[j];
      winner |= win(i, 0, 0, 1, type);
      winner |= win(0, i, 1, 0, type);
      winner |= win(0, 0, 1, 1, type);
      winner |= win(3, 0, -1, 1, type);
    }
    }
    
    bool draw=  true;
    for (int i=0;i<4;++i) for (int j=0;j<4;++j) if (board[i][j] == '.') draw = false;

    cout << "Case #" << t << ": ";
    if (winner == 'X' || winner == 'O') cout << winner << " won" << endl;
    else if (draw) cout << "Draw" << endl;
    else cout << "Game has not completed" << endl;
  }
}
