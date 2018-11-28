#include <iostream>
#include <numeric>
#include <map>
#include <cstdio>
#include <cstring>


int main(int argc, char** argv)
{
  int T;

  std::cin >> T;

  for (int i = 0; i < T; i ++) {
    int A, B;

    std::cin >> A >> B;

    std::map<std::pair<int, int>, char> map;

    for (int n = A; n <= B; n ++) {
      char s[32];
      
      sprintf(s, "%d", n);
      
      int size = strlen(s);
      
      sprintf(s + size, "%d", n);
      
      for (int j = size, k = size * 2; j > 0; j --, k --, s[k] = '\0') {
	int m = atoi(s + j);
	
	if (n < m && m <= B)
	  map[std::make_pair<int, int>(n, m)] = 0;
      }
    }

    std::cout << "Case #" << i + 1 << ": " << map.size() << std::endl;
  }
}
