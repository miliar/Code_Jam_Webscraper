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
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

int best_result;
vector<string> field;

struct state {
  string cur;
  string next;
  int row;
  int col;
  int digs;
  state(string cur_, string next_, int row_, int col_, int digs_): cur(cur_), next(next_), row(row_), col(col_), digs(digs_) {}
};

bool operator<(const state& a, const state& b) {
  if (a.row != b.row) {
    return a.row < b.row;
  }
  if (a.col != b.col) {
    return a.col < b.col;
  }
  if (a.digs != b.digs) {
    return a.digs < b.digs;
  }
  if (a.cur != b.cur) {
    return a.cur < b.cur;
  }
  return a.next < b.next;
}

set<state> was;
int F;

void go(string cur, string next, int row, int col, int digs) {
  if (row == field.size() - 1) {
    best_result = min(best_result, digs);
    return;
  }
  state cur_state(cur, next, row, col, digs);
  if (was.find(cur_state) != was.end()) {
    return;
  }
  was.insert(cur_state);
  if (col > 0 && cur[col - 1] == '.') {
    if (next[col - 1] == '#') {
      go(cur, next, row, col - 1, digs);
      next[col - 1] = '.';
      go(cur, next, row, col, digs + 1);
      next[col - 1] = '#';
    } else {
      int fall = 1;
      int currow = row;
      while (currow + 2 < field.size() && field[currow + 2][col - 1] == '.') {
        ++fall;
        ++currow;
      }
      if (fall <= F) {
        string newcur = fall == 1 ? next : field[currow + 1];
        string newnext;
        if (currow + 2 < field.size()) {
          newnext = field[currow + 2];
        }
        go(newcur, newnext, currow + 1, col - 1, digs);
      }
    }
  }
  if (col + 1 < field[row].size() && cur[col + 1] == '.') {
    if (next[col + 1] == '#') {
      go(cur, next, row, col + 1, digs);
      next[col + 1] = '.';
      go(cur, next, row, col, digs + 1);
      next[col + 1] = '#';
    } else {
      int fall = 1;
      int currow = row;
      while (currow + 2 < field.size() && field[currow + 2][col + 1] == '.') {
        ++fall;
        ++currow;
      }
      if (fall <= F) {
        string newcur = fall == 1 ? next : field[currow + 1];
        string newnext;
        if (currow + 2 < field.size()) {
          newnext = field[currow + 2];
        }
        go(newcur, newnext, currow + 1, col + 1, digs);
      }
    }
  }
}

bool isok(int col, int cols) {
  return col >= 0 && col < cols;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int rows, columns;
    cin >> rows >> columns >> F;
    field.resize(rows);
    for (int row = 0; row < rows; ++row) {
      cin >> field[row];
    }
    best_result = rows * columns + 1;
    string cur = field[0];
    string next = field[1];
    was.clear();
    go(cur, next, 0, 0, 0);
    cout << "Case #" << test_index + 1 << ": ";
    if (best_result < rows * columns + 1) {
      cout << "Yes " << best_result << endl;
    } else {
      cout << "No" << endl;
    }
    cerr << "test " << test_index + 1 << " of " << test_count << endl;
  }
  return 0;
}
