#include <limits.h>
#include <cstring>
#include <cmath>
#include <cassert>
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
    int N;
    std::cin >> N;
    int total = 0;
    std::vector<int> v(N);
    for(int i = 0; i < N; ++i) {
      std::cin >> v[i];
      total += v[i];
    }
    std::sort(v.begin(), v.end());
    std::vector<int> bits(10);
    for(int i = 0; i < N; ++i) {
      int x = v[i];
      for(int j = 0; j < 10; ++j) {
        if(x&(1 << j)) {
          ++bits[j];
        }
      }
    }
    bool ok = true;
    for(int i = 0; i < 10; ++i) {
      if(bits[i]%2 != 0) {
        ok = false;
        break;
      }
    }
    std::cout << "Case #" << test << ": ";
    if(ok) {
      std::cout << total-v[0];
    } else {
      std::cout << "NO";
    }
    std::cout << std::endl;
  }
}
