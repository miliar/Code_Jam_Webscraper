#include <iostream>
#include <vector>
#include <algorithm>

int main(int argc, char** argv){
  unsigned int T;
  std::cin >> T;

  for (unsigned int i = 1; i <= T; i++) {
    // input
    unsigned int n;
    std::cin >> n;

    std::vector<int> X(n);
    for (unsigned int j = 0; j < n; j++) {
      std::cin >> X[j];
    }
    
    std::vector<int> Y(n);
    for (unsigned int j = 0; j < n; j++) {
      std::cin >> Y[j];
    }
    
    std::sort(X.begin(), X.end());
    std::sort(Y.begin(), Y.end());
    
    int ans = 0;
    for (unsigned int j = 0; j < n; j++) {
      ans += X[j] * Y[n-1-j];
    }

    
    // output
    std::cout << "Case #" << i << ": ";
    
    // answer
    std::cout << ans;

    // EOF
    std::cout << std::endl;
  }
  

}
  
