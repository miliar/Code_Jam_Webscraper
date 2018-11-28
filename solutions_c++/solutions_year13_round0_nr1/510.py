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
bool check(const std::vector<std::string>& v, char c)
{
  for(int i = 0; i < 4; ++i) {
    bool ok1 = true, ok2 = true;
    for(int j = 0; j < 4 && (ok1 || ok2); ++j) {
      if(v[i][j] != c && v[i][j] != 'T') {
        ok1 = false;
      }
      if(v[j][i] != c && v[j][i] != 'T') {
        ok2 = false;
      }
    }
    if(ok1 || ok2) return true;
  }
  bool ok1 = true, ok2 = true;
  for(int i = 0; i < 4; ++i) {
    if(v[i][i] != c && v[i][i] != 'T') {
      ok1 = false;
    }
    if(v[3-i][i] != c && v[3-i][i] != 'T') {
      ok2 = false;
    }
  }
  return ok1 || ok2;
}
bool occupied(const std::vector<std::string>& v)
{
  for(int i = 0; i < 4; ++i) {
    if(std::find(v[i].begin(), v[i].end(), '.') != v[i].end()) {
      return false;
    }
  }
  return true;
}
int main()
{
  int tests;
  std::cin >> tests;
  for(int test = 1; test <= tests; ++test) {
    std::vector<std::string> v(4);
    for(int i = 0; i < 4; ++i) {
      std::cin >> v[i];
    }
    std::string res;
    if(check(v, 'X')) {
      res = "X won";
    } else if(check(v, 'O')) {
      res = "O won";
    } else if(occupied(v)) {
      res = "Draw";
    } else {
      res = "Game has not completed";
    }
    std::cout << "Case #" << test << ": " << res << std::endl;
  }
}

