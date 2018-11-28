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
    int length, run, walk, run_time;
    cin >> length >> walk >> run >> run_time;
    int walkway_count;
    cin >> walkway_count;
    vector< vector<int> > walkways(walkway_count, vector<int>(3));
    for (int i = 0; i < walkway_count; ++i) {
      cin >> walkways[i][1] >> walkways[i][2] >> walkways[i][0];
    }
    sort(walkways.begin(), walkways.end());
    double run_time_left = run_time;
    double res = 0;
    int no_walkway = length;
    for (int i = 0; i < walkway_count; ++i) {
      no_walkway -= (walkways[i][2] - walkways[i][1]);
    }
    if (run_time * run >= no_walkway) {
      double time = double(no_walkway) / double(run);
      res = time;
      run_time_left -= time;
    } else {
      run_time_left = 0;
      res = run_time + double(no_walkway - run_time * run) / double(walk);
    }
    for (int walkway_index = 0; walkway_index < walkways.size(); ++walkway_index) {
      int walkway_length = walkways[walkway_index][2] - walkways[walkway_index][1];
      int walkway_speed = walkways[walkway_index][0];
      if (run_time_left > 0) {
        if (run_time_left * (run + walkway_speed) >= walkway_length) {
          double time = double(walkway_length) / double(run + walkway_speed);
          res += time;
          run_time_left -= time;
        } else {
          res += run_time_left + double(walkway_length - (run + walkway_speed) * run_time_left) / double(walk + walkway_speed);
          run_time_left = 0;
        }
      } else {
        res += double(walkway_length) / double(walk + walkway_speed);
      }
    }
    cout << "Case #" << test_index + 1 << ": ";
    printf("%.10lf\n", res);
    cerr << "Case #" << test_index + 1 << ": ";
    fprintf(stderr, "%.10lf\n", res);
  }
  return 0;
}
