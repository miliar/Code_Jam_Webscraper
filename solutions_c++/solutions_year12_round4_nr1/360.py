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
    int n;
    scanf("%d", &n);
    vector<int> d(n + 1), l(n + 1);
    for (int i = 0; i < n; ++i) 
      scanf("%d %d", &d[i], &l[i]);
    scanf("%d", &d[n]);
    l[n] = 0;
    vector<int> m(n + 1, -1);
    m[0] = d[0];
    for (int i = 0; i < n + 1; ++i)
      for (int j = i + 1; j < n + 1; ++j)
        if (d[i] + m[i] >= d[j])
          m[j] = max(m[j], min(d[j] - d[i], l[j]));
    printf("Case #%d: ", tc);
    if (m[n] == 0)
      puts("YES");
    else
      puts("NO");
  }
  return 0;
}
