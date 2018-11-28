#include <cstring>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <set>
#include <map>
#include <vector>

//std::cin.ignore();

int main() {
  int T;
  std::cin >> T;
  for(int tt = 1; tt <= T; ++tt) {
    int N, K;
    std::cin >> N >> K;
    std::cout << "Case #" << tt << ": ";
    int f = 1 << N;
    if(K%f == f-1) {
      std::cout << "ON";
    } else {
      std::cout << "OFF";
    }
    std::cout << std::endl;
  }
}
