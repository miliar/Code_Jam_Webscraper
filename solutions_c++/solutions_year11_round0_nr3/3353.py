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
  
  int t, n, sum;
  
  std::cin >> t;
  for (int t_cnter = 1; t_cnter <= t; ++t_cnter) {
    a.clear();
    std::cin >> n;
    sum = 0;
    for (int i = 0; i < n; ++i) {
      int new_value;
      std::cin >> new_value;
      sum = sum ^ new_value;
      a.push_back(new_value);
    }
    std::cout << "Case #" << t_cnter << ": ";
    int ans = 0;
    if (sum == 0 && n >= 2) {
      std::sort(a.begin(), a.end());
      for (int i = 1; i < a.size(); ++i) {
        ans += a[i];
      }
    }
    if (sum != 0 || n < 2) {
      std::cout << "NO" << std::endl;
    } else {
      std::cout << ans << std::endl;
    }
  }

  return 0;
}