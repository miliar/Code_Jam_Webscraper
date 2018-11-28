#include <iostream>

namespace CodeJam {
  namespace X {
    void solveCase(int c) {
      bool possible;
      
      long long n;
      int pd, pg;

      std::cin >> n >> pd >> pg;

      if((pd % 100) == 0) {
	possible = true;
      } else if((pd % 50) == 0) {
	possible = (n >= 2);
      } else if((pd % 25) == 0) {
	possible = (n >= 4);
      } else if((pd % 20) == 0) {
	possible = (n >= 5);
      } else if((pd % 10) == 0) {
	possible = (n >= 10);
      } else if((pd % 5) == 0) {
	possible = (n >= 20);
      } else if((pd % 4) == 0) {
	possible = (n >= 25);
      } else if((pd % 2) == 0) {
	possible = (n >= 50);
      } else {
	possible = (n >= 100);
      }

      if((pd > 0 && pg == 0) || (pd < 100 && pg == 100)) {
	possible = false;
      }

      std::cout << "Case #" << (c + 1) << ": " 
		<< (possible ? "Possible" : "Broken") << std::endl;
    }

    void solveAll() {
      int k;

      std::cin >> k;

      for(int i = 0; i < k; i++) {
	solveCase(i);
      }
    }
  }
}

int main() {
  std::ios_base::sync_with_stdio(false);

  CodeJam::X::solveAll();

  return 0;
}
