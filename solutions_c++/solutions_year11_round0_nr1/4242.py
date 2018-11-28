#include <iostream>
#include <cstdio>
#include <cmath>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int solve (char* c, int* n, int j) {
  int o = 1, b = 1;
  int t = 0;
  queue<int> po, bo;
  queue<char> co;

  for (int i = -1; ++i < j; ) {
    if (c[i] == 'O') po.push(n[i]);
    if (c[i] == 'B') bo.push(n[i]);
    co.push(c[i]);
  }

  while (true) {
    bool b_ = false;
    if (po.empty() && bo.empty()) break;
    if (po.front() == o && co.front() == 'O') {
      po.pop(), co.pop();
      b_ = true;
    }
    else if (po.front() > o) ++o;
    else if (po.front() < o) --o;
    if (bo.front() == b && co.front() == 'B' && !b_) {
      bo.pop(), co.pop();
    }
    else if (bo.front() > b) ++b;
    else if (bo.front() < b) --b;
    ++t;
  }
  return t;
}

int main () {
  int i = 0, j = 0, k = 0, l = 0;
  double x = 0, y = 0, z = 0;
  char c[1000];
  int n[1000];
  cin >> i;
  while (cin >> j) {
    for (k = -1; ++k < j; ) {
      cin >> c[k];
      cin >> n[k];
    }
    cout << "Case #" << (++l) << ": " << solve(c, n, j) << endl;
  }
}

