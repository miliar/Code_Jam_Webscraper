#include <string>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <queue>
#include <cassert>

using namespace std;

typedef long long llint;

llint gcd(llint a, llint b) {
  return !b ? a : gcd(b, a % b);
}
llint lcm(llint a, llint b) {
  return (a * b) / gcd(a, b);
}

int main(void)
{
  int T; scanf("%d", &T);

  for (int t = 1; t <= T; ++t) 
  {
    llint n, pd, pg;
    scanf("%lld %lld %lld", &n, &pd, &pg);

    llint dmin;
    if (pd == 0) 
      dmin = 1;
    else 
      dmin = lcm(100, pd) / pd;

    printf("Case #%d: ", t);
    if (dmin > n || pd > 0 && pg == 0 || pd < 100 && pg == 100)
      puts("Broken");
    else 
      puts("Possible");
  }

  return 0;
}
