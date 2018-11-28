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



int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int rects_count;
    cin >> rects_count;
    vector< pair<pii, pii> > rects(rects_count);
    int field_size = 0;
    for (int i = 0; i < rects_count; ++i) {
      scanf("%d%d%d%d", &rects[i].first.first, &rects[i].first.second, &rects[i].second.first, &rects[i].second.second);
      field_size = max(field_size, max(rects[i].first.first, max(rects[i].first.second, max(rects[i].second.first, rects[i].second.second))));
    }
    field_size += 2;
    vector<vb> field(field_size, vb(field_size, false));
    for (int i = 0; i < rects_count; ++i) {
      for (int row = rects[i].first.first; row <= rects[i].second.first; ++row) {
        for (int column = rects[i].first.second; column <= rects[i].second.second; ++column) {
          field[row][column] = true;
        }
      }
    }
    int result;
    for (result = 0;; ++result) {
      vector<vb> new_field = field;
      bool has_alive = false;
      for (int row = 0; row < field.size(); ++row) {
        for (int column = 0; column < field.size(); ++column) {
          if (field[row][column]) {
            has_alive = true;
            if (row > 0 && column > 0 && !field[row - 1][column] && !field[row][column - 1]) {
              new_field[row][column] = false;
            }
            if (row > 0 && column + 1 < field.size() && field[row - 1][column + 1]) {
              new_field[row][column + 1] = true;
            }
            if (row + 1 < field.size() && column > 0 && field[row + 1][column - 1]) {
              new_field[row + 1][column] = true;
            }
          }
        }
      }
      if (!has_alive) {
        break;
      }
      field = new_field;
    }
    cerr << "Case #" << test_index + 1 << ": " << result << endl;
    cout << "Case #" << test_index + 1 << ": " << result << endl;
  }
  return 0;
}
