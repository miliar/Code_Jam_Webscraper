#include <iostream>
#include <string>
#include <vector>

bool check_row(const std::vector<std::string> &lines, char player,
               int i, int j, int di, int dj) {
  for (int k = 0; k < 4; ++k) {
    char value = lines[i + k * di][j + k * dj];
    if (value != player && value != 'T') {
      return false;
    }
  }
  return true;
}

bool check_victory(const std::vector<std::string> &lines, char player) {
  return check_row(lines, player, 0, 0, 1, 0)
    || check_row(lines, player, 0, 1, 1, 0)
    || check_row(lines, player, 0, 2, 1, 0)
    || check_row(lines, player, 0, 3, 1, 0)
    || check_row(lines, player, 0, 0, 0, 1)
    || check_row(lines, player, 1, 0, 0, 1)
    || check_row(lines, player, 2, 0, 0, 1)
    || check_row(lines, player, 3, 0, 0, 1)
    || check_row(lines, player, 0, 0, 1, 1)
    || check_row(lines, player, 0, 3, 1, -1);
}

int main() {
  int T;
  std::cin >> T;
  for (int casenum = 1; casenum <= T; ++casenum) {
    std::vector<std::string> lines;
    for (int i = 0; i < 4; ++i) {
      std::string line;
      std::cin >> line;
      lines.push_back(line);
    }

    std::string result;
    if (check_victory(lines, 'X')) {
      result = "X won";
    } else if (check_victory(lines, 'O')) {
      result = "O won";
    } else {
      bool seen_empty = false;
      for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
          if (lines[i][j] == '.') {
            seen_empty = true;
          }
        }
      }

      if (seen_empty) {
        result = "Game has not completed";
      } else {
        result = "Draw";
      }
    }

    std::cout << "Case #" << casenum << ": " << result << std::endl;
  }
}
