#include <iostream>
#include <string>
#include <vector>

bool solve(std::vector<std::string> &tiles) {
  for (std::size_t r = 0; r < tiles.size(); ++r) {
    for (std::size_t c = 0; c < tiles[r].size(); ++c) {
      if (tiles[r][c] == '#') {
        if (r == (tiles.size() - 1)) {
          return false;
        } else if (c == (tiles[r].size() - 1)) {
          return false;
        } else if ((tiles[r][c + 1] != '#') ||
            (tiles[r + 1][c] != '#') ||
            (tiles[r + 1][c + 1] != '#')) {
          return false;
        }
        tiles[r][c] = '/';
        tiles[r + 1][c] = '\\';
        tiles[r][c + 1] = '\\';
        tiles[r + 1][c + 1] = '/';
      }
    }
  }
  return true;
}

void print(const std::vector<std::string> &tiles) {
  for (std::size_t r = 0; r < tiles.size(); ++r) {
    std::cout << tiles[r] << std::endl;
  }
}

int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    int R, C;
    std::cin >> R >> C;
    std::vector<std::string> tiles(R);
    for (int r = 0; r < R; ++r) {
      std::cin >> tiles[r];
    }
    if (solve(tiles)) {
      std::cout << "Case #" << t << ":\n";
      print(tiles);
    } else {
      std::cout << "Case #" << t << ":\nImpossible" << std::endl;
    }
  }
  return 0;
}
