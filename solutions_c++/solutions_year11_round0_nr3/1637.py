#include <iostream>
#include <vector>
#include <algorithm>

int main() {
  int T;
  std::cin >> T;
  for (int tcase = 1; tcase <= T; ++tcase) {
    int N;
    std::cin >> N;
    std::vector<int> C;
    for (int i = 0; i < N; ++i) {
      int tmp;
      std::cin >> tmp;
      C.push_back(tmp);
    }

    std::sort(C.begin(), C.end());

    std::vector<int> counts(17, 0);

    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < 17; ++j) {
	counts[j] += ((C[i] >> j) & 1);
      }
    }

    bool no = false;
    for (int i = 0; i < 17; ++i) {
      if (counts[i] % 2 == 1) {
	no = true;
      }
    }

    std::cout << "Case #" << tcase << ": ";
    if (no) {
      std::cout << "NO";
    } else {
      int sum = 0;
      for (int i = 0; i < C.size(); ++i) {
	sum += C[i];
      }

      std::cout << (sum - C[0]);
    }
    std::cout << "\n";
  }
}
