#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <vector>
using namespace std;

bool can(multiset<int> values, int minlen) {
  map<int, int> seqs_by_end;
  while (!values.empty()) {
    int a = *values.begin(); values.erase(values.begin());
    int b = a+minlen-1;
    int i;
    for (i=a+1; i<=b; ++i) {
      multiset<int>::iterator it = values.find(i);
      if (it == values.end()) {
        break;
      }
      values.erase(it);
    }
    if (i > b) {
      ++seqs_by_end[b];
    } else {
      if (!seqs_by_end[a-1]) {
        return false;
      }
      --seqs_by_end[a-1];
      ++seqs_by_end[i-1];
    }
  }
  return true;
}

int main(void) {
  cin.sync_with_stdio(0);

  int CASES; cin >> CASES;
  for (int tt=1; tt<=CASES; ++tt) { // caret here
    int n; cin >> n;
    multiset<int> values;
    for (int i=0; i<n; ++i) {
      int x; cin >> x;
      values.insert(x);
    }

    int lo = 1, hi = n;
    while (lo < hi) {
      int mid = (lo + hi + 1) / 2;
      if (can(values, mid)) {
        lo = mid;
      } else {
        hi = mid-1;
      }
    }

    if (n == 0) lo = 0;

    cout << "Case #" << tt << ": " << lo << endl;
  }

  return 0;
}
