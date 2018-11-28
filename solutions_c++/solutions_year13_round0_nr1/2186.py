#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

enum TYPES {
  EMPTY = 0,
  T     = 1,
  X     = 2,
  O     = 3
};

bool checkWin(const TYPES field[4][4], TYPES type) {
  // check rows
  for (unsigned int r = 0;r<4;r++) {
    bool won = true;
    for (unsigned int c = 0;c<4;c++) {
      if (field[r][c] != type && field[r][c] != T) {
        won = false;
        break;
      }
    }
    if (won)
      return true;
  }

  // check columns
  for (unsigned int c = 0;c<4;c++) {
    bool won = true;
    for (unsigned int r = 0;r<4;r++) {
      if (field[r][c] != type && field[r][c] != T) {
        won = false;
        break;
      }
    }
    if (won)
      return true;
  }

  // check diagonals
  bool topLeft = true, topRight = true;
  for (unsigned int d = 0;d<4;d++) {
    if (field[d][d] != type && field[d][d] != T)
      topLeft = false;
    if (field[d][3-d] != type && field[d][3-d] != T)
      topRight = false;
  }

  return topLeft || topRight;
}


int main (int argc, const char **argv) {
  unsigned int noCases;

  if (argc != 2) {
    std::cout << "syntax: exe file" << std::endl;
    return 1;
  }

  std::ifstream input;
  input.open(argv[1]);
  if (!input.is_open()) {
    std::cout << "file not found" << std::endl;
    return 1;
  }

  std::string line;
  getline(input, line);
  std::stringstream ss(line);

  ss >> noCases;

  if (noCases > 1000) {
    std::cout << "T exceeds 1000" << std::endl;
  }

  std::ofstream output;
  output.open("result.txt");

  for (unsigned int i = 1;i<=noCases;i++) {
    TYPES field[4][4];
    bool completed = true;
    output << "Case #" << i << ": ";
    std::cout << "Case #" << i << ": ";

    for (unsigned int l = 0;l<4;l++) {
      getline(input, line);
      ss = std::stringstream(line);
      for (unsigned int c = 0;c<4;c++) {
        char square;
        ss >> square;
        switch (square) {
        case '.':
          field[l][c] = EMPTY;
          completed = false;
          break;
        case 'X':
          field[l][c] = X;
          break;
        case 'O':
          field[l][c] = O;
          break;
        case 'T':
          field[l][c] = T;
          break;
        default:
          std::cout << "parsing incorrect" << std::endl;
        }
      }
    }

    bool XWon = checkWin(field, X);
    bool OWon = checkWin(field, O);

    if (XWon && OWon) {
      output  << "Draw" << std::endl;
      std::cout  << "Draw" << std::endl;
    }
    else if (XWon) {
      output  << "X won" << std::endl;
      std::cout  << "X won" << std::endl;
    }
    else if (OWon) {
      output  << "O won" << std::endl;
      std::cout  << "O won" << std::endl;
    }
    else if (completed) {
      output  << "Draw" << std::endl;
      std::cout  << "Draw" << std::endl;
    }
    else {
      output  << "Game has not completed" << std::endl;
      std::cout  << "Game has not completed" << std::endl;
    }

    // skip the empty line
    getline(input, line);
  }

  input.close();
  output.close();

  return 0;
}