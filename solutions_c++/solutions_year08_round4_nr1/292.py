#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int T;

struct Node {
  bool val, isL, ch;
  Node() : val(false), isL(false), ch(false) {}
};

int m;
Node tree[100001];

int mres[10001][2];

#define CH(i) (tree[i].ch ? 1 : 10000)

int minNeed(int node, int need) {
  if (tree[node].isL) return (tree[node].val == need) ? 0 : 10000;

  if (!mres[node][need]) {
    int res = 10000;
    bool isA = tree[node].val == 1;
    if (need == 1) {
      res = min(res, minNeed(2 * node, 1) + minNeed(2 * node + 1, 1) + (isA ? 0 : CH(node))); // AND
      res = min(res, min(minNeed(2 * node, 1), minNeed(2 * node + 1, 1)) + (isA ? CH(node) : 0)); // OR
    }
    else {
      res = min(res, min(minNeed(2 * node, 0), minNeed(2 * node + 1, 0)) + (isA ? 0 : CH(node)));
      res = min(res, minNeed(2 * node, 0) + minNeed(2 * node + 1, 0) + (isA ? CH(node) : 0));
    }

    mres[node][need] = res + 1;
  }

  return mres[node][need] - 1;
}

int main() {

  cin >> T;
  for (int nn = 1; nn <= T; nn++) {
    int v; cin >> m >> v;
    memset(mres, 0, sizeof mres);

    for (int i = 1; i <= (m - 1)/2; i++) {
      int a, c; cin >> a >> c;
      tree[i].val = a == 1;
      tree[i].ch = c == 1;
      tree[i].isL = false;
    }

    for (int i = (m - 1)/2 + 1; i <= m; i++) {
      int a; cin >> a; tree[i].val = a == 1; tree[i].isL =true;
    }

    int res = minNeed(1, v);

    cout << "Case #" << nn << ": ";
    if (res >= 10000) cout << "IMPOSSIBLE"; else cout << res;
    cout << endl;
  }

  return 0;
}