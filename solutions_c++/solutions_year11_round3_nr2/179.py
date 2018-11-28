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
int L, N, C;
long long t;
std::vector<int> A;
int main()
{
  int T;
  std::cin >> T;
  for(int test = 1; test <= T; ++test) {
    std::cin >> L >> t >> N >> C;
    std::vector<int> g = std::vector<int>(C);
    for(int i = 0; i < C; ++i) {
      std::cin >> g[i];
    }
    A = std::vector<int>(N+1);
    for(int i = 0; i < N; ++i) {
      A[i] = g[i%C];
    }
    long long cumtime = 0;
    int start = 0;
    for(start = 0; start < N; ++start) {
      if(cumtime >= t) {
        break;
      }
      cumtime += A[start]*2;
    }
    // std::cout << "cumtime=" << cumtime << std::endl;
    // std::cout << "start=" << start << std::endl;
    if(cumtime > t) {
      long long length = (cumtime-t)/2;
      A[N] = length;
      ++N;
      cumtime -= cumtime-t;
      //std::cout << "length after booster = " << length << std::endl;
    }
    std::sort(A.begin()+start, A.end(), std::greater<int>());
    int max = std::min(start+L, N);
    //std::cout << "max booster=" << max << std::endl;
    for(int i = start; i < max; ++i) {
      cumtime += A[i];
    }
    for(int i = max; i < N; ++i) {
      cumtime += A[i]*2;
    }
    std::cout << "Case #" << test << ": " << cumtime << std::endl;
  }
}
