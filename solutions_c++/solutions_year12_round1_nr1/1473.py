#include <limits.h>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <limits>
#include <cassert>
#include <string>
#include <vector>
#include <deque>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <queue>
#include <iterator>
#include <set>
static const int INF = std::numeric_limits<int>::max();
int main()
{
  int T;
  std::cin >> T;
  for(int test = 1; test <= T; ++test) {
    int A, B;
    std::cin >> A >> B;
    std::vector<double> P(A);
    double pac = 1;
    for(int i = 0; i < A; ++i) {
      std::cin >> P[i];
      pac *= P[i];
    }
    double res1 = pac*(B-A+1) + (1-pac)*(B-A+1+B+1);
    double res2 = 2+B;
    double p = 1;
    double res3 = INF;
    for(int i = 0; i < A; ++i) {
      double pi = p*(A-i+B-i+1) + (1-p)*(A-i+B-i+1+B+1);
      //std::cout << "pi=" << pi << std::endl;
      res3 = std::min(res3, pi);
      p *= P[i];
    }
    // std::cout << "keep = " << res1 << std::endl;
    // std::cout << "rightaway = " << res2 << std::endl;
    std::cout << "Case #" << test << ": " << std::fixed << std::setprecision(9)
              << std::min(res1, std::min(res2, res3))
              << std::endl;
  }
}
