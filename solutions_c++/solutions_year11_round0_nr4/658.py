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
    int N; cin >> N;
    int ans = 0;
    for (int i = 1; i <= N; i++) {
      int j; cin >> j;
      ans += i != j;
    }
    printf("Case #%d: %d\n", t, ans);
  }
}
