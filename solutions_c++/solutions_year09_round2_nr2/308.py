#include <climits>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <set>
#include <map>
#include <vector>
#include <string>

int main() {
  int C;
  std::cin >> C;
  std::cin.ignore();
  for(int c = 1; c <= C; ++c) {
    std::string line;
    getline(std::cin, line);
    bool nolast = std::next_permutation(line.begin(), line.end());
    if(!nolast) {
      std::sort(line.begin(), line.end());
      std::string::size_type p = line.find_first_not_of("0");
      std::swap(line[0], line[p]);
      line.insert(1, "0");
    }
    std::cout << "Case #" << c << ": " << line << std::endl;
  }
}
