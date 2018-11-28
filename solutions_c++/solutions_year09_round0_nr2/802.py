#include <algorithm>
#include <cassert>
#include <cstdio>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

#define PROBLEM_ID "B"

const int dr[4] = {-1, 0, 0, 1};
const int dc[4] = {0, -1, 1, 0};

pii GetSink(const vector< vector<int> >& heights, int row, int col, vector< vector<pii> >* sink) {
  if (sink->at(row).at(col).first != -1) {
    return sink->at(row).at(col);
  }
  int lowest = numeric_limits<int>::max();
  for (int dir = 0; dir < 4; ++dir) {
    int nrow = row + dr[dir];
    int ncol = col + dc[dir];
    if (nrow >= 0 && nrow < heights.size() && ncol >= 0 && ncol < heights[0].size()) {
      if (heights[nrow][ncol] < lowest) {
        lowest = heights[nrow][ncol];
      }
    }
  }
  if (lowest >= heights[row][col]) {
    return sink->at(row).at(col) = MP(row, col);
  }
  for (int dir = 0; dir < 4; ++dir) {
    int nrow = row + dr[dir];
    int ncol = col + dc[dir];
    if (nrow >= 0 && nrow < heights.size() && ncol >= 0 && ncol < heights[0].size()) {
      if (heights[nrow][ncol] == lowest) {
        return sink->at(row).at(col) = GetSink(heights, nrow, ncol, sink);
      }
    }
  }
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_number = 0; test_number < test_count; ++test_number) {
    int rows, cols;
    cin >> rows >> cols;
    vector< vector<int> > heights(rows, vector<int>(cols));
    for (int i = 0; i < rows; ++i) {
      for (int j = 0; j < cols; ++j) {
        cin >> heights[i][j];
      }
    }
    vector< vector<pii> > sink(rows, vector<pii>(cols, MP(-1, -1)));
    for (int row = 0; row < rows; ++row) {
      for (int col = 0; col < cols; ++col) {
        GetSink(heights, row, col, &sink);
      }
    }
    vector< vector<char> > answer(rows, vector<char>(cols));
    int color = -1;
    map<pii, int> colors;
    for (int row = 0; row < rows; ++row) {
      for (int col = 0; col < cols; ++col) {
        pii cur_sink = sink[row][col];
        if (colors.find(cur_sink) == colors.end()) {
          ++color;
          colors[cur_sink] = color;
          answer[cur_sink.first][cur_sink.second] = color + 'a';
        }
        answer[row][col] = answer[cur_sink.first][cur_sink.second];
      }
    }
    cout << "Case #" << test_number + 1 << ":" << endl;
    for (int row = 0; row < rows; ++row) {
      for (int col = 0; col < cols; ++col) {
        cout << answer[row][col];
        if (col + 1 < cols) {
          cout << ' ';
        }
      }
      cout << endl;
    }
  }
  return 0;
}
