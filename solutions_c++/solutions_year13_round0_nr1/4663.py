#include<iostream>


using namespace std;

int main() {
  int cas;

  cin>>cas;
  int board[4][4];
  for(int ca=1; ca<=cas; ++ca) {
    string s;
    bool draw = true;
    for(int i=0 ;i<4; ++i) {
      cin>>s;
      for(int j=0; j<4; ++j) {
        if(s[j] == 'O') {
          board[i][j] = 2;
        } else if (s[j] =='X'){
          board[i][j] = 1;
        } else if (s[j] =='T') {
          board[i][j] = 3;
        } else {
          board[i][j] = 0;
          draw = false;
        }
      }
    }

    bool found = false;
    string winner;
    for(int cand = 1; !found && cand<3; ++cand) {
      bool l = true, r = true;
      for(int i=0 ;i<4; ++i) {
        if (board[i][i] != cand && board[i][i] != 3) {
          l = false;
        }
        if (board[i][3-i] != cand && board[i][3-i] != 3) {
          r = false;
        }
      }
      if (l||r) {
        found = true;
      }

      for(int i=0 ; !found && i<4; ++i) {
        bool vgood = true;
        bool hgood = true;
        for(int j=0; (vgood || hgood) && j<4; ++j) {
          if (board[i][j] != cand && board[i][j] != 3) {
            vgood = false;
          }
          if (board[j][i] != cand && board[j][i] != 3) {
            hgood = false;
          }
        }
        if (vgood || hgood) {
          found =true;
        }
      }
      if (found) {
        winner = cand == 2 ? "O" : "X";
      }
    }
    cout<<"Case #"<<ca<<": ";
    if (found) {
      cout<<winner<<" won"<<endl;
    } else if (draw) {
      cout<<"Draw"<<endl;
    } else {
      cout<<"Game has not completed"<<endl;
    }
  }
}
