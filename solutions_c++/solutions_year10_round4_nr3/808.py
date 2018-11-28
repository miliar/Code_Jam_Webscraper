#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cctype>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <list>
#include <functional>
#include <numeric>
#include <bitset>
#include <ext/hash_set>
#include <ext/hash_map>
#include <stdexcept>
using namespace std;

int maj(int a, int b, int c) {
  return a + b + c >= 2;
}

vector< vector<int> > m1, m2;

int main() {
  int cases;
  scanf("%i", &cases);
  for (int numcase = 1; numcase <= cases; ++numcase) {
    int numrect;
    scanf("%i", &numrect);

    m1.resize(102, vector<int>(102));
    for (int i = 0; i < numrect; ++i) {
      int x1, y1, x2, y2;
      scanf("%i%i%i%i", &x1, &y1, &x2, &y2);
      if (x1 > x2) swap(x1, x2);
      if (y1 > y2) swap(y1, y2);
      for (int x = x1; x <= x2; ++x)
        for (int y = y1; y <= y2; ++y)
          m1[x][y] = 1;
    }
    printf("Case #%i: ", numcase);

    m2 = m1;
    for (int steps = 0; ; ++steps) {
      int cnt = 0;
      for (int i = 0; i <= 101; ++i)
        for (int j = 0; j <= 101; ++j) 
          if (m1[i][j]) ++cnt;
      if (cnt == 0) {
        printf("%i\n", steps);
        break;
      }
      for (int i = 0; i <= 101; ++i)
        for (int j = 0; j <= 101; ++j) {
          int a = i ? m1[i - 1][j] : 0,
              b = j ? m1[i][j - 1] : 0;
          m2[i][j] = maj(a, b, m1[i][j]);
        }
      swap(m1, m2);
    }
  }
  return 0;
}
