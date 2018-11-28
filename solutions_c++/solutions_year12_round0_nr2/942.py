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
    int N, S, p;
    std::cin >> N >> S >> p;
    std::vector<int> v(N);
    for(int i = 0; i < N; ++i) {
      std::cin >> v[i];
    }
    int cnt = 0;
    int sup = 0;
    for(int i = 0; i < N; ++i) {
      if(v[i] >= p*3-2) {
        ++cnt;
      } else if(p*3-4 >= 0 && v[i] >= p*3-4) {
        ++sup;
      }
    }
    int res = cnt+std::min(sup, S);
    std::cout << "Case #" << test << ": " << res << std::endl;
  }
}
