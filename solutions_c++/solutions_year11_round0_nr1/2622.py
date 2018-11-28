#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

#define N 102

using namespace std;

namespace {

  void solve(int test_case) {
    int n;
    int len[2] = {0, 0};
    int t[2][N], who[N];

    int last_pos[2] = {1, 1}, tot_t[2] = {0, 0};
    int ret = 0, cur_pos;
    cin >> n;
    for (int i = 0; i < n; ++i) {
      string s; cin >> s;
      int cur_pos; cin >> cur_pos;
      who[i] = (s[0] == 'B');
      tot_t[who[i]] += abs(last_pos[who[i]] - cur_pos) + 1;
      last_pos[who[i]] = cur_pos;
      t[who[i]][len[who[i]]++] = tot_t[who[i]];
    }
 
    int ind[2] = {0, 0};
    int wait[2] = {0, 0};
    int cur_t = 0;
    for (int step = 0; step < n; ++step) {
      int w = who[step];
      int i = ind[w];
      int next_t = wait[w] + t[w][i];
      if (next_t <= cur_t) {
	wait[w] += cur_t - next_t + 1;
	++cur_t;
      } else
	cur_t = next_t;
      ++ind[w];
    }
    cout << "Case #" << test_case << ": " << cur_t << endl;
  }
  
}

int main() {
  int n_tc; cin >> n_tc;
  for (int i = 1; i <= n_tc; ++i)
    solve(i);
  return 0;
}
