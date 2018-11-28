#include <iostream>
#include <vector>
#include <string>

#define FOR(i,C) for(int i=0; i<C; i++)
#define FOR_REV(i,C) for(int i=C-1; i>=0; i--)

typedef long long ll_t;

using namespace std;

string ans(vector<int>& marks);

int main(int argc, char* argv[]){
  int T;

  cin >> T;

  // read input
  ll_t c = 0;
  char symbol;
  vector<int> marks(16);

  while( cin ){
    if( ++c > T ) return -1;

    FOR(i,16){
      cin >> symbol;
      if( symbol == 'X' ){
        marks[i] = 1;
      }
      else if( symbol == 'O' ){
        marks[i] = 2;
      }
      else if( symbol == 'T' ){
        marks[i] = 3;
      }
      else if( symbol == '.' ){
        marks[i] = 0;
      }
    }

    // output answer
    cout << "Case #" << c << ": " << ans(marks) << endl;
  }

  return 0;
}

string ans(vector<int>& marks){
  int winner = 0;
  FOR(i,4){
    // row
    winner = marks[4*i] & marks[4*i + 1] & marks[4*i + 2] & marks[4*i + 3];
    if( winner == 1 ){ return "X won"; }
    else if( winner == 2 ){ return "O won"; }

    // column
    winner = marks[i] & marks[i+4] & marks[i+8] & marks[i+12];
    if( winner == 1 ){ return "X won"; }
    else if( winner == 2 ){ return "O won"; }
  }

  // diagonal
  winner = marks[0] & marks[5] & marks[10] & marks[15];
  if( winner == 1 ){ return "X won"; }
  else if( winner == 2 ){ return "O won"; }

  winner = marks[3] & marks[6] & marks[9] & marks[12];
  if( winner == 1 ){ return "X won"; }
  else if( winner == 2 ){ return "O won"; }

  FOR(i,16){
    if( marks[i] == 0 ) return "Game has not completed";
  }

  return "Draw";
}
