#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <set>
#include <assert.h>
#include <stdio.h>
using namespace std;
char grid[205][205];
int main() {
  int nocases;
  cin >> nocases;
  for (int rr = 1; rr <= nocases; ++rr) {
    int R;
    set<pair <int, int> > S;
    cin >> R;
    for (int i = 0; i < R; ++i) {
      int x1, y1, x2, y2;
      cin >> x1 >> y1 >> x2 >> y2;
      for (int i = x1; i <= x2; ++i)
	for (int j = y1; j <= y2; ++j)
	  S.insert(make_pair(i, j));
    }
    int t = 0;
    while (S.size()) {
      set<pair <int, int> > T;
      for (set< pair<int, int> >::iterator iter = S.begin(); iter != S.end(); ++iter) {
	pair<int, int> p = *iter;
	if (S.find(make_pair(p.first+1, p.second-1)) != S.end())
	  T.insert(make_pair(p.first+1, p.second));
	if ((S.find(make_pair(p.first-1, p.second)) != S.end()) ||
	    (S.find(make_pair(p.first, p.second-1)) != S.end()))
	  T.insert(p);
      }
      S = T, ++t;
    }
    printf("Case #%d: %d\n", rr, t);
  }
  return 0;
}
