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
    int N;
    std::cin >> N;
    std::vector<std::string> v(N);
    for(int i = 0; i < N; ++i) {
      std::cin >> v[i];
    }
    std::vector<double> WP(N);
    std::vector<double> OWP(N);
    std::vector<double> OOWP(N);
    for(int i = 0; i < N; ++i) {
      int win = std::count(v[i].begin(), v[i].end(), '1');
      int lose = std::count(v[i].begin(), v[i].end(), '0');
      WP[i] = (double)win/(win+lose);
    }
    for(int i = 0; i < N; ++i) {
      double t = 0;
      int num = 0;
      for(int j = 0; j < N; ++j) {
        if(v[j][i] == '.') {
          continue;
        }
        int win = std::count(v[j].begin(), v[j].end(), '1');
        int lose = std::count(v[j].begin(), v[j].end(), '0');
        if(v[j][i] == '1') {
          --win;
        }
        if(v[j][i] == '0') {
          --lose;
        }
        ++num;
        t += (double)win/(win+lose);
      }
      OWP[i] = t/num;
    }
    for(int i = 0; i < N; ++i) {
      double t = 0;
      int num = 0;
      for(int j = 0; j < N; ++j) {
        if(v[j][i] == '.') {
          continue;
        }
        ++num;
        t += OWP[j];
      }
      OOWP[i] = t/num;
    }
    std::cout << "Case #" << test << ":" << std::endl;
    for(int i = 0; i < N; ++i) {
      std::cout << 0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i] << std::endl;
    }
  }
}
