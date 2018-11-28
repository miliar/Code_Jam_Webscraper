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
    int see[1024];
    int cost[10][1024];
    memset(see, 0, sizeof(see));
    memset(cost, 0, sizeof(cost));
    int p;
    scanf("%d", &p);
    for (int i = 0; i < (1 << p); ++i) {
      int x;
      scanf("%d", &x);
      see[i] = p - x;
    }

    for (int row = 0; row < p; ++row) {
      int thisp = p - row - 1;
      for (int i = 0; i < (1 << thisp); ++i) {
        scanf("%d", &cost[row][i]);
      }
    }

    set<pair<int, int> > get;
    for (int i = 0; i < (1 << p); ++i) {
      int x = i;
      for (int j = 0; j < p; ++j) {
        x /= 2;
        if (j >= (p - see[i])) {
          get.insert(make_pair(j, x));
        }
      }
    }

    long answer = 0;
    for (set<pair<int, int> >::const_iterator cit = get.begin();
         cit != get.end(); ++cit) {
      answer += cost[cit->first][cit->second];
    }

    printf("Case #%d: %ld\n", case_i, answer);
  }
  return 0;
}
