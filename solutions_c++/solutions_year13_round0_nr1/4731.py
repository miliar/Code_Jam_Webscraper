#include <fstream>
#include <iostream>

using namespace std;
ifstream in("in");
ofstream out("out");
int casei, ncase;
ostream &writeCase() {
  return out<<"Case #"<<++casei<<": ";
}

string Xwon="X won", Owon="O won", draw="Draw", incomplete="Game has not completed";

int const boardsz = 4*4;

char board[boardsz];

char wild='T';

int starts[] = {0, 1, 2, 3,
                0, 4, 8, 12,
                0, 3};
int strides[] = {4, 4, 4, 4,
                 1, 1, 1, 1,
                 5, 3};

int nstrides = 4+4+2;

/// board may have at most one T. so 'who' wins if any line is all 'who' or T.
bool wins(char who, int start, int stride) {
  for (int i = 0; i<4; ++i) {
    char b = board[start+stride*i];
    if (!(b=='T' || b==who)) return false;
  }
  return true;
}

string NoWinner() {
  for (int i = 0; ; ++i) {
    if (board[i]=='.')
      break;
    if (i==boardsz)
      return draw;
  }
  return incomplete;
}

string EvalBoard() {
  for (int i = 0; i<nstrides; ++i) {
    if (wins('X', starts[i], strides[i]))
      return Xwon;
    if (wins('O', starts[i], strides[i]))
      return Owon;
  }
  return NoWinner();
}


int main() {
  in>>ncase;
  for (int i = 0; i<ncase; ++i) {
    for (int j = 0; j<boardsz; ++j)
      in>>board[j];
    writeCase() << EvalBoard() << '\n';
  }
}
