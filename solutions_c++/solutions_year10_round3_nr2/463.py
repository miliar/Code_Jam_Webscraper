#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

int solve(long a, long b, long c) {
  if ((a * c) >= b) return 0;
  long aa = a, bb = b;
  while (bb > aa) {
    aa *= c;
    bb /= c;
  }
  int x = 1 + solve(aa, b, c);
  int y = 1 + solve(a, aa, c);
  int r = max(x, y);
  return r;
}

int main() {
  int cases;
  scanf("%d", &cases);
  for (int casei = 1; casei <= cases; ++casei) {
    long L, P, C;
    scanf("%ld%ld%ld", &L, &P, &C);
    int answer = solve(L, P, C);
    printf("Case #%d: %d\n", casei, answer);
  }
  return 0;
}
