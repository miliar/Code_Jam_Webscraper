#include <iostream>
#include <vector>
#include <set>

using namespace std;
namespace {
void PrintOutput(size_t iter, bool possible, const vector<vector<char> >& result) {
  cout << "Case #" << iter+1 << ":" << endl;
  if (possible) {
    for (size_t i = 0; i < result.size(); ++i) {
      for (size_t j = 0; j < result[i].size(); ++j) {
        cout << result[i][j];
      }
      cout << endl;
    }
  } else {
    cout << "Impossible" << endl;
  }
}
} //namespace

int main() {
  size_t T;
  cin >> T;

  for (size_t t = 0; t < T; ++t) {
    size_t R, C;
    cin >> R >> C;
    vector<vector<size_t> > tiles(R, vector<size_t>(C));

    for (size_t r = 0; r < R; ++r) {
      for (size_t c = 0; c < C; ++c) {
        char tmp;
        cin >> tmp;
        if (tmp == '.')
          tiles[r][c] = 1;
        else if (tmp == '#')
          tiles[r][c] = 2;
      }
    }

    bool possible = true;
    vector<vector<char> > result(R, vector<char>(C, '.'));

    for (size_t r = 0; possible && r < R; ++r) {
      for (size_t c = 0; possible && c < C; ++c) {
        if (tiles[r][c] == 2) {
          if (r == R-1 || c == C-1) {
            possible = false;
            continue;
          } else if (tiles[r+1][c] != 2 || tiles[r][c+1] != 2 || tiles[r+1][c+1] != 2) {
            possible = false;
            continue;
          }

          tiles[r][c] = 1; tiles[r+1][c] = 1; tiles[r][c+1] = 1; tiles[r+1][c+1] = 1;
          result[r][c] = '/'; result[r+1][c] = '\\'; result[r][c+1] = '\\'; result[r+1][c+1] = '/';
        }
      }
    }
    PrintOutput(t, possible, result);
  }

  return 0;
}
