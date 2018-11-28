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
  int T; scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    int t1, t2, x1, x2;
    t1 = t2 = 0;
    x1 = x2 = 1;
    int N; scanf("%d", &N);
    for (int i = 0; i < N; ++i) {
      char r; int x;
      scanf(" %c %d", &r, &x);
      switch (r) {
        case 'O': 
          t1 += abs(x1 - x) + 1;
          t1 = max(t1, t2 + 1);
          x1 = x;
          break;
        case 'B': 
          t2 += abs(x2 - x) + 1;
          t2 = max(t2, t1 + 1);
          x2 = x;
      }
    }
    printf("Case #%d: %d\n", t, max(t1, t2));
  }
  return 0;
}
