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
#define PROBLEM_ID "A"

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int rows;
    cin >> rows;
    vector<string> field(rows);
    for (int i = 0; i < rows; ++i) {
      cin >> field[i];
    }
    vector<int> rightmost(rows);
    int cols = rows;
    for (int row = 0; row < rows; ++row) {
      for (int col = 0; col < cols; ++col) {
        if (field[row][col] == '1') {
          rightmost[row] = col;
        }
      }
    }
    int result = 0;
    bool found_error;
    vector<int> position(rows);
    vector<bool> position_used(rows, false);
    for (int row = 0; row < rows; ++row) {
      int init_pos = rightmost[row];
      while (position_used[init_pos]) {
        ++init_pos;
      }
      position[row] = init_pos;
      position_used[init_pos] = true;
    }
    do {
      found_error = true;
      int max_pos = -1;
      int index_max = -1;
      for (int row = 0; row < rows; ++row) {
        if (position[row] > row && position[row] > max_pos) {
          max_pos = position[row];
          index_max = row;
        }
      }
      if (max_pos == -1) {
        break;
      }
      while (position[index_max] > index_max) {
        swap(position[index_max], position[index_max + 1]);
        ++index_max;
        ++result;
      }
    } while (found_error);
    cout << "Case #" << test_index + 1 << ": " << result << endl;
  }
  return 0;
}
