#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int check(int ans){
  if ((ans == 8) || (ans == 16))
    return 1;
  else if ((ans == 27) || (ans == 81))
    return 2;
  else if (ans == 0)
    return 0; 
  else 
    return -1;
}

int main(){
  ifstream in("C:/CodeJam/1/A-large.in");
  ofstream out("C:/CodeJam/1/res_large.txt");
  //cin.rdbuf(in.rdbuf());
  //cout.rdbuf(out.rdbuf());
  map<char, unsigned int> _map;
  _map['X'] = 2; _map['O'] = 3; 
  _map['T'] = 1; _map['.'] = 0;
  unsigned int T;
  in >> T;
  for (unsigned int t = 0; t < T; ++t){
    unsigned int lastRow[4] = {1,1,1,1};
    unsigned int board[4][4];
    bool emptyCheck = false;
    int overAnswer = 0;
    for (unsigned int row = 0; row < 4; ++row){
      string rowStr;
      in >> rowStr;
      int rowSum = 1;
      for (unsigned int column = 0; column < 4; ++column){
        lastRow[column] *= _map[rowStr.at(column)];
        board[row][column] = _map[rowStr.at(column)];
        rowSum *= board[row][column];
      }
      int ans = check(rowSum);
      if ((ans == 1) || (ans == 2))
        overAnswer = ans;
      emptyCheck = emptyCheck || (ans == 0);
    }
    if (!overAnswer){
      for (unsigned int col = 0; col < 4; ++col){
        int ans = check(lastRow[col]);
        if ((ans == 1) || (ans == 2)){
          overAnswer = ans;
          break;
        }
      }    
      if (!overAnswer){
        int ans1 = check(board[0][0] * board[1][1] * board[2][2] * board[3][3]);
        int ans2 = check(board[0][3] * board[1][2] * board[2][1] * board[3][0]);
        if ((ans1 == 1) || (ans1 == 2))
          overAnswer = ans1;
        if ((ans2 == 1) || (ans2 == 2))
          overAnswer = ans2;
      }
    }
    out << "Case #" << t + 1 << ": ";
    if (overAnswer)
      if (overAnswer == 1)
        out << "X won" << endl;
      else
        out << "O won" << endl;
    else 
      if (emptyCheck)
        out << "Game has not completed" << endl;
      else
        out << "Draw" << endl;
    string rowStr;
    getline(in, rowStr);
  }
  in.close();
  out.close();
}