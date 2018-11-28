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
    int N; scanf("%d", &N);
    int x = 0, s = 0, m = 1 << 30;
    while (N--) {
      int C; scanf("%d", &C);
      x ^= C;
      s += C;
      m = min(m, C);
    }
    printf("Case #%d: ", t); 
    if (x) 
      puts("NO"); 
    else 
      printf("%d\n", s - m);
  }
  return 0;
}
