#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <numeric>
#include <utility>

using namespace std;

int main(void) {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    int N, S, p; cin >> N >> S >> p;
    int ans = 0;
    for (int i = 0; i < N; i++) {
      int ti; cin >> ti;
      int s1 = (ti+2)/3, s2 = (ti+4)/3;
      if (s1 >= p) ans++;
      else if (s2 >= p && ti && S) {
	ans++;
	S--;
      }
    }
    printf("Case #%d: %d\n", t, ans);
  }
}
