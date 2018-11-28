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

//std::cin.ignore();

int main() {
  int T;
  std::cin >> T;
  for(int t = 1; t <= T; ++t) {
    int P;
    std::cin >> P;
    int numTeam = 1 << P;
    std::vector<std::pair<int, int> > M;
    for(int i = 0; i < numTeam; ++i) {
      int m;
      std::cin >> m;
      M.push_back(std::make_pair(m, i));
    }
    for(int i = 0; i < numTeam-1; ++i) {
      int x;
      std::cin >> x;
    }
    std::sort(M.begin(), M.end());
    int tickets = 0;
    std::vector<int> matches(numTeam, 0);
    for(int team = 0; team < numTeam; ++team) {
      int miss = M[team].first;
      int t = M[team].second;
      //std::cout << "team " << t << std::endl;
      for(int r = 1; r <= P; ++r) {
        int match = (1 << (P-r))+t/2;
        //std::cout << "round " << r << std::endl;
        if(miss) {
          if(matches[match] == 0) {
            --miss;
          }
        } else {
          if(matches[match] ==  0) {
            //std::cout << "buy " << match << std::endl;
            ++tickets;
            matches[match] = 1;
          }
        }
        t = match-(1 << (P-r));
      }
    }
    std::cout << "Case #" << t << ": " << tickets << std::endl;
  }
}
