#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <string.h>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <sstream>
using namespace std;
long long gcd(long long a, long long b) { return !b?a:gcd(b, a%b); }
int main(int argc, char* argv[]) {
  int nocases;
  cin >> nocases;
  for (int rr = 1; rr <= nocases; ++rr) {
    long long n, pd, pg, a, b, c, d, e;
    cin >> n >> pd >> pg;
    e = gcd(pd, 100);
    a = pd / e, b = 100 / e;
    e = gcd(pg, 100);
    c = pg / e, d = 100 / e;
    if (b > n)
      printf("Case #%d: Broken\n", rr);
    else if (c==1&&d==1&&(a!=1||b!=1))
      printf("Case #%d: Broken\n", rr);
    else if (!c && a)
      printf("Case #%d: Broken\n", rr);
    else
      printf("Case #%d: Possible\n", rr);
  }
  return 0;
}
