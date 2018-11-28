#include <limits.h>
#include <cstring>
#include <cmath>
#include <cassert>
#include <limits>
#include <string>
#include <vector>
#include <deque>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <queue>
#include <iterator>
#include <set>
#include <map>
int main()
{
  int T;
  std::cin >> T;
  for(int test = 1; test <= T; ++test) {
    int N, L, H;
    std::cin >> N >> L >> H;
    std::vector<int> v(N);
    for(int i = 0; i < N; ++i) {
      std::cin >> v[i];
    }
    int res = -1;
    for(int i = L; i <= H; ++i) {
      int j;
      for(j = 0; j < N; ++j) {
        if(v[j]%i != 0 && i%v[j] != 0) {
          break;
        }
      }
      if(j == N) {
        res = i;
        break;
      }
    }
    std::cout << "Case #" << test << ": ";
    if(res == -1) {
      std::cout << "NO";
    } else {
      std::cout << res;
    }
    std::cout << std::endl;
  }
}
