#include<cstdio>
#include<cassert>

#include<vector>
#include<algorithm>
#include<iostream>
#include<string>

using namespace std;

class TicTacTomek{
public:
  TicTacTomek(){};

  TicTacTomek(vector<string> table1){
    table = table1;
  }

  string GetWinner(){
    int isfinished = 1;
    for(int i = 0; i < table.size(); ++i)
      for(int j = 0; j < table[i].size(); ++j)
        if(table[i][j] == '.')
          isfinished = 0;

    for(int i = 0; i < table.size(); ++i){
      int x = 0, y = 0;
      for(int j = 0; j < table[i].size(); ++j)
        if(table[i][j] == 'X')
          ++x;
        else if(table[i][j] == 'O')
          ++y;
        else  if(table[i][j] == 'T')
          ++x, ++y;

      if(x == 4)
        return "X won";
      if(y == 4)
        return "O won";
    }

    for(int j = 0; j < table.size(); ++j){
      int x = 0, y = 0;
      for(int i = 0; i < table[j].size(); ++i)
        if(table[i][j] == 'X')
          ++x;
        else if(table[i][j] == 'O')
          ++y;
        else  if(table[i][j] == 'T')
          ++x, ++y;

      if(x == 4)
        return "X won";
      if(y == 4)
        return "O won";
    }

    int x = 0, y = 0;

    for(int i = 0; i < table.size(); ++i){
      if(table[i][i] == 'X')
        ++x;
      else if(table[i][i] == 'O')
        ++y;
      else  if(table[i][i] == 'T')
        ++x, ++y;

      if(x == 4)
        return "X won";
      if(y == 4)
        return "O won";
    }

    x = 0, y = 0;
    for(int i = 0; i < table.size(); ++i){
      if(table[i][3 - i] == 'X')
        ++x;
      else if(table[i][3 - i] == 'O')
        ++y;
      else  if(table[i][3 - i] == 'T')
        ++x, ++y;

      if(x == 4)
        return "X won";
      if(y == 4)
        return "O won";
    }

    if(isfinished)
      return "Draw";

    return "Game has not completed";
  }

private:
  vector<string> table;
};

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int tests;
  cin >> tests;

  for(int i = 1; i <= tests; ++i){
    vector<string> given;

    for(int j = 0; j < 4; ++j){
      string aux;
      cin >> aux;
      given.push_back(aux);
    }

    TicTacTomek t(given);

    cout << "Case #" << i << ": " << t.GetWinner() << "\n";
  }

  return 0;
}
