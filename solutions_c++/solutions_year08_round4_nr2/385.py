#include <iostream>
#include <queue>
#include <cmath>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;
int mabs(int x) { return x<0?-x:x; }
int main() {
  int no_cases;
  cin >> no_cases;
  for (int rr = 1; rr <= no_cases; ++rr) {
    int n, m, a;
    cin >> n >> m >> a;
    bool found = false;
    for (int x1 = 0; x1 <= n; ++x1)
      for (int y1 = 0; y1 <= m; ++y1)
	for (int x2 = 0; x2 <= n; ++x2)
	  for (int y2 = 0; y2 <= m; ++y2) {
	    if (mabs(x2*y1 - x1*y2) == a) {
	      printf("Case #%d: 0 0 %d %d %d %d\n", rr, x1, y1, x2, y2);
	      found = true;
	      goto done;
	    }
	  }
  done:
    if (!found)
      printf("Case #%d: IMPOSSIBLE\n", rr);
  }
  return 0;
}
