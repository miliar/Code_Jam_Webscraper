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

int main() {
  int cases;
  int cache[32];
  for (int i = 0; i < 32; ++i)
    cache[i] = -1;
  scanf("%d", &cases);
  for (int casei = 1; casei <= cases; ++casei) {
    long answer = 0;
    int n;
    scanf("%d", &n);
    if (cache[n] >= 0) {
      answer = cache[n];
    } else {
      for (int m = (1 << (n + 1)) - 4; m; m -= 4) {
        vector<int> v;
        for (int i = 2; i <= n; ++i)
          if (m & (1 << i))
            v.push_back(i);
        for (int x = 1; ; x = v[x - 1]) {
          if (x == n) {
            ++answer;
            break;
          } else if (x > v.size()) {
            break;
          }
        }
      }
      cache[n] = answer;
    }
    printf("Case #%d: %d\n", casei, answer % 100003);
  }
  return 0;
}
