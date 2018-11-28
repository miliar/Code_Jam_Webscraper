#include <iostream>
#include <cstdio>
#include <sstream>
#include <set>

using namespace std;

pair<int, int> ten(int x)
{
  int res = 1, pow = 0;
  x /= 10;
  while (x > 0) {
    ++pow;
    res *= 10;
    x /= 10;
  }
  return make_pair(res, pow);
}

int rotate(int n, int up_val)
{
  pair<int, int> p = ten(n);
  int factor = p.first, pow = p.second;
  int res = 0;
  int n__ = n;

  set<int> ss;
  for (int i = 0; i < pow; ++i) {
    n = (n % 10) * factor + (n / 10);
    if (n > n__ && n <= up_val && ss.find(n) == ss.end()) {      
      ++res;
      ss.insert(n);
    }       
  }
  return res;
}

int main()
{
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    int A, B;
    cin >> A >> B;
    int res = 0;
    for (int i = A; i <= B; ++i)
      res += rotate(i, B);
    printf("Case #%d: %d\n", test, res);
  }
  return 0;
}
