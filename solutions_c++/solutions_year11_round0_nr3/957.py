#include <iostream>

namespace CodeJam {
  namespace CandySplitting {
    void solveCase(int c) {
      int smallest = 10000000;
      int totalValue = 0;
      int totalXor = 0;

      int n; std::cin >> n;
      for(int i = 0; i < n; i++) {
	int value;
	std::cin >> value;
	
	smallest = std::min(smallest, value);
	totalValue += value;
	totalXor ^= value;
      }

      std::cout << "Case #" << c << ": ";

      if (totalXor != 0) {
	std::cout << "NO";
      } else {
	std::cout << (totalValue - smallest);
      }
      
      std::cout << std::endl;
    }

    void solveAll() {
      int k; std::cin >> k;

      for(int i = 1; i <= k; i++) {
	solveCase(i);
      }
    }
  }
}

int main() {
  std::ios_base::sync_with_stdio(false);

  CodeJam::CandySplitting::solveAll();  

  return 0;
}
