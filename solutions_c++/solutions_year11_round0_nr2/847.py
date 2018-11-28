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

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int combine;
    cin >> combine;
    vector<string> combinations(combine);
    for (int i = 0; i < combine; ++i) {
      cin >> combinations[i];
    }
    int opposed;
    cin >> opposed;
    vector<string> oppositions(opposed);
    for (int i = 0; i < opposed; ++i) {
      cin >> oppositions[i];
    }
    int symbols;
    string input;
    cin >> symbols >> input;
    vector<char> current;
    for (int index = 0; index < symbols; ++index) {
      current.push_back(input[index]);
      bool was_combine = false;
      while (current.size() >= 2) {
        bool something_combined = false;
        for (int combination = 0; combination < combine; ++combination) {
          if ((combinations[combination][0] == current.back() && combinations[combination][1] == current[current.size() - 2]) ||
              (combinations[combination][0] == current[current.size() - 2] && combinations[combination][1] == current.back())) {
              current.pop_back();
              current.pop_back();
              current.push_back(combinations[combination][2]);
              something_combined = true;
              break;
          }
        }
        if (!something_combined) {
          break;
        } else {
          was_combine = true;
        }
      }
      if (was_combine) {
        continue;
      }
      for (int opposition = 0; opposition < opposed; ++opposition) {
        for (int i = 0; i + 1 < current.size(); ++i) {
          if ((oppositions[opposition][0] == current[i] && oppositions[opposition][1] == current.back()) ||
              (oppositions[opposition][0] == current.back() && oppositions[opposition][1] == current[i])) {
            current.clear();
            break;
          }
        }
        if (current.empty()) {
          break;
        }
      }
    }
    cout << "Case #" << test_index + 1 << ": [";
    cerr << "Case #" << test_index + 1 << ": [" << endl;
    for (int i = 0; i + 1 < current.size(); ++i) {
      cout << current[i] << ", ";
    }
    if (!current.empty()) {
      cout << current.back();
    }
    cout << "]" << endl;
  }
  return 0;
}
