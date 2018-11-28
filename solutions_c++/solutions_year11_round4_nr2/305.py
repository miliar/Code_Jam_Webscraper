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
#define PROBLEM_ID "B"

typedef long long ll;
typedef vector<ll> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

ll get_sum(const vvi& weights, int bottom, int top, int left, int right) {
  return weights[top + 1][right + 1] - weights[bottom][right + 1] - weights[top + 1][left] + weights[bottom][left];
}

ll get_blade_sum(const vvi& weights, int bottom, int left, int size) {
  return get_sum(weights, bottom, bottom + size - 1, left, left + size - 1) - 
         get_sum(weights, bottom, bottom, left, left) - 
         get_sum(weights, bottom + size - 1, bottom + size - 1, left, left) -
         get_sum(weights, bottom, bottom, left + size - 1, left + size - 1) -
         get_sum(weights, bottom + size - 1, bottom + size - 1, left + size - 1, left + size - 1);
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int rows, columns, D;
    cin >> rows >> columns >> D;
    vector<string> field(rows);
    for (int i = 0; i < rows; ++i) {
      cin >> field[i];
    }
    vvi hor_weights(rows + 1, vi(columns + 1, 0));
    vvi vert_weights(rows + 1, vi(columns + 1, 0));
    vvi weights(rows + 1, vi(columns + 1, 0));
    for (int row = 0; row < rows; ++row) {
      ll hor_sum = 0;
      ll vert_sum = 0; 
      ll weight_sum = 0;
      for (int column = 0; column < columns; ++column) {
        ll weight = (D + (field[row][column] - '0'));
        hor_sum += weight * column;
        vert_sum += weight * row;
        weight_sum += weight;
        hor_weights[row + 1][column + 1] = hor_weights[row][column + 1] + hor_sum;
        vert_weights[row + 1][column + 1] = vert_weights[row][column + 1] + vert_sum;
        weights[row + 1][column + 1] = weights[row][column + 1] + weight_sum;
      }
    }
    int size;
    bool found = false;
    for (size = min(rows, columns); size >= 3; --size) {
      for (int bottom = 0; bottom + size <= rows; ++bottom) {
        for (int left = 0; left + size <= columns; ++left) {
          ll x_sum = get_blade_sum(hor_weights, bottom, left, size);
          ll y_sum = get_blade_sum(vert_weights, bottom, left, size);
          ll weight_sum = get_blade_sum(weights, bottom, left, size);
          ll right = (left + size - 1);
          ll top = (bottom + size - 1);
          if ((left + right) * weight_sum == x_sum * 2 && (top + bottom) * weight_sum == y_sum * 2) {
            found = true;
            break;
          }
        }
        if (found) {
          break;
        }
      }
      if (found) {
        break;
      }
    }
    cout << "Case #" << test_index + 1 << ": ";
    cerr << "Case #" << test_index + 1 << ": ";
    if (!found) {
      cout << "IMPOSSIBLE" << endl;
      cerr << "IMPOSSIBLE" << endl;
    } else {
      cout << size << endl;
      cerr << size << endl;
    }
  }
  return 0;
}
