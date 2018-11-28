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
    int N; cin >> N;
    vector <int> d(N), len(N);
    for (int i = 0; i < N; i++)
      cin >> d[i] >> len[i];
    int D; cin >> D;
    bool ok = false;
    vector <int> max_len(N);
    max_len[0] = d[0];
    for (int i = 0; i < N; i++) {
      for (int j = i+1; j < N; j++)
	if (max_len[i] + d[i] >= d[j])
	  max_len[j] = max(max_len[j], min(len[j], d[j]-d[i]));
      if (max_len[i] + d[i] >= D)
	ok = true;
    }
    printf("Case #%d: %s\n", t, ok ? "YES" : "NO");
  }
}
