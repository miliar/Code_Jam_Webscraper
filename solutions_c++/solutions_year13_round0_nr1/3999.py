#include<iostream>
#include<fstream>
#include <algorithm>
using namespace std;
ifstream fin("in");
ofstream fout("out");
char board[4][4];
bool check(char ch){
  int count=0;
  for (int i=0; i<4; i++){
    for (int j=0; j<4; j++){
      if (board[i][j]==ch || board[i][j]=='T') count++;
    }
    if (count==4) {return true;}
    else count=0;
  }
  for (int i=0; i<4; i++){
    for (int j=0; j<4; j++){
      if (board[j][i]==ch || board[j][i]=='T') count++;
    }
    if (count==4) {return true;}
    else count=0;
  }
  for (int i=0; i<4; i++){
    if (board[i][i]==ch || board[i][i]=='T') count ++;
  }
  if (count==4) return true;
  count=0;
  for (int i=0; i<4; i++){
    if (board[i][3-i]==ch || board[i][3-i]=='T') count ++;
  }
  if (count ==4) return true;
  else return false;
}

int main(){
  int cases;
  fin >> cases;
  for (int i=1; i<=cases; i++){
    int countDot=0;
    for (int j=0; j<4; j++){
      for (int k=0; k<4; k++){
	fin >> board[j][k];
	if (board[j][k]=='.') countDot++;
      }
    }
    fout << "Case #" << i<<": ";
    if (check('X')){
      fout << "X won"<< endl;
    }
    else if (check('O')){
      fout << "O won"<< endl;
    }
    else if (countDot>0) {
      fout << "Game has not completed"<< endl;
    }
    else {
      fout << "Draw"<< endl;
    }
  }
  return 0;
}
    
