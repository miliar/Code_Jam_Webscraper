#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

bool solve(long n, long k) {
  return ((k % (1 << n)) + 1) == (1 << n);
}

int main() {
  int cases;
  scanf("%d", &cases);
  for (int i = 1; i <= cases; ++i) {
    long n, k;
    scanf("%ld%ld", &n, &k);
    bool on = solve(n, k);
    printf("Case #%d: %s\n", i, on ? "ON": "OFF");
  }

  return 0;
}
