#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

int main(void)
{
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    int N; cin >> N; int sum = 0, small = 1<<20, xorsum = 0;
    for (int i = 0; i < N; i++) {
      int x; cin >> x;
      sum += x; small <?= x; xorsum ^= x;
    }
    if (xorsum == 0)
      printf("Case #%d: %d\n", t, sum - small);
    else
      printf("Case #%d: NO\n", t);
  }
}
