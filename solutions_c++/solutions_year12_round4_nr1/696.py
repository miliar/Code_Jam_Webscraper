#include <cstdio>
#include <vector>
#include <iostream>
using namespace std;

bool solve(vector<pair<int,int>> const& vines, int dest)
{
  int n = vines.size();
  vector<int> best(n);
  best[0] = vines[0].first;
  for (int i = 0; i < n; i++) {
    int d = vines[i].first;
    int x = best[i];
    if (d + x >= dest) return true;
    for (int j = i+1; j < n; j++) {
      if (d + x < vines[j].first) break;
      int nx = min(vines[j].second, vines[j].first - d);
      best[j] = max(best[j], nx);
    }
  }
  return false;
}

int main()
{
  int t;
  cin >> t;
  for (int case_ = 1; case_ <= t; case_++) {
    int n;
    cin >> n;
    vector<pair<int, int>> vines;
    for (int i = 0; i < n; i++) {
      int d, l;
      cin >> d >> l;
      vines.push_back({d, l});
    }
    int dest;
    cin >> dest;
    bool res = solve(vines, dest);
    cout << "Case #" << case_ << ": " << (res ? "YES" : "NO") << endl;
  }
  return 0;
}
