#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <string>
using namespace std;

int M = 10000;

int solve()
{
  int n;
  scanf("%d", &n);
  map<string, int> colors;
  vector<pair<int, pair<int, int> > > data;
  for (int i = 0; i < n; i++) {
    char col[999];
    int a, b;
    scanf(" %s %d %d", col, &a, &b);
    if (colors.count(string(col)) == 0) colors[col] = colors.size();
    data.push_back(make_pair(colors[col], make_pair(a, b)));
  }
  int res = 999999;
  for (int S = 0; S < (1 << n); S++) {
    set<int> used;
    for (int i = 0; i < n; i++) if (S & (1 << i)) used.insert(data[i].first);
    if (used.size() > 3) continue;
    bool painted[11111] = {};
    for (int i = 0; i < n; i++) {
      if (!(S & (1 << i))) continue;
      for (int j = data[i].second.first; j <= data[i].second.second; j++) painted[j] = true;
    }
    bool ok = true;
    for (int i = 1; i <= M; i++) if (!painted[i]) ok = false;
    if (ok) res = min(res, __builtin_popcount(S));
  }
  if (res > n) return -1;
  return res;
}

int main()
{
  int t;
  scanf("%d", &t);
  for (int c = 0; c < t; c++) {
    printf("Case #%d: ", c+1);
    int res = solve();
    if (res < 0) puts("IMPOSSIBLE");
    else printf("%d\n", res);
  }
}
