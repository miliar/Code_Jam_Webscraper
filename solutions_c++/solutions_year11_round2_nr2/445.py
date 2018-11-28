#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <utility>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>

typedef long long LL;


LL n, d;
std::vector<LL> a;

bool Can(LL x) {
  LL t = a[0]-x;
  for (int i = 1; i < a.size(); ++i) {
    if (a[i]+x < t+d) {
      return false;
    } else {
      t = std::max<LL>(t+d, a[i]-x);
    }
  }
  return true;
}


int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int t;

  std::cin >> t;
  for (int q = 0; q < t; ++q) {
    std::cin >> n >> d;
    d *= 2;
    a.clear();
    for (int i = 0; i < n; ++i) {
      int p, v;
      std::scanf("%d %d", &p, &v);
      for (int j = 0; j < v; ++j) {
        a.push_back(p*2);
      }
    }
    
    std::sort(a.begin(), a.end());
    LL l = -1, r = 100000000000000000L;
    while (r-l > 1) {
      LL x = (l+r)/2;
      if (Can(x)) {
        r = x;
      } else {
        l = x;
      }
    }
    std::printf("Case #%d: ", q+1);
    if (r%2 == 1) {
      std::printf("%lld.5\n", r/2);
    } else {
      std::printf("%lld.0\n", r/2);
    }
  }

  return 0;
}