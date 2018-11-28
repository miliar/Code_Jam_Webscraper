#include <cstdio>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <sstream>
using namespace std;
typedef long long ll;

int main() {

  int T;
  scanf(" %d", &T);

  for (int ii = 0; ii < T; ii++) {
    int N, S, p;
    scanf(" %d%d%d", &N, &S, &p);
    int ans = 0;
    for (int i = 0; i < N; ++i) {
      int t; scanf(" %d", &t);
      int d = t / 3 + (t % 3 > 0 ? 1 : 0);
      if (d >= p) {
	ans++;
      } else {
	if (d == p - 1 && S > 0 && ((t % 3 == 0 && t >= 3) || t % 3 == 2)) {
	  ans++;
	  S--;
	}
      }
    }
    printf("Case #%d: %d\n", ii + 1, ans);
  }
}
