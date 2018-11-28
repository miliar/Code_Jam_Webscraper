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
    int R, C;
    std::cin >> R >> C;
    std::vector<std::string> v(R);
    for(int i = 0; i < R; ++i) {
      std::cin >> v[i];
    }
    for(int i = 0; i < R-1; ++i) {
      for(int j = 0; j < C-1; ++j) {
        if(v[i][j] == '#' && v[i][j+1] == '#' &&
           v[i+1][j] == '#' && v[i+1][j+1] == '#') {
          v[i][j] = v[i+1][j+1] = '/';
          v[i][j+1] = v[i+1][j] = '\\';
        }
      }
    }
    bool ok = true;
    for(int i = 0; i < R; ++i) {
      if(v[i].find('#') != std::string::npos) {
        ok = false;
        break;
      }
    }
    std::cout << "Case #" << test << ":" << std::endl;
    if(ok) {
      std::copy(v.begin(), v.end(), std::ostream_iterator<std::string>(std::cout, "\n"));
    } else {
      std::cout << "Impossible" << std::endl;
    }
  }
}
