#include <iostream>
#include <sstream>
#include <inttypes.h>
#include <vector>
#include <algorithm>
#include <numeric>
#include <fstream>

template<typename T>
std::string to_s(T v)
{
  std::stringstream s;
  s << v;
  return s.str();
}

class Descent {
public:
  bool operator()(int lhs, int rhs) const
  {
    return lhs > rhs;
  }
};

int main(int argc, char** argv) {
  std::ifstream in(argv[1]);
  int numCase;
  in >> numCase;
  for(int cases = 0; cases < numCase; ++cases) {
    std::string line;
    int ints;
    in >> ints;
    std::vector<int> v1;
    std::vector<int> v2;
    for(int i = 0; i < ints; ++i) {
      int x;
      in >> x;
      v1.push_back(x);
    }
    for(int i = 0; i < ints; ++i) {
      int x;
      in >> x;
      v2.push_back(x);
    }


    std::sort(v1.begin(), v1.end());
    std::sort(v2.begin(), v2.end(), Descent());
    
    std::vector<int> result(v1.size());
    
    std::cout << "Case #" << cases+1 << ": " << std::inner_product(v1.begin(), v1.end(), v2.begin(), 0) << std::endl;
  }
}
