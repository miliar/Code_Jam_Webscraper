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
  scanf("%d", &cases);
  for (int case_i = 1; case_i <= cases; ++case_i) {
    int nr;
    set<pair<int, int> > points;
    scanf("%d", &nr);
    for (int i = 0; i < nr; ++i) {
      int a, b, c, d;
      scanf("%d%d%d%d\n", &a, &b, &c, &d);
      for (int x = a; x <= c; ++x)
        for (int y = b; y <= d; ++y)
          points.insert(make_pair(x, y));
    }

    long answer = 0;
    while (!points.empty()) {
      set<pair<int, int> > next;
      for (set<pair<int, int> >::const_iterator cit = points.begin();
           cit != points.end(); ++cit) {
        if (points.find(make_pair(cit->first-1, cit->second)) != points.end()
            or points.find(make_pair(cit->first, cit->second-1)) != points.end())
          next.insert(make_pair(cit->first, cit->second));
        if (points.find(make_pair(cit->first - 1, cit->second + 1)) != points.end())
          next.insert(make_pair(cit->first, cit->second + 1));
        if (points.find(make_pair(cit->first + 1, cit->second - 1)) != points.end())
          next.insert(make_pair(cit->first + 1, cit->second));
      }
      swap(points, next);
      ++answer;
    }

    printf("Case #%d: %ld\n", case_i, answer);
  }
  return 0;
}
