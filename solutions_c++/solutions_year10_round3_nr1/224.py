#include <cassert>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <iterator>
#include <set>
#include <map>
#include <vector>

//std::cin.ignore();

int main() {
  int T;
  std::cin >> T;
  for(int t = 1; t <= T; ++t) {
    int N;
    std::cin >> N;
    std::vector<int> left(N, 0);
    std::vector<int> right(N, 0);
    for(int i = 0; i < N; ++i) {
      std::cin >> left[i] >> right[i];
    }
    int count = 0;
    for(int i = 0; i < N; ++i) {
        for(int j = 0; j < N; ++j) {
          if(left[i] > left[j] && right[i] < right[j]) {
            ++count;
          }
        }
    }
    std::cout << "Case #" << t << ": " << count << std::endl;
  }
}
