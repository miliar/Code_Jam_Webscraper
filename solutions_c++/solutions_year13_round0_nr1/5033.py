
#include<iostream>
#include<string>
#include<vector>

using namespace std;

vector<string> board;

bool finished(){
  for(int i = 0; i < 4; ++i){
    for(int j = 0; j < 4; ++j){
      if(board[i][j] == '.') return false;
    }
  }
  return true;
}


bool columns(char c){
  bool win;
  for(int i = 0; i < board.size(); ++i){
    win = true;
    for(int j = 0; j < board[i].size(); ++j){
      if((board[i][j] != c) && (board[i][j] != 'T')){
        win = false;
        break;
      }
    }
    if(win) break;
  }
  return win;
}

bool rows(char c){
  bool win;
  for(int j = 0; j < 4; ++j){
    win = true;
    for(int i = 0; i < 4; ++i){
      if((board[i][j] != c) && (board[i][j] != 'T')){
        win = false;
        break;
      }
    }
    if(win) break;
  }
  return win;
}

bool diag(char c){
  bool win1 = true;
  bool win2 = true;
  for(int i = 0; i < 4; ++i){
    if((board[i][i] != c) && (board[i][i] != 'T')){
      win1 = false;
    }
    if((board[i][3-i] != c) && (board[i][3-i] != 'T')){
      win2 = false;
    }
  }
  return (win1||win2);
}


bool win(char c){
  if(columns(c)) return true;
  if(rows(c)) return true;
  return diag(c);
}
 



int main(){
  int T;
  cin >> T;
  for(int t = 1; t <=T; ++t){
    board = vector<string>(4, "");
    for(int i = 0; i < 4; ++i){
      cin >> board[i];
    }
    cout << "Case #" << t << ": ";
    if(win('X')) cout << "X won" << endl;
    else if(win('O')) cout << "O won" << endl;
    else if(finished()) cout << "Draw" << endl;
    else cout << "Game has not completed" << endl;
  }

  return 0;
}




