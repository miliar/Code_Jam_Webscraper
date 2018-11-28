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

struct level {
  int L, P, ind;
  level(int l, int p, int i) : L(l), P(p), ind(i) {}
  bool operator < (const level &lev2) const {
    int lhs = L * lev2.P, rhs = lev2.L * P;
    if (lhs < rhs) return true;
    else if (lhs > rhs) return false;
    else return ind < lev2.ind;
  }
};

int main(void) {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    int N; cin >> N;
    vector <int> L(N), P(N);
    for (int i = 0; i < N; i++)
      cin >> L[i];
    for (int i = 0; i < N; i++)
      cin >> P[i];
    vector <level> levs;
    for (int i = 0; i < N; i++)
      levs.push_back(level(L[i], P[i], i));
    sort(levs.begin(), levs.end());
    printf("Case #%d:", t);
    for (int i = 0; i < N; i++)
      cout << " " << levs[i].ind;
    cout << endl;
  }
}
