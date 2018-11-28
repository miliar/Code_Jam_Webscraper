#include <iostream>
#include <vector>
#include <algorithm>

namespace CodeJam {
  namespace GoroSort {
    void solveCase(int c) {
      int value, misplaced = 0, n;

      std::cin >> n;
      for(int i = 1; i <= n; i++) {
	std::cin >> value;
	
	if(value != i) {
	  misplaced++;
	}
      }

      std::cout << "Case #" << c << ": " << misplaced << ".000000" << std::endl;
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

  CodeJam::GoroSort::solveAll();  

  return 0;
}
