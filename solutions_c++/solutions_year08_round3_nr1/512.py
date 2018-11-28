#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>
#include <vector>

struct result {
  int64_t x;
  result(int64_t a) : x(a) {}
};

std::ostream&
operator<<(std::ostream& os, const result& r) {
  os << r.x;
  return os;
}

const result
process(std::istream& is) {
  int64_t x = 0;
  int P, K, L;
  std::vector<int> f;

  is >> P >> K >> L;
  for (int i = 0; i < L; ++i) {
    int l;
    is >> l;
    f.push_back(l);
  }

  std::sort(f.begin(), f.end());
  int r = 1;
  int l = 1;
  for (int i = L-1; i >=0; --i) {
    x += r*f[i];
    ++l;
    if (l > K) {
      l = 1;
      ++r;
    }
  }
  
  return result(x);
}

int
main(int argc, char** argv) {
  int cases = 0;
  std::ifstream is(argv[1]);

  is >> cases;
  for (int i = 1; i <= cases; ++i)
    std::cout << "Case #" << i << ": " << process(is) << '\n';
  return 0;
}
