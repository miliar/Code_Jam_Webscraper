#include <algorithm>
#include <iostream>
#include <vector>

int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    int N;
    std::cin >> N;
    std::vector<int> values(N);
    for (int n = 0; n < N; ++n) {
      std::cin >> values[n];
    }
    std::vector<int> sorted_values(values);
    std::sort(sorted_values.begin(), sorted_values.end());
    int num_diffs = 0;
    for (int n = 0; n < N; ++n) {
      if (values[n] != sorted_values[n]) {
        ++num_diffs;
      }
    }
    std::cout << "Case #" << t << ": " << num_diffs << std::endl;
  }
  return 0;
}
