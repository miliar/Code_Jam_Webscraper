#include <limits.h>
#include <cstring>
#include <cmath>
#include <limits>
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
#include <stack>
int main()
{
  int T;
  std::cin >> T;
  for(int test = 1; test <= T; ++test) {
    int R, C, D;
    std::cin >> R >> C >> D;
    std::vector<std::string> v(R);
    for(int i = 0; i < R; ++i) {
      std::cin >> v[i];
    }
    int res = 0;
    for(int i = 0; i < R; ++i) {
      for(int j = 0; j < C; ++j) {
        for(int k = 3; i+k <= R && j+k <= C; ++k) {
          double dx = (double)(i+i+k-1)/2;
          double dy = (double)(j+j+k-1)/2;
          double vx = 0;
          double vy = 0;
          for(int u = i; u < i+k; ++u) {
            for(int w = j; w < j+k; ++w) {
              if((u == i && w == j) ||
                 (u == i && w == j+k-1) ||
                 (u == i+k-1 && w == j) ||
                 (u == i+k-1 && w == j+k-1)) {
                continue;
              }
              vx += (double)(u-dx)*(v[u][w]+D);
              vy += (double)(w-dy)*(v[u][w]+D);
            }
          }
          if(fabs(vx) < 1e-9 && fabs(vy) < 1e-9) {
            res = std::max(res, k);
          }
        }
      }
    }
    std::cout << "Case #" << test << ": ";
    if(res == 0) {
      std::cout << "IMPOSSIBLE" << std::endl;
    } else {
      std::cout << res << std::endl;
    }
  }
}
