#include <iostream>
#include <string>
#include <cstring>
#include <cassert>

using namespace std;


struct cmatch {
  char ch;

  cmatch(char ch) : ch(ch) {}

  bool operator()(char c){
    return (c == ch || c == 'T');
  }
};

void run(int icase){

  char board[4][4];
  string s;
  for(int i = 0; i < 4; ++i){
    cin >> s;
    const char *cstr = s.c_str();
    memcpy(board[i], cstr, 4);
  }

  char buf[10];
  cin.getline(buf, '\n');

  for(int r = 0; r < 4; ++r){
    const char* cstr = board[r];
    char c0 = cstr[0];
    cmatch cm(c0);
    if(cm(cstr[1]) && cm(cstr[2]) && cm(cstr[3])){
      if(c0 == 'X'){
        cout << "Case #" << icase << ": X won\n";
        return;
      }
      else if(c0 == 'O'){
        cout << "Case #" << icase << ": O won\n";
        return;
      }
    }
  }

  for(int c = 0; c < 4; ++c){
    char c0 = board[0][c];
    cmatch cm(c0);
    if(cm(board[1][c]) && cm(board[2][c]) && cm(board[3][c])){
      if(c0 == 'X'){
        cout << "Case #" << icase << ": X won\n";
        return;
      }
      else if(c0 == 'O'){
        cout << "Case #" << icase << ": O won\n";
        return;
      }
    }
  }


  char c00 = board[0][0];
  cmatch cm00(c00);
  if(cm00(board[1][1]) && cm00(board[2][2]) && cm00(board[3][3])){
    if(c00 == 'X'){
      cout << "Case #" << icase << ": X won\n";
      return;
    }
    else if(c00 == 'O'){
      cout << "Case #" << icase << ": O won\n";
      return;
    }
  }

  char c03 = board[0][3];
  cmatch cm03(c03);
  if(cm03(board[1][2]) && cm03(board[2][1]) && cm03(board[3][0])){
    if(c03 == 'X'){
      cout << "Case #" << icase << ": X won\n";
      return;
    }
    else if(c03 == 'O'){
      cout << "Case #" << icase << ": O won\n";
      return;
    }
  }

  for(int r = 0; r < 4; ++r){
    const char *cstr = board[r];
    for(int j = 0; j < 4; ++j)
      if(cstr[j] == '.'){
        cout << "Case #" << icase << ": Game has not completed\n";
        return;
      }
  }
    
  cout << "Case #" << icase << ": Draw\n";
}

int main(){
  int ncases;
  cin >> ncases;
  for(int icase = 0; icase < ncases; ++icase)
    run(icase + 1);

  return 0;
}