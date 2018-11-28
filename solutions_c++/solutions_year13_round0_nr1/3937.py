#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <array>

typedef std::array<std::array<char, 4>, 4> matrix_t;

matrix_t read_m(std::istream & stream) {
  matrix_t m;
  for(size_t i = 0; i < 4; ++i) {
    for(size_t j = 0; j < 4; ++j) {
      stream >> m[i][j];
    }
  }
  return m;
}

template<class P>
bool check_column(matrix_t const& m, size_t i, P p)
{
  for(size_t j = 0; j < 4; ++j) {
    if (!p(m[j][i])) {
      return false;
    }
  }
  return true;
}

bool check(matrix_t const& m, char ch)
{
  bool main_diag = true;
  bool aux_diag = true;

  auto p = [ch](char c) { return c == ch || c == 'T'; };
  for(size_t i = 0; i < 4; ++i) {
    // check rows
    
    if (std::all_of(m[i].begin(), m[i].end(), p)) {
      return true;
    }

    // check columns
    if (check_column(m, i, p)) {
      return true;
    }

    // check diags
    if (!(m[i][i] == ch || m[i][i] == 'T')) {
      main_diag = false;
    }
    if (!(m[3-i][i] == ch || m[3-i][i] == 'T')) {
      aux_diag = false;
    }
  }
  return main_diag || aux_diag;
}

bool check_not_end(matrix_t const& m)
{
  for(size_t i = 0; i < 4; ++i) {
    for(size_t j = 0; j < 4; ++j) {
      if (m[i][j] == '.') {
        return true;
      }
    }
  }
  return false;
}

int main(int argc, char *argv[]) {
  char const*file = argv[1];
  std::ifstream fin(file);
  size_t count;
  fin >> count;
  for(size_t i = 1; i <= count; ++i) {
    matrix_t m = read_m(fin);
    bool cond;
    std::cout << "Case #" << i << ": ";
    if (cond = check(m, 'X')) {
      std::cout << "X won";
    } else if (cond = check(m, 'O')) {
      std::cout << "O won";
    } else if (cond = check_not_end(m)) {
      std::cout << "Game has not completed";
    } else {
      std::cout << "Draw";
    }
    std::cout << std::endl;
  }
}
