#include <iostream>
#include <cstdio>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <numeric>
#include <functional>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <string>
#include <sstream>
#include <fstream>
#include <complex>
#include <iterator>
#include <memory>
#include <utility>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define rep(i,s,n) for(int i=s;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
#define MP(a, b) make_pair((a), (b))
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long double ld;
typedef long long ll;

const int M = 1000;
int T, N;
int ns[1000];

int Dfs(int c, const vector<int>& ns, vector<bool>& visited) {
  visited[c] = true;
  if (!visited[ns[c]])
    return Dfs(ns[c], ns, visited) + 1;
  return 1;
}

ll ExpectCycle(int n) {
  if (n <= 1) return 0;
  return n;
}

ll Expect(const vector<int>& v) {
  vector<bool> visited(v.size());
  ll res = 0;
  REP(i, v.size()) if (!visited[i]) {
    int num = Dfs(i, v, visited);
    if (num == (int) v.size()) return -1;
    res += ExpectCycle(num);
  }
  return res;
}

ll Expect() {
  vector<int> v(N);
  REP(i, N) v[i] = ns[i];
  ll e = Expect(v);
  return e < 0 ? ExpectCycle(N) : e;
}

int main() {
  cin >> T;
  REP(turn, T) {
    cin >> N;
    REP(i, N) {
      cin >> ns[i];
      --ns[i];
    }
    ll ans = Expect();
    printf("Case #%d: %lld.000000\n", turn + 1, ans);
  }
  return 0;
}
