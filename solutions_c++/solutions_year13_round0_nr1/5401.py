// Google Code Jam
// Qualification Round 2013
//
// Problem A. Tic-Tac-Toe-Tomek
//
// Compiled with C++11 and clang++
// clang++ -std=c++11 -stdlib=libc++ -Wall

#include <iostream>

using std::cin;
using std::cout;
using std::endl;

namespace codejam {

static const int kBoardSize = 4;

static const char kO = 'O';
static const char kX = 'X';
static const char kT = 'T';
static const char kSpace = '.';

class TicTacToeTomekAnaliser {
 public:
  TicTacToeTomekAnaliser();
  void nextToken(char token) noexcept;

  bool failed() const noexcept;
  bool hasSpace() const noexcept;
  char whoWon() const noexcept;
  bool won() const noexcept;

 private:
  enum State {
    INIT, FOUND1, FOUND2, FOUND3, WON, TOMEK, FAILED, FAILED_WITH_SPACE
  };

  TicTacToeTomekAnaliser(const TicTacToeTomekAnaliser&);
  TicTacToeTomekAnaliser& operator=(const TicTacToeTomekAnaliser&);

  char first_;
  int state_;
};

TicTacToeTomekAnaliser::TicTacToeTomekAnaliser()
    : first_('\0'),\
      state_(State::INIT) {}

void TicTacToeTomekAnaliser::nextToken(char token) noexcept {
  switch (state_) {
  case INIT:
    if (token == kO || token == kX) {
      first_ = token;
      state_ = FOUND1;
    } else if (token == kT) {
      state_ = TOMEK;
    } else {  // token == kSpace
      state_ = FAILED_WITH_SPACE;
    }
    break;
  case FOUND1:
  case FOUND2:
  case FOUND3:
    if (token == first_ || token == kT) {
      ++state_;
    } else if (token == kSpace) {
      state_ = FAILED_WITH_SPACE;
    } else {  // token == other player's token
      state_ = FAILED;
    }
    break;
  case WON:
    state_ = FAILED;
    break;
  case TOMEK:
    if (token == kO || token == kX) {
      first_ = token;
      state_ = FOUND2;
    } else {  // token == kSpace
      state_ = FAILED_WITH_SPACE;
    }
    break;
  case FAILED:
  case FAILED_WITH_SPACE:
    break;
  }
}

bool TicTacToeTomekAnaliser::failed() const noexcept {
  return state_ == FAILED || state_ == FAILED_WITH_SPACE;
}

bool TicTacToeTomekAnaliser::hasSpace() const noexcept {
  return state_ == FAILED_WITH_SPACE;
}

char TicTacToeTomekAnaliser::whoWon() const noexcept {
  return first_;
}

bool TicTacToeTomekAnaliser::won() const noexcept {
  return state_ == WON;
}

inline char charAt(char* board, int i, int j) {
  return board[i * kBoardSize + j];
}

char extractWinner(const TicTacToeTomekAnaliser& t1,
                   const TicTacToeTomekAnaliser& t2,
                   const TicTacToeTomekAnaliser& t3) {
  if (t1.won()) {
    return t1.whoWon();
  } else if (t2.won()) {
    return t2.whoWon();
  } else if (t3.won()) {
    return t3.whoWon();
  }
  return '0';
}

void evaluate(int testCase, char* board) {
  bool hasSpace = false;
  char whoWon = '\0';
  bool won = false;

  TicTacToeTomekAnaliser diagonal1;
  TicTacToeTomekAnaliser diagonal2;

  for (auto i = 0; !won && i < kBoardSize; ++i) {
    TicTacToeTomekAnaliser horizontal;
    TicTacToeTomekAnaliser vertical;

    for (int j = 0; j < kBoardSize; ++j) {
      horizontal.nextToken(charAt(board, i, j));
      vertical.nextToken(charAt(board, j, i));
      if (i == j) {
        diagonal1.nextToken(charAt(board, i, j));
      } else if (i + j == kBoardSize - 1) {
        diagonal2.nextToken(charAt(board, i, j));
      }

      if (i == kBoardSize - 1 && j == 0 && diagonal2.won()) {
        whoWon = diagonal2.whoWon();
        won = true;
      } else if (j == kBoardSize - 1) {
        whoWon = extractWinner(horizontal, vertical, diagonal1);
        if (whoWon != '0') {
          won = true;
        } else if (!hasSpace) {
          hasSpace = horizontal.hasSpace() ||
                     vertical.hasSpace() ||
                     diagonal1.hasSpace() ||
                     diagonal2.hasSpace();
        }
      }
    }
  }

  cout << "Case #" << testCase << ": ";
  if (won) {
    cout << whoWon << " won";
  } else if (hasSpace) {
    cout << "Game has not completed";
  } else {
    cout << "Draw";
  }
  cout << endl;
}

}  // namespace codejam

using codejam::kBoardSize;
using codejam::evaluate;

int main(int argc, char* argv[]) {
  int t;
  cin >> t;
  for (auto testCase = 1; testCase <= t; ++testCase) {
    char board[kBoardSize * kBoardSize];
    for (auto i = 0; i < kBoardSize; ++i) {
      for (int j = 0; j < kBoardSize; ++j) {
        cin >> board[i * kBoardSize + j];
      }
    }
    evaluate(testCase, board);
  }
  return 0;
}
