#include <climits>
#include <ctime>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

typedef long unsigned int lui;

const char* inputFile  = "A-large.in";
const char* outputFile = "A-large.out";

void print_board(char board[][50], int N) {
  for (int i = 0; i < N; ++i) {
      for (int j = 0; j < N; ++j) {
        cout << board[i][j] << " ";
      }
      cout << endl;
    }
}

void rotate_board(char board[][50], int N) {
  for (int i = 0; i < N; ++i) {

    for (int j = N - 1; j >= 0; --j) {

      char b = board[i][j];
      if (b == '.') {

        int k = j - 1;
        while (k >= 0 && board[i][k] == '.')
          --k;

        if (k >= 0) {
          board[i][j] = board[i][k];
          board[i][k] = '.';
        }
        else
          break;
      }
    }
  }
}

bool check_dir(char board[][50], int N, int K, char b, int i, int j, int di, int dj) {

  if (i < 0 || i >= N || j < 0 || j >= N)
    return false;

  if (board[i][j] != b)
    return false;

  else if (K == 1)
    return true;

  return check_dir(board,N,K-1,b,i+di,j+dj,di,dj);
}

void check_winners(char board[][50], int N, int K, bool& r, bool& b) {
  r = false; b = false;

  for (int i = 0; i < N && !(r && b); ++i) {
    for (int j = 0; j < N && !(r && b); ++j) {
      if (!r) {
        r = check_dir(board,N,K,'R',i,j,+1,+0);
        if (!r) r = check_dir(board,N,K,'R',i,j,+1,+1);
        if (!r) r = check_dir(board,N,K,'R',i,j,+0,+1);
        if (!r) r = check_dir(board,N,K,'R',i,j,-1,+1);
        if (!r) r = check_dir(board,N,K,'R',i,j,-1,+0);
        if (!r) r = check_dir(board,N,K,'R',i,j,-1,-1);
        if (!r) r = check_dir(board,N,K,'R',i,j,+0,-1);
        if (!r) r = check_dir(board,N,K,'R',i,j,+1,-1);
      }
      if (!b) {
        b = check_dir(board,N,K,'B',i,j,+1,+0);
        if (!b) b = check_dir(board,N,K,'B',i,j,+1,+1);
        if (!b) b = check_dir(board,N,K,'B',i,j,+0,+1);
        if (!b) b = check_dir(board,N,K,'B',i,j,-1,+1);
        if (!b) b = check_dir(board,N,K,'B',i,j,-1,+0);
        if (!b) b = check_dir(board,N,K,'B',i,j,-1,-1);
        if (!b) b = check_dir(board,N,K,'B',i,j,+0,-1);
        if (!b) b = check_dir(board,N,K,'B',i,j,+1,-1);
      }
    }
  }
}

int main(int argc, char** argv) {

  ifstream iFile;
  iFile.open(inputFile);
  if (!iFile.is_open()) {
    cerr << "Failed to open input file!" << endl;
    return 0;
  }

  ofstream oFile;
  oFile.open(outputFile);
  if (!oFile.is_open()) {
    cerr << "Failed to open output file!" << endl;
    return 0;
  }

  clock_t t0 = clock();
  clock_t now;

  int T,N,K;

  char board[50][50];

  iFile >> T;
  for (int t = 1; t <= T; ++t) {

    iFile >> N >> K;

    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < N; ++j) {
        iFile >> board[i][j];
      }
    }

    rotate_board(board,N);

    bool r, b;
    check_winners(board,N,K,r,b);

    oFile << "Case #" << t << ": ";
    if (r && b)       oFile << "Both";
    else if (r && !b) oFile << "Red";
    else if (!r && b) oFile << "Blue";
    else              oFile << "Neither";
    oFile << endl;

    now = clock();
    printf("T %d/%d : %f\n",t,T,((double)(now - t0))/(double)CLOCKS_PER_SEC);
  }

  iFile.close();
  oFile.close();

  return 0;
}
