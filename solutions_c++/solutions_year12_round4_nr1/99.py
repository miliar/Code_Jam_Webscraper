#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

template<typename T, typename U> inline void relaxmax(T &res, const U &x) {
  if (x > res) {
    res = x;
  }
}
typedef long long int64;

int main() {
  cin.sync_with_stdio(0);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    int n;
    cin >> n;

    vector<int64> d(n), len(n);
    for (int i=0; i<n; ++i) {
      cin >> d[i] >> len[i];
    }
    int64 D;
    cin >> D;

    vector<int64> maxr(n, -1);
    maxr[0] = d[0];

    bool ans = false;
    for (int i=0; i<n; ++i) {
      if (maxr[i] < 0) {
        continue;
      }

      if (d[i] + maxr[i] >= D) {
        ans = true;
        break;
      }

      for (int j=i+1; j<n; ++j) {
        int64 dx = d[j] - d[i];
        if (maxr[i] >= dx) {
          relaxmax(maxr[j], min(dx, len[j]));
        }
      }
    }

    printf("Case #%d: %s\n", tt, ans ? "YES" : "NO");
  }
  
  return 0;
}
