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
    int actions;
    cin >> actions;
    const int BUTTONS = 100;
    const int INF = ll(1) << 30;
    vvvi min_time(actions + 1, vvi(BUTTONS, vi(BUTTONS, INF)));
    min_time[0][0][0] = 0;
    for (int action = 0; action < actions; ++action) {
      string which;
      int index;
      cin >> which >> index;
      --index;
      for (int first_position = 0; first_position < BUTTONS; ++first_position) {
        for (int second_position = 0; second_position < BUTTONS; ++second_position) {
          if (min_time[action][first_position][second_position] == INF) {
            continue;
          }
          int delta = -1;
          if (which == "O") {
            delta = abs(first_position - index) + 1;
          } else {
            delta = abs(second_position - index) + 1;
          }
          if (which == "O") {
            for (int moving_position = max(0, second_position - delta); moving_position < BUTTONS && moving_position <= second_position + delta; ++moving_position) {
              min_time[action + 1][index][moving_position] = 
                  min(min_time[action + 1][index][moving_position],
                      min_time[action][first_position][second_position] + delta);
            }
          } else {
            for (int moving_position = max(0, first_position - delta); moving_position < BUTTONS && moving_position <= first_position + delta; ++moving_position) {
              min_time[action + 1][moving_position][index] = 
                  min(min_time[action + 1][moving_position][index],
                      min_time[action][first_position][second_position] + delta);
            }
          }
        }
      }
    }
    int res = INF;
    for (int first_position = 0; first_position < BUTTONS; ++first_position) {
      for (int second_position = 0; second_position < BUTTONS; ++second_position) {
        res = min(res, min_time[actions][first_position][second_position]);
      }
    }
    cout << "Case #" << test_index + 1 << ": " << res << endl;
    cerr << "Case #" << test_index + 1 << ": " << res << endl;
  }
  return 0;
}
