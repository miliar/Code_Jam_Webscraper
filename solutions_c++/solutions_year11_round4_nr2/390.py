#include <inttypes.h>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>

typedef long long ll;

using namespace std;

namespace {

void PrintOutput(size_t iter, const size_t result) {
  if (result != 1)
    printf("Case #%d: %d\n", iter+1, result);
  else
    printf("Case #%d: IMPOSSIBLE\n", iter+1);
}
} //namespace

int main() {
  size_t T;
  cin >> T;

  for (size_t iter = 0; iter < T; ++iter) {
    int R, C, D;
    cin >> R >> C >> D;

    vector<vector<int> > rec(R, vector<int>(C, 0));
    for (int r = 0; r < R; ++r) {
      for (int c = 0; c < C; ++c) {
        char tmp;
        cin >> tmp;
        int num = tmp - '0';
        rec[r][c] = num;
      }
    }

    int max_k = min(C, R);

    bool check = true;
    for (; max_k != 2 && check; --max_k) {
      for (int r = 0; r < R - max_k + 1 && check; ++r) {
        for (int c = 0; c < C - max_k + 1 && check; ++c) {
          int row_direct = 0;
          int col_direct = 0;
          for (int row = 0; row < max_k; ++row) {
            for (int col = 0; col < max_k; ++col) {
              if ((col == 0 && row == 0) ||
                  (col == (max_k - 1) && row == 0) ||
                  (col == 0 && row == (max_k - 1)) ||
                  (col == (max_k - 1) && row == (max_k - 1)))
                continue;

              row_direct += (D + rec[r + row][c + col]) * (2 * row - max_k + 1);
              col_direct += (D + rec[r + row][c + col]) * (2 * col - max_k + 1);
            }
          }

          if (row_direct == 0 && col_direct == 0) {
            PrintOutput(iter, max_k);
            check = false;
          }
        }
      }
    }

    if (check)
      PrintOutput(iter, 1);
  }
  return 0; 
}
