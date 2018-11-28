#include <iostream>
#include <map>
#include <algorithm>
#include <sstream>
#include <vector>
#include <iomanip>
#include <cassert>
#include <queue>
using namespace std;
bool solve2(vector<vector<int> >&g, int N, int st)
{
  if (N == 1) return false;
  vector<int> cnt(N);
  priority_queue<int> pq;
  for (int i = 0; i < g[st].size(); ++i)
    pq.push(g[st][i]);

  while (!pq.empty()) {
    // if (cnt.at(N-1) > 1) return true;
    int v = pq.top();
    pq.pop();
    ++cnt[v];
    if (cnt.at(v) > 1) return true;
    for (int i = 0; i < g[v].size(); ++i)
      pq.push(g[v][i]);
  }

  for (int i = 0; i < N; ++i) {
    if (cnt.at(i) > 1) return true;
  }
  return false;
}
bool solv(vector<vector<int> >&g, int N)
{
  for (int i = 0; i < N; ++i) {
    if (solve2(g, N, i)) return true;
  }
  return false;
}
int main()
{
  int sz, now = 1;
  cin >> sz;
  for (int sz_i = 0; sz_i < sz; ++sz_i) {
    int N; cin >> N;
    vector<vector<int> > g(N, vector<int>());
    for (int i = 0; i < N; ++i) {
      int mi; cin >> mi;
      for (int j = 0; j < mi; ++j) {
        int v; cin >> v;
        g[i].push_back(v - 1);
      }
    }
    bool ret = solv(g, N);
    stringstream ss;
    ss << "Case #" << now++ << ": ";
    cout << ss.str() << (ret ? "Yes" : "No") << endl;
  }
}
