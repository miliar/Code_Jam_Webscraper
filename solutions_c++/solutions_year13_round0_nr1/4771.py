#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

int main(){
  int T;
  cin >> T;
  for(int z=1; z<=T; ++z){
    vector<string> in(4),ni(4,string('.', 4));
    for(int i=0; i<4; ++i){
      cin >> in[i];
    }
    for(int i=0; i<4; ++i){
      for(int j=0; j<4; ++j){
        ni[i][j] = in[j][i];
      }
    }

    bool o_win = false;
    bool x_win = false;
    bool empty = false;

    {
      int o = 0;
      int x = 0;
      int t = 0;
      for(int i=0; i<4; ++i){
        for(int j=0; j<4; ++j){
          o += in[i][j] == 'O';
          x += in[i][j] == 'X';
          t += in[i][j] == 'T';
        }
      }
      if(o+x+t < 16){
        empty = true;
      }
    }

    for(int i=0; i<4; ++i){
      int o = count(in[i].begin(), in[i].end(), 'O');
      int x = count(in[i].begin(), in[i].end(), 'X');
      int t = count(in[i].begin(), in[i].end(), 'T');
      if(o+t == 4){
        o_win = true;
      }
      if(x+t == 4){
        x_win = true;
      }
    }

    in = ni;
    for(int i=0; i<4; ++i){
      int o = count(in[i].begin(), in[i].end(), 'O');
      int x = count(in[i].begin(), in[i].end(), 'X');
      int t = count(in[i].begin(), in[i].end(), 'T');
      if(o+t == 4){
        o_win = true;
      }
      if(x+t == 4){
        x_win = true;
      }
    }

    {
      int o = 0;
      int x = 0;
      int t = 0;
      for(int i=0; i<4; ++i){
        o += in[i][i] == 'O';
        x += in[i][i] == 'X';
        t += in[i][i] == 'T';
      }
      if(o+t == 4){
        o_win = true;
      }
      if(x+t == 4){
        x_win = true;
      }
    }

    {
      int o = 0;
      int x = 0;
      int t = 0;
      for(int i=0; i<4; ++i){
        o += in[i][3-i] == 'O';
        x += in[i][3-i] == 'X';
        t += in[i][3-i] == 'T';
      }
      if(o+t == 4){
        o_win = true;
      }
      if(x+t == 4){
        x_win = true;
      }
    }


    cout << "Case #" << z << ": ";
    if(o_win){
      cout << "O won" << endl;
    }else if(x_win){
      cout << "X won" << endl;
    }else if(empty){
      cout << "Game has not completed" << endl;
    }else{
      cout << "Draw" << endl;
    }
  }
}