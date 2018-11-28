#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>

using namespace std;

int position_of_last_one(const string &row) {
  for (int i = row.size() - 1; i >= 0; --i) {
    if (row[i] == '1') {
      return i;
    }
  }
  return -1;
}

int main() {
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);

  int test_cases;
  cin >> test_cases;
  for (int test = 1; test <= test_cases; ++test) {

    int n;
    cin >> n;
    vector<string> matrix(n, string(n,' '));
    for (int i = 0; i < n; ++i) {
      cin >> matrix[i];
    }

    int swaps_count = 0;
    for (int i = 0; i < n; ++i) {
      int candidate = -1;
      for (int j = i; j < n; ++j) {
        if (position_of_last_one(matrix[j]) <= i) {
          candidate = j;
          break;
        }
      }
      swaps_count += candidate - i;
      for (int j = candidate; j > i; --j) {
        swap(matrix[j], matrix[j - 1]);
      }
    }
    
    int answer = swaps_count;

    cout << "Case #" << test << ": " << answer << endl;
  }

  return 0;
}