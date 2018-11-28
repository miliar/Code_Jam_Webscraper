// Problem B: Fair Warning (Qualification Round, Google Code Jam 2010)
// Author: Su Shi (Carmack.Shi@gmail.com)
// Usage: [execute] < inputfile > outputfile

#include <vector>
#include <iostream>
#include <cassert>
#include <cmath>
#include <algorithm>
using namespace std;

int GCD(int a, int b) {
  if (b == 0) return a;

  return GCD(b, a % b);
}

int FindOptimumAnniversary(vector<int> event_times) {
  size_t n = event_times.size();

  assert(n >= 2);

  sort(event_times.begin(), event_times.end());

  vector<int> adjacent_diffs(n - 1);
  for (size_t i = 0; i < n - 1; ++i) {
    adjacent_diffs[i] = event_times[i + 1] - event_times[i];
  }

  // Find maximum factor [T].
  int max_factor = adjacent_diffs[0];
  for (size_t j = 0; j < adjacent_diffs.size(); ++j) {
    max_factor = GCD(max_factor, adjacent_diffs[j]);
  }

  // Calculate the optimum anniversary.
  int minimum_multiples = (event_times[0] / max_factor) +
                             static_cast<int>((event_times[0] % max_factor) > 0);


  return minimum_multiples * max_factor - event_times[0];
}

int main() {
  int c, n;

  cin >> c;
  for (int i = 1; i <= c; ++i) {
    cin >> n;
    vector<int> event_times(n);

    for (int j = 0; j < n; ++j) {
      cin >> event_times[j];
    }

    cout << "Case #" << i << ": "
         << FindOptimumAnniversary(event_times) << endl;
  }

  return 0;
}
