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
std::string tos(int n)
{
  std::string s;
  while(n) {
    s += n%10+'0';
    n /= 10;
  }
  std::reverse(s.begin(), s.end());
  return s;
}
int main()
{
  int T;
  std::cin >> T;
  for(int test = 1; test <= T; ++test) {
    int A, B;
    std::cin >> A >> B;
    int ans = 0;
    for(int i = A; i < B; ++i) {
      std::string n = tos(i);
      std::string m = n;
      std::set<int> used;
      for(int j = 0; j < (int)n.size()-1; ++j) {
        std::rotate(m.begin(), m.begin()+1, m.end());
        int mint = strtol(m.c_str(), 0, 10);
        if(i < mint && mint <= B && used.count(mint) == 0) {
          //std::cout << "(" << n << ", " << m << ")" << std::endl;
          used.insert(mint);
          ++ans;
        }
      }
    }
    std::cout << "Case #" << test << ": " << ans << std::endl;
  }
}
