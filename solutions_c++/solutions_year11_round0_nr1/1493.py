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
    int n;
    std::cin >> n;
    std::vector<std::pair<char, int> > order(n);
    for(int i = 0; i < n; ++i) {
      std::cin >> order[i].first >> order[i].second;
    }
    std::vector<int> pos(2, 1);
    std::vector<int> lastmove(2);
    int t = 0;
    for(int i = 0; i < n; ++i) {
      int j;
      if(order[i].first == 'B') {
        j = 0;
      } else {
        j = 1;
      }
      int d = abs(pos[j]-order[i].second);
      int nt = std::max(lastmove[(j+1)%2]+1, lastmove[j]+d+1);
      if(nt > t) {
        t = nt;
        lastmove[j] = t;
      } else {
        lastmove[j] = nt;
      }
      pos[j] = order[i].second;
    }
    std::cout << "Case #" << test << ": " << t << std::endl;
  }
}
