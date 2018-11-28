#include <iostream>
#include <vector>
#include <algorithm>

int main(int argc, char** argv){
  unsigned int n;
  std::cin >> n;

  char str[100];
  for (unsigned int i = 1; i <= n; i++) {
    // input
    unsigned int S;
    std::cin >> S;

    std::cin.getline(str, 100);

    std::vector<std::string> engines(S);
    for (unsigned int j = 0; j < S; j++) {
      char str[100];
      std::cin.getline(str, 100);
      engines[j] = std::string(str);
    }
 
    unsigned int Q;
    std::cin >> Q;

    std::cin.getline(str, 100);
    
    std::vector<std::string> queries(Q);
    for (unsigned int j = 0; j < Q; j++) {
      char str[100];
      std::cin.getline(str, 100);
      queries[j] = std::string(str);
    }

    int Y = (Q == 0) ? 0 : -1;
    for (unsigned int j = 0; j < Q;) {
      std::vector<unsigned int> runs;
      
      for (unsigned int k = 0; k < S; k++) {
	unsigned int r = j;
	while ((r < Q) && (queries[r] != engines[k])) {
	  r++;
	}
    
	runs.push_back(r);
      }
      
      j = *std::max_element(runs.begin(), runs.end());
      Y++;
    }
    
    // output
    std::cout << "Case #" << i << ": ";
    
    // answer
    std::cout << Y;

    // EOF
    std::cout << std::endl;
  }
  

}
  
