#include <iostream>
#include <vector>

int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    int N;
    std::cin >> N;
    int min = 1000000;
    int bits = 0;
    int total = 0;
    for (int i = 1; i <= N; ++i) {
      int value;
      std::cin >> value;
      if (value < min) {
        min = value;
      }
      bits ^= value;
      total += value;
    }
    std::cout << "Case #" << t << ": ";
    if (bits != 0) {
      std::cout << "NO";
    } else {
      std::cout << (total - min);
    }
    std::cout << std::endl;
  }
  return 0;
}
