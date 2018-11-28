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
int N;
struct Node {
  std::vector<int> next;
};
std::vector<Node> nodes;
std::vector<int> used;
bool dfs(int x)
{
  used[x] = 1;
  for(std::vector<int>::const_iterator i = nodes[x].next.begin();
      i != nodes[x].next.end(); ++i) {
    int y = *i;
    if(used[y] == 0) {
      bool rv = dfs(y);
      if(rv) {
        return rv;
      }
    } else {
      return true;
    }
  }
  return false;
}
int main()
{
  int T;
  std::cin >> T;
  for(int test = 1; test <= T; ++test) {
    std::cin >> N;
    nodes = std::vector<Node>(N+1);
    std::vector<int> knum(N+1);
    for(int i = 1; i <= N; ++i) {
      int M;
      std::cin >> M;
      knum[i] = M;
      for(int j = 0; j < M; ++j) {
        int k;
        std::cin >> k;
        nodes[k].next.push_back(i);
        //std::cout << i << " -> " << k << std::endl;
      }
    }
    std::string res = "No";
    for(int i = 1; i <= N; ++i) {
      if(knum[i] == 0) {
        used = std::vector<int>(N+1);
        //std::cout << "start " << i << std::endl;
        if(dfs(i)) {
          res = "Yes";
          break;
        }
      }
    }
    std::cout << "Case #" << test << ": " << res << std::endl;
  }
}
