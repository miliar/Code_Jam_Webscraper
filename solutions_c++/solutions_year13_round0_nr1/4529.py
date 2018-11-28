#include <iostream>
#include <string>

using namespace std;

int const SIZE = 4;

string const X_WON = "X won";
string const O_WON = "O won";
string const DRAW = "Draw";
string const PROGRESS = "Game has not completed";

char const EMPTY = '.';
char const X = 'X';
char const O = 'O';
char const T = 'T';

class TTTT {
  public:
    TTTT();
    void print(ostream&);
    bool solve();
    bool ended();
  private:
    bool is(int,int,char search);
    bool full_row(int,char);
    bool full_col(int,char);
    bool full_diag(char);
    char configuration[SIZE][SIZE];
};

TTTT::TTTT() {
  for(int i = 0; i < SIZE; ++i) {
    string line;
    cin >> line;
    for(int j = 0; j < SIZE; ++j) {
      configuration[i][j] = line[j]; 
    }
  }
}

bool TTTT::is(int x, int y,char search) {
  return (configuration[x][y] == search || configuration[x][y] == T);
}

bool TTTT::full_row(int row,char search) {
  return (is(row,0,search) && is(row,1,search) && is(row,2,search) && is(row,3,search) );
}

bool TTTT::full_col(int col, char search) {
  return (is(0,col,search) && is(1,col,search) && is(2,col,search) && is(3,col,search) );
}

bool TTTT::full_diag(char search) {
  return ( (is(0,0,search) && is(1,1,search) && is(2,2,search) && is(3,3,search) )
        || (is(3,0,search) && is(2,1,search) && is(1,2,search) && is(0,3,search) ) );
}

bool TTTT::ended() {
  for(int i = 0; i < SIZE; ++i) {
    for(int j = 0; j < SIZE; ++j) {
      if(configuration[i][j] == EMPTY) {
        return false;
      }
    }
  }
  return true;
}

bool TTTT::solve() {
  if( full_row(0,X) || full_row(1,X) || full_row(2,X) || full_row(3,X) 
   || full_col(0,X) || full_col(1,X) || full_col(2,X) || full_col(3,X) 
   || full_diag(X) ) {
    cout << "X won";
    return true;
  }
  if( full_row(0,O) || full_row(1,O) || full_row(2,O) || full_row(3,O) 
   || full_col(0,O) || full_col(1,O) || full_col(2,O) || full_col(3,O) 
   || full_diag(O) ) {
    cout << "O won";
    return true;
  }
  
  if(ended() == false) {
    cout << "Game has not completed";
    return true;
  }

  cout << "Draw";
  return true;
}

int main() {
  int T;
  cin >> T;
  for(int i = 1; i <= T; ++i) {
    TTTT tictactoetomek = TTTT();
    cout << "Case #" << i << ": ";
    tictactoetomek.solve();
    cout << endl;
  }
  
  return 0;
}
