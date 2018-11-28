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

int MinCost(int round, int match_index, int missed, int first_team_index, int last_team_index, const vector<int>& costs, const vector<int>& miss, vector< vector<int> >& answer) {
  if (round == 0) {
    if (missed > miss[first_team_index]) {
      return -2;
    }
    return 0;
  }
  if (answer[match_index][missed] != -1)
    return answer[match_index][missed];
  int& result = answer[match_index][missed];
  result = -2;
  int left_dont_miss = MinCost(round - 1, 
                           2 * match_index + 1, 
                           missed, 
                           first_team_index, 
                           (first_team_index + last_team_index) / 2,
                           costs,
                           miss,
                           answer);
  int right_dont_miss = MinCost(round - 1,
                           2 * match_index + 2,
                           missed,
                           (first_team_index + last_team_index) / 2,
                           last_team_index,
                           costs,
                           miss,
                           answer);
  if (left_dont_miss != -2 && right_dont_miss != -2) {
    result = costs[match_index] + left_dont_miss + right_dont_miss;
  }
  int left_miss = MinCost(round - 1, 
                          2 * match_index + 1, 
                          missed + 1, 
                          first_team_index, 
                          (first_team_index + last_team_index) / 2,
                          costs,
                          miss,
                          answer);
  int right_miss = MinCost(round - 1,
                           2 * match_index + 2,
                           missed + 1,
                           (first_team_index + last_team_index) / 2,
                           last_team_index,
                           costs,
                           miss,
                           answer);
  if (left_miss != -2 && right_miss != -2) {
    if (result == -2 || result > left_miss + right_miss) {
      result = left_miss + right_miss;
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
    int rounds;
    cin >> rounds;
    int teams = (1 << rounds);
    vector<int> miss(teams);
    for (int i = 0; i < teams; ++i) {
      scanf("%d", &miss[i]);
    }
    vector<int> costs(teams - 1);
    for (int i = rounds - 1; i >= 0; --i) {
      int begin = (1 << i) - 1;
      for (int j = 0; j < (1 << i); ++j) {
        scanf("%d", &costs[j + begin]);
      }
    }
    vector< vector<int> > answer(teams - 1, vector<int>(teams - 1, -1));
    int result = MinCost(rounds, 0, 0, 0, teams, costs, miss, answer);
    cout << "Case #" << test_index + 1 << ": " << result << endl;
  }
  return 0;
}
