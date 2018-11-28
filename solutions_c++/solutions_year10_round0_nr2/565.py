#include <iostream>
#include <vector>
#include <algorithm>

typedef int myint;

myint calc_gcd(myint const& x, myint const& y)
{
  myint const mod(y % x);
  return (mod == 0) ? x : calc_gcd(mod, x);
}

int
main()
{
  int C;
  std::cin >> C;
  for (int i(1); i <= C; ++i) {
    int N;
    std::cin >> N;
    std::vector<myint> t(N);
    for (int j(0); j < N; ++j) {
      std::cin >> t[j];
    }
    std::sort(t.begin(), t.end());
    std::vector<myint> diff(N - 1);
    for (int j(0); j < N - 1; ++j) {
      diff[j] = t[j + 1] - t[j];
    }
    std::sort(diff.begin(), diff.end());
    int gcd(diff[0]);
    for (int j(1); j < diff.size(); ++j) {
      gcd = gcd == 0 ? diff[j] : calc_gcd(gcd, diff[j]);
    }
    std::cout << "Case #" << i << ": "
      << (t[0] % gcd == 0 ? 0 : gcd * (t[0] / gcd + 1) - t[0]) << '\n';
  }
  return 0;
}
