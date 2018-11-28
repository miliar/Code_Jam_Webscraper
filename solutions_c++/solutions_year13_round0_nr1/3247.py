// Google CodeJam 2013 Qualifying Round A
// dom7b5

#include <iostream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;

const int size = 4;
const int nrows = size;
const int ncols = size;

/* Determine whether the subset of a sequence should be
   considered as matching for a win. */
bool match(char a, char b) 
{
  return ((a == 'X' || a == 'O' || a == 'T') &&
          (b == 'X' || b == 'O' || b == 'T') &&
          ((a == b) || (a == 'T' || b == 'T')));
}

/* Given that a or b are characters of a winning sequence,
   return the player involved in the sequence, X or O. */
char player(char a, char b)
{
  return a == 'T' ? b : a;
}

/* Determine whether the given sequence (row, column, or
   diagonal) is a win for a player, and returns the winner. */
char winner(string seq)
{
  char w = 0;
  for (int i = 1; i < ncols; ++i) {
    if (!match(seq[i-1], seq[i])) {
      return 0;
    }
    else {
      // be wary of the case where OTXX (pairs match, but seq fails)
      if (w) {
        if (w != player(seq[i-1], seq[i])) {
          return 0;
        }
      }
      else {
        w = player(seq[i-1], seq[i]);
      }
    }
  }
  return w;
}

/* Convert the given board to a set of sequences, for all
   the rows, columns, and diagonals. */
void sequences(vector<string> &board, vector<string> &seqs)
{
  string seq("....");
  int nseq = 0;

  // row sequences
  for (int r = 0; r < nrows; ++r) {
    for (int c = 0; c < ncols; ++c) {
      seq[c] = board[r][c];
    }
    seqs[nseq++] = seq;
  }

  // column sequences
  for (int c = 0; c < nrows; ++c) {
    for (int r = 0; r < ncols; ++r) {
      seq[r] = board[r][c];
    }
    seqs[nseq++] = seq;
  }
  
  // diagonal 1 sequence
  for (int r = 0; r < nrows; ++r) {
    seq[r] = board[r][r];
  }
  seqs[nseq++] = seq;

  // diagonal 2 sequence
  for (int r = 0; r < nrows; ++r) {
    seq[r] = board[r][size-1-r];
  }
  seqs[nseq++] = seq;
}

/* Determine the status of the given game board configuration. */
string status(vector<string> &board)
{
  stringstream s;
  vector<string> seqs(4 + 4 + 2); // rows, columns, diagonals
  char w = 0;

  // convert board to sequences of rows, columns, diagonals
  sequences(board, seqs);

  // check rows, columns, and diagonals
  for (unsigned int i = 0; i < seqs.size(); ++i) {
    w = winner(seqs[i]);
    if (w) {
      s << w << " won";
      return s.str();
    }
  }

  // no winners; determine completeness
  for (int r = 0; r < nrows; ++r) {
    for (int c = 0; c < ncols; ++c) {
      if (board[r][c] == '.') {
        return "Game has not completed";
      }
    }
  }
  
  // no winners and complete; must be draw
  return "Draw";
}

/* Read the cases and output the status for each. */
int main(int argc, char *argv[])
{
  int ncases = 0;
  vector<string> board(4);
  
  cin >> ncases;

  for (int cs = 0; cs < ncases; ++cs) {
    for (int r = 0; r < nrows; ++r) {
      cin >> board[r];
    }
    cout << "Case #" << (cs + 1) << ": "
         << status(board) << endl;
  }
  
}
