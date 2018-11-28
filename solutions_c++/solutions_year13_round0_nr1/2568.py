#include <iostream>
#include <string>
using namespace std;

enum state { xwon, owon, tie, incomplete };

char board[4][4];

void printboard(){
  for (int i = 0; i < 4; ++i){
    for (int j = 0; j < 4; ++j)
      cout << board[i][j];
    cout << endl;
  }
}

inline bool checkplayer(char c, char& player, bool& isspace){
  switch (c){
    case '.': isspace = true; return false; 
    case 'T': return true;
    case 'X': if (player == 'O') return false; break;
    case 'O': if (player == 'X') return false; break;
  }
  player = c;
  return true;
}

inline void reset(char& player, bool& state){
  player = 'T';
  state = true;
}

inline state report_player(char player){
  switch(player){
    case 'X': return xwon;
    case 'O': return owon;
  }
}

state eval(){
  bool seen_space = false;
  bool winning_row = true;
  char player = 'T';
  //horizontal and vertical
  for (int i = 0; i < 4; ++i){
    for (int j = 0; j < 4; ++j)
      if ((winning_row = checkplayer(board[i][j], player, seen_space)) == false)
        break;
    if (winning_row) return report_player(player);
    reset(player, winning_row);
    for (int j = 0; j < 4; ++j)
      if ((winning_row = checkplayer(board[j][i], player, seen_space)) == false)
        break;
    if (winning_row) return report_player(player);
    reset(player, winning_row);
  }
  //diagonal
  for (int i = 0; i < 4; ++i)
    if ((winning_row = checkplayer(board[i][i], player, seen_space)) == false)
      break;
  if (winning_row) return report_player(player);
  reset(player, winning_row);
  for (int i = 0; i < 4; ++i)
    if ((winning_row = checkplayer(board[i][4-i-1], player, seen_space)) == false)
      break;
  if (winning_row) return report_player(player);
  if (seen_space) return incomplete;
  return tie;
}

int main(){
  int n; cin>>n;
  string str; getline(cin, str);
  for (int i = 1; i <= n; ++i){
    for (int j = 0; j < 4; ++j){
      getline(cin, str);
      for (int k = 0; k < 4; ++k)
        board[j][k] = str[k];
    }

    cout << "Case #" << i << ": ";
    switch (eval()){
      case xwon: cout << "X won"; break;
      case owon: cout << "O won"; break;
      case tie:  cout << "Draw"; break;
      case incomplete: cout << "Game has not completed"; break;
    }
    cout << endl;

    getline(cin, str);
  }
}
