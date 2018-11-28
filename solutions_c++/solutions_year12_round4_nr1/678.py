#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>

using namespace std;

vector<pair<int, int> > vines;
map<pair<int, int>, bool> dp;
int N;


bool solve(int i, int D, int dist) {
  int j = i + 1;
  if (dp.find(make_pair(i, dist)) != dp.end())
    return dp[make_pair(i, dist)];
  bool ret = false;
  if (vines[i].first + min(dist, vines[i].second) >= D)
    return true;
  while (j < N && vines[j].first <= vines[i].first + min(dist, vines[i].second)) {
    if (solve(j, D, vines[j].first - vines[i].first)) {
      dp[make_pair(i, dist)] = true;
      return true;
    }
    ++j;
  }
  dp[make_pair(i, dist)] = false;
  return false;
}

int main() {
  int d, l, T, D;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    cin >> N;
    vines.clear();
    dp.clear();
    for (int i = 0; i < N; ++i) {
      cin >> d >> l;
      vines.push_back(make_pair(d, l));
    }
    cin >> D;
    bool ret = solve(0, D, min(vines[0].second, vines[0].first));
    if (ret)
      cout << "Case #" << t+1 << ": YES" << endl;
    else
      cout << "Case #" << t+1 << ": NO" << endl;
  }
  return 0;
}
