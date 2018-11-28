#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <utility>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <string>


std::vector<int> a;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  
  int t, n;
  
  std::cin >> t;
  for (int tnum = 1; tnum <= t; ++tnum) {
    a.clear();
    std::cin >> n;
    int sm = 0;
    for (int i = 0; i < n; ++i) {
      int v;
      std::cin >> v;
      sm ^= v;
      a.push_back(v);
    }
    int ans = 0;
    if (sm == 0 && n >= 2) {
      std::sort(a.begin(), a.end());
      for (int i = 1; i < a.size(); ++i) {
        ans += a[i];
      }
    }
    std::cout << "Case #" << tnum << ": ";
    if (sm != 0 || n < 2) {
      std::cout << "NO" << std::endl;
    } else {
      std::cout << ans << std::endl;
    }
  }

  return 0;
}