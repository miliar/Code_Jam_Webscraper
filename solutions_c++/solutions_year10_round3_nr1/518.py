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
  for (int casei = 1; casei <= cases; ++casei) {
    int n;
    scanf("%d", &n);
    set<int> left, right;
    map<int, int> x;
    for (int i = 0; i < n; ++i) {
      int l, r;
      scanf("%d%d", &l, &r);
      left.insert(l);
      right.insert(r);
      x[l] = r;
    }
    int answer = 0;
    for (map<int, int>::const_iterator it = x.begin();
         it != x.end(); ++it) {
      int dleft = distance(left.begin(), left.find(it->first));
      int dright = distance(right.begin(), right.find(it->second));
      answer += abs(dright - dleft);
    }
    answer /= 2;
    printf("Case #%d: %d\n", casei, answer);
  }
  return 0;
}
