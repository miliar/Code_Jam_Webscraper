#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "C"

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

int StupidSolution(int rows, int cols, const vvi& dr, const vvi& dc) {
  int result = 0;
  for (int mask = 0; mask < (1 << (rows * cols)); ++mask) {
    vector<vector<pii> > next(rows, vector<pii>(cols));
    for (int row = 0; row < rows; ++row) {
      for (int col = 0; col < cols; ++col) {
        int index = row * cols + col;
        int nrow, ncol;
        if ((mask & (1 << index)) != 0) {
          nrow = (row + dr[row][col] + rows) % rows;
          ncol = (col + dc[row][col] + cols) % cols;
        } else {
          nrow = (row - dr[row][col] + rows) % rows;
          ncol = (col - dc[row][col] + cols) % cols;
        }
        next[row][col] = MP(nrow, ncol);
      }
    }
    vector<vb> done(rows, vb(cols, false));
    bool ok = true;
    for (int row = 0; row < rows; ++row) {
      for (int col = 0; col < cols; ++col) {
        if (!done[row][col]) {
          pii start = MP(row, col);
          pii cur = start;
          while (!done[cur.first][cur.second]) {
            done[cur.first][cur.second] = true;
            cur = next[cur.first][cur.second];
          }
          if (cur != start) {
            ok = false;
            break;
          }
        }
      }
      if (!ok) {
          break;
      }
    }
    if (ok) {
      ++result;
    }
  }
  return result;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int rows, columns;
    cin >> rows >> columns;
    vector<string> field(rows);
    for (int i = 0; i < rows; ++i) {
      cin >> field[i];
    }
    vvi dr(rows, vi(columns));
    vvi dc(rows, vi(columns));
    for (int row = 0; row < rows; ++row) {
      for (int col = 0; col < columns; ++col) {
        switch(field[row][col]) {
          case '|':
            dr[row][col] = 1;
            dc[row][col] = 0;
            break;
          case '-':
            dr[row][col] = 0;
            dc[row][col] = 1;
            break;
          case '/':
            dr[row][col] = 1;
            dc[row][col] = -1;
            break;
          case '\\':
            dr[row][col] = 1;
            dc[row][col] = 1;
            break;
        }
      }
    }
    int answer = StupidSolution(rows, columns, dr, dc);
    cout << "Case #" << test_index + 1 << ": " << answer << endl;
    cerr << "Case #" << test_index + 1 << ": " << answer << endl;
  }
  return 0;
}
