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

struct state {
  vector<pii> positions;
  bool must_connect;

  bool normalize() {
    sort(positions.begin(), positions.end());
    int size = positions.size();
    return unique(positions.begin(), positions.end()) - positions.begin() == size;
  }

  int find(pii pos) {
    for (int i = 0; i < positions.size(); ++i) {
      if (positions[i] == pos) {
        return i;
      }
    }
    return -1;
  }

  bool is_connected() {
    vector<bool> was(positions.size(), false);
    was[0] = true;
    queue<pii> q;
    q.push(positions[0]);
    while (!q.empty()) {
      pii cur = q.front();
      q.pop();
      for (int dx = -1; dx <= 1; ++dx) {
        for (int dy = -1; dy <= 1; ++dy) {
          if (abs(dx) + abs(dy) == 1) {
            pii next = cur;
            next.first = cur.first + dx;
            next.second = cur.second + dy;
            int index = -1;
            for (int i = 0; i < positions.size(); ++i) {
              if (positions[i] == next) {
                index = i;
                break;
              }
            }
            if (index != -1 && !was[index]) {
              was[index] = true;
              q.push(next);
            }
          }
        }
      }
    }
    for (int i = 0; i < positions.size(); ++i) {
      if (!was[i]) {
        return false;
      }
    }
    return true;
  }
};

bool operator<(const state& a, const state& b) {
  if (a.must_connect != b.must_connect) {
    return a.must_connect < b.must_connect;
  }
  return a.positions < b.positions;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    cerr << "Test " << test_index + 1 << " of " << test_count << endl;
    map<state, int> answer;
    state init, final;
    init.must_connect = false;
    int rows, cols;
    cin >> rows >> cols;
    vector<string> field(rows);
    for (int i = 0; i < rows; ++i) {
      cin >> field[i];
    }
    for (int row = 0; row < rows; ++row) {
      for (int col = 0; col < cols; ++col) {
        if (field[row][col] == 'o' || field[row][col] == 'w') {
          init.positions.push_back(MP(row, col));
        }
        if (field[row][col] == 'x' || field[row][col] == 'w') {
          final.positions.push_back(MP(row, col));
        }
      }
    }
    answer[init] = 0;
    queue<state> q;
    q.push(init);
    int result = -1;
    while (!q.empty()) {
      state cur = q.front();
      q.pop();
      if (cur.positions == final.positions) {
        result = answer[cur];
        break;
      }
      for (int pos_index = 0; pos_index < cur.positions.size(); ++pos_index) {
        pii cur_position = cur.positions[pos_index];
        for (int dx = -1; dx <= 1; ++dx) {
          for (int dy = -1; dy <= 1; ++dy) {
            if (abs(dx) + abs(dy) == 1) {
              pii next_position = cur_position;
              next_position.first += dx;
              next_position.second += dy;
              pii from_position = cur_position;
              from_position.first -= dx;
              from_position.second -= dy;
              if (next_position.first >= 0 && 
                  next_position.first < rows && 
                  next_position.second >= 0 && 
                  next_position.second < cols && 
                  field[next_position.first][next_position.second] != '#' &&
                  cur.find(next_position) == -1 &&
                  from_position.first >= 0 &&
                  from_position.first < rows &&
                  from_position.second >= 0 &&
                  from_position.second < cols &&
                  field[from_position.first][from_position.second] != '#' &&
                  cur.find(from_position) == -1) {
                state next = cur;
                next.positions[pos_index] = next_position;
                if (next.normalize()) {
                  bool next_connected = next.is_connected();
                  if (cur.must_connect && !next_connected) {
                    continue;
                  }
                  if (!next_connected) {
                    next.must_connect = true;
                  } else {
                    next.must_connect = false;
                  }
                  if (answer.find(next) == answer.end()) {
                    answer[next] = answer[cur] + 1;
                    q.push(next);
                  }
                }
              }
            }
          }
        }
      }
    }
    cout << "Case #" << test_index + 1 << ": " << result << endl;

  }
  return 0;
}
