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

typedef long long ll;

void inc(int &start, int N) {
  start++; if (start == N) start = 0;
}

int main(void)
{
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    ll R, k, N; cin >> R >> k >> N;
    vector <ll> g(N);
    ll tot = 0;
    for (int i = 0; i < N; i++) {
      cin >> g[i];
      tot += g[i];
    }
    ll ans = 0;
    if (tot <= k) {
      ans = tot * R;
    }
    else {
      vector <ll> tot_g(N); vector <int> first_seen(N, -1);
      first_seen[0] = 0;
      int prev_start = 0;
      int cycle_len = -1, cycle_qty = 0;
      for (int ctr = 1; ; ctr++) {
	int start = prev_start;
	tot = g[start]; inc(start, N);
	while (tot + g[start] <= k) {
	  tot += g[start];
	  inc(start, N);
	}
	tot_g.push_back(tot);
	ans += tot; R--;
	if (R == 0) break;
	if (first_seen[start] != -1) {
	  cycle_len = ctr - first_seen[start];
	  cycle_qty = accumulate(tot_g.end()-cycle_len, tot_g.end(), 0);
	  break;
	}
	prev_start = start;
	first_seen[start] = ctr;
      }
      if (R) {
	ans += (R / cycle_len) * cycle_qty;
	ans += accumulate(tot_g.end()-cycle_len,
			  tot_g.end()-cycle_len+R%cycle_len, 0);
      }
    }
    printf("Case #%d: %Ld\n", t, ans);
  }
}
