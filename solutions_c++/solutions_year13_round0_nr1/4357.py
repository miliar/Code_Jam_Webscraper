#include <iostream>

using namespace std;

char G[4][4];
string ans[4] = {"X won",
                 "O won",
                 "Draw",
                 "Game has not completed"};
  
string solve() {
  bool xWin = false;
  bool oWin = false;
  int cnt = 0;
  
  for(int i = 0; i < 4; i++) {
    for(int j = 0; j < 4; j++) {
      if(G[i][j] == '.') cnt++;
    }
  }

  int x, o;
  
  // yoko
  for(int i = 0; i < 4; i++) {
    x = o = 0;
    for(int j = 0; j < 4; j++) {
      if(G[i][j] == 'X' || G[i][j] == 'T') x++;
      if(G[i][j] == 'O' || G[i][j] == 'T') o++;
    }
    if(x == 4) xWin = true;
    if(o == 4) oWin = true;
  }
      
  // tate
  for(int j = 0; j < 4; j++) {
    x = o = 0;
    for(int i = 0; i < 4; i++) {
      if(G[i][j] == 'X' || G[i][j] == 'T') x++;
      if(G[i][j] == 'O' || G[i][j] == 'T') o++;
    }
    if(x == 4) xWin = true;
    if(o == 4) oWin = true;
  }
  
  // naname
  x = o = 0;
  for(int i = 0; i < 4; i++) {
    if(G[i][i] == 'X' || G[i][i] == 'T') x++;
    if(G[i][i] == 'O' || G[i][i] == 'T') o++;
    if(x == 4) xWin = true;
    if(o == 4) oWin = true;
  }
  x = o = 0;
  for(int i = 0; i < 4; i++) {
    if(G[i][3 - i] == 'X' || G[i][3 - i] == 'T') x++;
    if(G[i][3 - i] == 'O' || G[i][3 - i] == 'T') o++;
    if(x == 4) xWin = true;
    if(o == 4) oWin = true;
  }
  
  int idx = 0;
  if(xWin && oWin) idx = 2;
  else if(xWin) idx = 0;
  else if(oWin) idx = 1;
  else if(cnt == 0) idx = 2;
  else idx = 3;

  return ans[idx];
}

int main() {
  int T;
  cin >> T;
  
  for(int tc = 1; tc <= T; tc++) {
    for(int i = 0; i < 4; i++) {
      for(int j = 0; j < 4; j++) {
        cin >> G[i][j];
      }
    }
    cout << "Case #" << tc << ": " << solve() << endl;
  }
  
  return 0;
}
