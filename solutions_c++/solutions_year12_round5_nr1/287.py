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

struct Level {
  int l, p, i;
  Level() {}
  friend inline bool operator < (const Level &a, const Level& b) {
    if (a.p != b.p)
      return a.p > b.p;
    if (a.p == 0)
      return a.i < b.i;
    if (a.l != b.l)
      return a.l < b.l;
    return a.i < b.i;
  }
};

int main(void) {
  int tt; scanf("%d", &tt);
  for (int tc = 1; tc <= tt; ++tc) {
    int n;
    scanf("%d", &n);   
    vector<Level> v(n);
    for (int i = 0; i < n; ++i) {
      scanf("%d", &v[i].l);
      v[i].i = i;
    }
    for (int i = 0; i < n; ++i)
      scanf("%d", &v[i].p);
    sort(v.begin(), v.end()); 
    printf("Case #%d:", tc);
    for (int i = 0; i < n; ++i)
      printf(" %d", v[i].i);
    printf("\n");
  }
  return 0;
}
