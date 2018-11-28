#include <cstdio>
#include <cstring>
#include <cctype>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <climits>

using namespace std;

int main() {

  int ca;
  scanf(" %d", &ca);

  for (int ii = 0; ii < ca; ii++) {

    int n, sum = 0, x = 0;
    int minv = INT_MAX;
    scanf(" %d", &n);

    for (int i = 0; i < n; i++) {
      int m;
      scanf(" %d", &m);
      x ^= m;
      sum += m;
      minv = min(minv, m);
    }
    
    printf("Case #%d: ", ii+1);
    if (x == 0) printf("%d\n", sum - minv);
    else printf("NO\n");

  }
}
