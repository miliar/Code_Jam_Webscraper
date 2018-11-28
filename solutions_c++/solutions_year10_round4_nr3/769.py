#include <cassert>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <iterator>
#include <set>
#include <map>
#include <vector>
#include <deque>

//std::cin.ignore()
int map[102][102];

int letdoit()
{
  int days = 0;
  while(1) {
    int map2[102][102];
    memcpy(map2, map, sizeof(map));
    bool done = true;
    for(int y = 1; y <= 100; ++y) {
      for(int x = 1; x <= 100; ++x) {
        if(map[y][x] == 1) {
          done = false;
        }
        if(map[y][x] == 1 && map[y-1][x] == 0 && map[y][x-1] == 0) {
          map2[y][x] = 0;
        } else if(map[y][x] == 0 && map[y-1][x] == 1 && map[y][x-1] == 1) {
          map2[y][x] = 1;
          done = false;
        }
      }
    }
    if(done) {
      break;
    }
    ++days;
    memcpy(map, map2, sizeof(map));
  }
  return days;
}

int main() {
  int T;
  std::cin >> T;
  for(int t = 1; t <= T; ++t) {
    int R;
    std::cin >> R;
    memset(map, 0, sizeof(map));
    for(int i = 0; i < R; ++i) {
      int X1, Y1, X2, Y2;
      std::cin >> X1 >> Y1 >> X2 >> Y2;
      for(int y = Y1; y <= Y2; ++y) {
        for(int x = X1; x <= X2; ++x) {
          map[y][x] = 1;
        }
      }
    }
    std::cout << "Case #" << t << ": " <<  letdoit() << std::endl;
  }
}
