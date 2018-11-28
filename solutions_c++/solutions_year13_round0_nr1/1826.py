#include <iostream>
#include <string>
#include <vector>

using std::string;
using std::vector;

vector<string> GetTable() {
  vector<string> result(4);
  for (size_t line = 0; line < 4; ++line) {
    getline(std::cin, result[line]);
  }
  scanf("\n");
  return result;
}

bool ContainsEmptyCells(const vector<string>& table) {
  for (size_t row = 0; row < table.size(); ++row) {
    for (size_t column = 0; column < table[row].size(); ++column) {
      if (table[row][column] == '.') {
        return true;
      }
    }
  }
  return false;
}

int GetRowWinner(const vector<string>& table) {
  for (size_t row = 0; row < table.size(); ++row) {
    char first_char;
    bool first_taken = false;
    bool good_line = true;
    for (size_t column = 0; column < table[row].size() && good_line; ++column) {
      if (table[row][column] == '.') {
        good_line = false;
        continue;
      }

      if (!first_taken) {
        if (table[row][column] != 'T') {
          first_char = table[row][column];
          first_taken = true;
        }
        continue;
      }

      if (table[row][column] != 'T' && table[row][column] != first_char) {
        good_line = false;
      }
    }

    if (good_line) {
      return first_char == 'O';
    }
  }
  return -1;
}

int GetColumnWinner(const vector<string>& table) {
  for (size_t row = 0; row < table.size(); ++row) {
    char first_char;
    bool first_taken = false;
    bool good_line = true;
    for (size_t column = 0; column < table[row].size() && good_line; ++column) {
      if (table[column][row] == '.') {
        good_line = false;
        continue;
      }

      if (!first_taken) {
        if (table[column][row] != 'T') {
          first_char = table[column][row];
          first_taken = true;
        }
        continue;
      }

      if (table[column][row] != 'T' && table[column][row] != first_char) {
        good_line = false;
      }
    }

    if (good_line) {
      return first_char == 'O';
    }
  }
  return -1;
}

int GetDiagonalWinner(const vector<string>& table) {
  char first_char;
  bool first_taken = false;
  bool good_line = true;
  
  // check first diagonal
  for (size_t index = 0; index < table.size() && good_line; ++index) {
    if (table[index][index] == '.') {
      good_line = false;
      continue;
    }

    if (!first_taken) {
      if (table[index][index] != 'T') {
        first_char = table[index][index];
        first_taken = true;
      }
      continue;
    }

    if (table[index][index] != 'T' && table[index][index] != first_char) {
      good_line = false;
      continue;
    }
  }

  if (good_line) {
    return first_char == 'O';
  }

  first_char;
  first_taken = false;
  good_line = true;

  // check second diagonal
  for (size_t index = 0; index < table.size() && good_line; ++index) {
    if (table[index][3 - index] == '.') {
      good_line = false;
      continue;
    }

    if (!first_taken) {
      if (table[index][3 - index] != 'T') {
        first_char = table[index][3 - index];
        first_taken = true;
      }
      continue;
    }

    if (table[index][3 - index] != 'T' && table[index][3 - index] != first_char) {
      good_line = false;
      continue;
    }
  }

  if (good_line) {
    return first_char == 'O';
  }

  return -1;
}

string GetGameState(const vector<string>& table) {
  if (ContainsEmptyCells(table)) { // Draw is not possible
    int row_winner = GetRowWinner(table);
    if (row_winner != -1) {
      if (row_winner == 0) {
        return "X won";
      } else {
        return "O won";
      }
    }

    int column_winner = GetColumnWinner(table);
    if (column_winner != -1) {
      if (column_winner == 0) {
        return "X won";
      } else {
        return "O won";
      }
    }

    int diagonal_winner = GetDiagonalWinner(table);
    if (diagonal_winner != -1) {
      if (diagonal_winner == 0) {
        return "X won";
      } else {
        return "O won";
      }
    }

    return "Game has not completed";
  } else { // Draw is possible
    int row_winner = GetRowWinner(table);
    if (row_winner != -1) {
      if (row_winner == 0) {
        return "X won";
      } else {
        return "O won";
      }
    }

    int column_winner = GetColumnWinner(table);
    if (column_winner != -1) {
      if (column_winner == 0) {
        return "X won";
      } else {
        return "O won";
      }
    }

    int diagonal_winner = GetDiagonalWinner(table);
    if (diagonal_winner != -1) {
      if (diagonal_winner == 0) {
        return "X won";
      } else {
        return "O won";
      }
    }

    return "Draw";
  }
}

void Solve() {
  int T;
  scanf("%d\n", &T);
  for (int test_number = 1; test_number <= T; ++test_number) {
    vector<string> table = GetTable();
    string state = GetGameState(table);
    printf("Case #%d: %s\n", test_number, state.c_str());
  }
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  Solve();
  return 0;
}