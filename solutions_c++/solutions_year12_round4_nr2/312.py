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

int main(void) {
  int tt; scanf("%d", &tt);
  for (int tc = 1; tc <= tt; ++tc) {
    int n, w, l;
    scanf("%d %d %d", &n, &w, &l);
    vector<pair<int,int> > r(n);
    for (int i = 0; i < n; ++i) {
      scanf("%d", &r[i].first);
      r[i].second = i;
    }
    sort(r.begin(), r.end());
    reverse(r.begin(), r.end());
    vector<pair<int, int> > s(n);
    int x = 0;
    int y = l + 1;
    int h = 0;
    for (int i = 0; i < n; ++i) {
      if (y != 0 && y + r[i].first > l) {
        x += h;
        if (h != 0)
          x += r[i].first;
        h = r[i].first;
        y = 0;
      }
      if (y == 0) {
        s[r[i].second] = make_pair(x, 0);
        y += r[i].first;
      } else {
        s[r[i].second] = make_pair(x, y + r[i].first);
        y += 2 * r[i].first;
      }
    }
    printf("Case #%d:", tc);
    for (int i = 0; i < n; ++i)
      printf(" %d %d", s[i].first, s[i].second);
    printf("\n");
  }
  return 0;
}
