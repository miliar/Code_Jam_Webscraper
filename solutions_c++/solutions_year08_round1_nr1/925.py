#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>
#include <vector>

struct result {
  int x;
  result(int a) : x(a) {}
};

std::ostream&
operator<<(std::ostream& os, const result& r) {
  os << r.x;
  return os;
}

const result
process(std::istream& is) {
  int n;
  is >> n;

  std::vector<int> x(n), y(n);
  for (int i = 0; i < n; ++i) { is >> x[i]; }
  for (int i = 0; i < n; ++i) { is >> y[i]; }

  std::sort(x.begin(), x.end());
  std::sort(y.begin(), y.end());

  int z = 0;
  while (!x.empty()) {
    if ((x.front() < 0 && y.back() > 0) ||
        (x.front() > 0 && y.back() < 0)) {
      z += x.front() * y.back();
      x.erase(x.begin());
      y.pop_back();
    }
    else {
//    if ((x.back() > 0 && y.front() < 0) ||
//        (x.back() < 0 && y.front() > 0)) {
      z += y.front() * x.back();
      y.erase(y.begin());
      x.pop_back();
    }
#if 0
    else {
      z += x.back()*y.back();
      x.pop_back();
      y.pop_back();
    }
#endif
  }

  return result(z);
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
