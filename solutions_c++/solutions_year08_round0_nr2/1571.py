#include <iostream>
#include <fstream>
#include <cstdlib>
#include <deque>
#include <vector>
#include <algorithm>
#include <iterator>

int
read_time(std::istream& is) {
  std::string t;

  is >> t;
  t[2] = '\0';
  return 60 * atoi(t.c_str()) + atoi(t.c_str() + 3);
}

template <typename T>
void
print(const T& t) {
  std::copy(t.begin(), t.end(), std::ostream_iterator<int>(std::cout, ", "));
  std::cout << '\n';
}

int
count(std::deque<int>& depart, const std::deque<int>& arrival, int T) {
  int c = 0;

  while (!depart.empty()) {
    std::deque<int> tmp = arrival;

    while (!tmp.empty() && tmp.front() + T > depart.front())
      tmp.pop_front();
    if (tmp.empty())
      ++c;
    depart.pop_front();
  }
  return c;
}

int
main(int argc, char** argv) {
  int CASES;
  std::ifstream is(argv[1]);

  is >> CASES;
  for (int i = 1; i <= CASES; ++i) {
    int T, NA, NB;
    std::deque<int> DepartsA, ArrivalsB, DepartsB, ArrivalsA;

    is >> T >> NA >> NB;
    while (NA--) {
      DepartsA.push_back(read_time(is));
      ArrivalsB.push_back(read_time(is) + T);
    }
    while (NB--) {
      DepartsB.push_back(read_time(is));
      ArrivalsA.push_back(read_time(is) + T);
    }
    std::sort(DepartsA.begin(), DepartsA.end());
    std::sort(DepartsB.begin(), DepartsB.end());
    std::sort(ArrivalsA.begin(), ArrivalsA.end());
    std::sort(ArrivalsB.begin(), ArrivalsB.end());

    int a = 0;
    int b = 0;

    while (!DepartsA.empty()) {
      if (!ArrivalsA.empty() && ArrivalsA.front() <= DepartsA.front())
        ArrivalsA.pop_front();
      else
        ++a;
      DepartsA.pop_front();
    }
    
    while (!DepartsB.empty()) {
      if (!ArrivalsB.empty() && ArrivalsB.front() <= DepartsB.front())
        ArrivalsB.pop_front();
      else
        ++b;
      DepartsB.pop_front();
    }
    
    std::cout << "Case #" << i << ": " << a << ' ' << b << '\n';
  }
  return 0;
}
