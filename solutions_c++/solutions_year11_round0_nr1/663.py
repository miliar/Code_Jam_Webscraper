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
    int pos[2]; pos[0] = pos[1] = 1;
    int buf[2]; buf[0] = buf[1] = 0;
    for (int i = 0; i < N; i++) {
      char bot; int p; cin >> bot >> p;
      int b = bot == 'O';
      int x = 1 + max(0, abs(p - pos[b]) - buf[b]);
      ans += x;
      pos[b] = p; buf[b] = 0;
      buf[1-b] += x;
    }
    printf("Case #%d: %d\n", t, ans);
  }
}
